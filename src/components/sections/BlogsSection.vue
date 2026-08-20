<template>
  <div class="container" id="blogs-section">
    <el-row>
      <el-col class="blogs-section">
        <div class="header">
          <div class="greetings">Blogs</div>
          <p class="description">Notes on engineering, product, and experiments.</p>
          <div class="meta-row">
            <div class="stat">
              <span class="stat-number">{{ totalBlogs }}</span> posts
            </div>
            <div class="stat">
              <span class="stat-number">{{ tagCount }}</span> topics
            </div>
            <div v-if="filtersActive" class="stat">
              Showing {{ filteredBlogs.length }} of {{ totalBlogs }}
            </div>
          </div>
        </div>

        <div class="controls">
          <div class="control-group">
            <label class="control-label" for="blog-search">Search</label>
            <input
              id="blog-search"
              v-model="searchQuery"
              class="search-input"
              type="text"
              placeholder="Search titles, tags, or keywords"
              aria-label="Search blogs"
            />
          </div>

          <div class="control-group">
            <label class="control-label" for="blog-sort">Sort</label>
            <select id="blog-sort" v-model="sortBy" class="sort-select" aria-label="Sort blogs">
              <option value="newest">Newest first</option>
              <option value="oldest">Oldest first</option>
              <option value="title-asc">Title A-Z</option>
              <option value="title-desc">Title Z-A</option>
            </select>
          </div>

          <button
            v-if="filtersActive"
            class="clear-btn"
            type="button"
            @click="clearFilters"
          >
            Clear filters
          </button>
        </div>

        <div class="tags-row">
          <button
            v-for="tag in tagOptions"
            :key="tag"
            type="button"
            class="tag-chip"
            :class="{ active: selectedTag === tag }"
            @click="selectTag(tag)"
          >
            {{ tag === 'all' ? 'All' : tag }}
          </button>
        </div>

        <div v-if="filteredBlogs.length === 0" class="empty-state">
          No posts match your filters. Try clearing or adjusting the search.
        </div>

        <div class="blog-list">
          <article class="blog-card" v-for="blog in filteredBlogs" :key="blog.title">
            <div class="blog-head">
              <button class="blog-title" type="button" @click="toggleBlog(blog)">
                {{ blog.title }}
              </button>
              <div class="blog-meta">
                <span class="blog-date">{{ blog.time }}</span>
                <span class="meta-dot"></span>
                <span class="blog-read">{{ blog.readTime }} min read</span>
              </div>
            </div>

            <div class="tag-line">
              <button
                v-for="tag in blog.tags || []"
                :key="tag"
                type="button"
                class="tag-chip tag-chip--small"
                @click.stop="selectTag(tag)"
              >
                {{ tag }}
              </button>
            </div>

            <div
              v-if="isExpanded(blog)"
              class="blog-description"
              v-html="blog.content"
            ></div>
            <div
              v-else
              class="blog-description blog-description--preview"
              @click="toggleBlog(blog)"
            >
              {{ blog.excerpt }}
            </div>

            <div class="blog-actions">
              <button class="ghost-btn" type="button" @click="toggleBlog(blog)">
                {{ isExpanded(blog) ? 'Collapse' : 'Read full' }}
              </button>
            </div>
          </article>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import data from '../../assets/blogs/blogs.json'

const months = [
  'January', 'February', 'March', 'April', 'May', 'June',
  'July', 'August', 'September', 'October', 'November', 'December'
]

export default {
  name: 'BlogsSection',
  data() {
    return {
      localBlogs: [],
      searchQuery: '',
      selectedTag: 'all',
      sortBy: 'newest',
      expandedTitle: ''
    }
  },
  created() {
    this.localBlogs = this.prepareBlogs(data)
  },
  mounted() {
    const node = document.getElementById('blogs-section')
    if (node) node.scrollIntoView()
  },
  computed: {
    tagOptions() {
      const tags = new Set()
      this.localBlogs.forEach((blog) => {
        (blog.tags || []).forEach((tag) => tags.add(tag))
      })
      return ['all', ...Array.from(tags).sort()]
    },
    filteredBlogs() {
      let list = this.localBlogs.slice()
      const query = this.searchQuery.trim().toLowerCase()
      if (query) {
        list = list.filter((blog) => blog.searchText.includes(query))
      }
      if (this.selectedTag !== 'all') {
        list = list.filter((blog) => (blog.tags || []).includes(this.selectedTag))
      }
      if (this.sortBy === 'oldest') {
        list.sort((a, b) => a.dateValue - b.dateValue)
      } else if (this.sortBy === 'title-asc') {
        list.sort((a, b) => a.title.localeCompare(b.title))
      } else if (this.sortBy === 'title-desc') {
        list.sort((a, b) => b.title.localeCompare(b.title))
      } else {
        list.sort((a, b) => b.dateValue - a.dateValue)
      }
      return list
    },
    totalBlogs() {
      return this.localBlogs.length
    },
    tagCount() {
      return Math.max(this.tagOptions.length - 1, 0)
    },
    filtersActive() {
      return this.searchQuery.trim() !== '' || this.selectedTag !== 'all' || this.sortBy !== 'newest'
    }
  },
  methods: {
    selectTag(tag) {
      if (tag === 'all') {
        this.selectedTag = 'all'
        return
      }
      this.selectedTag = this.selectedTag === tag ? 'all' : tag
    },
    clearFilters() {
      this.searchQuery = ''
      this.selectedTag = 'all'
      this.sortBy = 'newest'
    },
    isExpanded(blog) {
      return this.expandedTitle === blog.title
    },
    async toggleBlog(blog) {
      const isOpen = this.isExpanded(blog)
      this.expandedTitle = isOpen ? '' : blog.title
      if (this.expandedTitle && blog && blog.contentSource && !blog.contentLoaded) {
        try {
          const base = process.env.BASE_URL || '/'
          const res = await fetch(base + blog.contentSource)
          const html = await res.text()
          const sanitized = html.replace(/<script[\s\S]*?<\/script>/gi, '')
          blog.content = sanitized
          blog.contentLoaded = true
        } catch (e) {
          blog.content = '<p>Failed to load article. Please try again.</p>'
        }
      }
    },
    getMonthIndex(monthName) {
      return months.indexOf(monthName)
    },
    getDateValue(dateString) {
      if (!dateString) return 0
      const parts = dateString.split(' ')
      if (parts.length < 3) return 0
      const day = parseInt(parts[0], 10)
      const monthIndex = this.getMonthIndex(parts[1])
      const year = parseInt(parts[2], 10)
      if (Number.isNaN(day) || Number.isNaN(year) || monthIndex < 0) return 0
      return new Date(year, monthIndex, day).getTime()
    },
    stripHtml(html) {
      if (!html) return ''
      return html.replace(/<[^>]*>/g, ' ').replace(/\s+/g, ' ').trim()
    },
    getExcerpt(text, maxLength = 200) {
      if (!text) return ''
      if (text.length <= maxLength) return text
      const truncated = text.slice(0, maxLength)
      return truncated.replace(/\s+\S*$/, '') + '...'
    },
    prepareBlogs(allBlogs) {
      const cleaned = allBlogs.filter((blog) => !(blog.tags || []).includes('personal'))
      return cleaned.map((blog) => {
        const plain = this.stripHtml(blog.content || '')
        const wordCount = plain ? plain.split(/\s+/).length : 0
        const readTime = Math.max(1, Math.round(wordCount / 220))
        const searchText = [blog.title, plain, ...(blog.tags || [])].join(' ').toLowerCase()
        return {
          ...blog,
          excerpt: this.getExcerpt(plain, 220),
          searchText,
          wordCount,
          readTime,
          dateValue: this.getDateValue(blog.time)
        }
      })
    }
  }
}
</script>

<style scoped>
.container {
  background-color: transparent;
  height: 100%;
  overflow-y: hidden;
}
.blogs-section {
  overflow-y: scroll;
  height: calc(100vh - 60px);
  background: transparent;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  padding-bottom: 60px;
}
.blogs-section .header {
  width: min(960px, 90%);
  text-align: left;
  margin-top: 20px;
}
.blogs-section .greetings {
  color: var(--color-text);
  font-family: var(--font-heading);
  font-size: 40px;
  font-weight: 700;
  line-height: 0.95;
  letter-spacing: -0.02em;
  text-transform: uppercase;
}
.blogs-section .description {
  color: var(--color-text-dim);
  font-family: var(--font-body);
  font-size: 18px;
  font-weight: 400;
  line-height: 1.6;
  margin: 6px 0 0 0;
  max-width: 520px;
}
.blogs-section .meta-row {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 12px;
}
.blogs-section .stat {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  color: var(--color-text-dim);
  font-family: var(--font-mono);
  font-size: 12px;
  letter-spacing: 0.5px;
  padding: 6px 12px;
  text-transform: uppercase;
}
.blogs-section .stat-number {
  color: var(--color-text);
  font-weight: 600;
}
.blogs-section .controls {
  width: min(960px, 90%);
  margin-top: 20px;
  display: grid;
  grid-template-columns: 1fr 180px auto;
  gap: 12px;
  align-items: end;
}
.blogs-section .control-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.blogs-section .control-label {
  color: var(--color-text-dim);
  font-family: var(--font-mono);
  font-size: 12px;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}
.blogs-section .search-input,
.blogs-section .sort-select {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  color: var(--color-text);
  font-family: var(--font-body);
  font-size: 14px;
  padding: 10px 12px;
}
.blogs-section .search-input:focus,
.blogs-section .sort-select:focus {
  outline: 2px solid var(--color-accent);
  border-color: var(--color-accent);
}
.blogs-section .clear-btn {
  background: transparent;
  border: 1px solid var(--color-border);
  color: var(--color-text);
  cursor: pointer;
  font-family: var(--font-heading);
  font-size: 13px;
  letter-spacing: 0.4px;
  padding: 10px 14px;
  text-transform: uppercase;
  transition: background 0.15s ease, color 0.15s ease;
}
.blogs-section .clear-btn:hover {
  background: var(--color-text);
  color: var(--color-bg);
}
.blogs-section .tags-row {
  width: min(960px, 90%);
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 16px;
}
.blogs-section .tag-chip {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  color: var(--color-text);
  cursor: pointer;
  font-family: var(--font-heading);
  font-size: 12px;
  letter-spacing: 0.4px;
  padding: 6px 12px;
  text-transform: uppercase;
  transition: background 0.15s ease, color 0.15s ease, border-color 0.15s ease;
}
.blogs-section .tag-chip:hover {
  border-color: var(--color-accent);
  color: var(--color-accent);
}
.blogs-section .tag-chip.active {
  background: var(--color-accent);
  border-color: var(--color-accent);
  color: var(--color-text);
}
.blogs-section .tag-chip--small {
  font-size: 11px;
  padding: 4px 10px;
}
.blogs-section .empty-state {
  width: min(960px, 90%);
  margin-top: 24px;
  padding: 18px 20px;
  border: 1px dashed var(--color-border);
  background: var(--color-surface);
  color: var(--color-text-dim);
  font-family: var(--font-body);
  text-align: left;
}
.blogs-section .blog-list {
  width: min(960px, 90%);
}
.blogs-section .blog-card {
  margin-top: 30px;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  padding: 20px;
  transition: box-shadow 0.15s ease;
}
.blogs-section .blog-card:hover {
  box-shadow: 4px 4px 0 var(--color-border);
}
.blogs-section .blog-head {
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.blogs-section .blog-title {
  background: transparent;
  border: none;
  color: var(--color-text);
  cursor: pointer;
  font-family: var(--font-heading);
  font-size: 24px;
  font-weight: 700;
  letter-spacing: -0.02em;
  padding: 0;
  text-align: left;
  text-transform: uppercase;
}
.blogs-section .blog-title:hover {
  color: var(--color-accent);
}
.blogs-section .blog-meta {
  display: flex;
  align-items: center;
  gap: 8px;
  color: var(--color-text-dim);
  font-family: var(--font-mono);
  font-size: 13px;
  letter-spacing: 0.5px;
}
.blogs-section .meta-dot {
  width: 4px;
  height: 4px;
  background: var(--color-accent);
  display: inline-block;
}
.blogs-section .tag-line {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 12px;
}
.blogs-section .blog-description {
  font-size: 15px;
  font-family: var(--font-body);
  font-weight: 300;
  line-height: 1.6;
  text-align: left;
  color: var(--color-text-dim);
  margin-top: 14px;
}
.blogs-section .blog-description--preview {
  cursor: pointer;
}
.blogs-section .blog-description img {
  max-width: 100%;
  margin: 10px 0;
}
.blogs-section .blog-description pre {
  overflow-x: auto;
  padding: 10px 12px;
}
.blogs-section .blog-actions {
  display: flex;
  justify-content: flex-start;
  margin-top: 16px;
}
.blogs-section .ghost-btn {
  background: transparent;
  border: 1px solid var(--color-border);
  color: var(--color-text);
  cursor: pointer;
  font-family: var(--font-heading);
  font-size: 13px;
  letter-spacing: 0.4px;
  padding: 8px 14px;
  text-transform: uppercase;
  transition: background 0.15s ease, color 0.15s ease;
}
.blogs-section .ghost-btn:hover {
  background: var(--color-text);
  color: var(--color-bg);
}
@media (max-width: 768px) {
  .container {
    padding-top: 60px;
    overflow-y: visible;
  }
  .blogs-section {
    height: auto;
    min-height: calc(100vh - 60px);
  }
  .blogs-section .header {
    width: 92%;
  }
  .blogs-section .greetings {
    font-size: 30px;
    font-weight: 700;
  }
  .blogs-section .description {
    font-size: 15px;
    line-height: 1.6;
  }
  .blogs-section .controls {
    width: 92%;
    grid-template-columns: 1fr;
  }
  .blogs-section .tags-row,
  .blogs-section .blog-list,
  .blogs-section .empty-state {
    width: 92%;
  }
  .blogs-section .tag-chip {
    font-size: 11px;
  }
  .blogs-section .blog-title {
    font-size: 20px;
  }
  .blogs-section .blog-description {
    font-size: 14px;
    line-height: 1.6;
  }
}
</style>