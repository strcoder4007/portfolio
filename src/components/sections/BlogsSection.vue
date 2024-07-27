<template>
  <div class="container" id="blogs-section">
    <el-row>
      <el-col class="blogs-section">
        <div class="greetings">Blogs</div>

        <div class="blog-card" v-for="(blog, idx) in localBlogs" :key="blog.title">
          <div  @click="toggleBlog(idx)" class="blog-name">{{ blog.title }}</div>
          <div  @click="toggleBlog(idx)" class="blog-date">{{ blog.time }}</div>
          <div v-if="showBlogArray[idx]" class="blog-description" v-html="blog.content"></div>
          <div v-else @click="toggleBlog(idx)" class="blog-description" v-html="blog.content.substring(0, 150) + '...'"></div>
        </div>

        <br>

      </el-col>
    </el-row>
  </div>
</template>

<script>
import { ref } from 'vue'
import data from '../../assets/blogs/blogs.json'

const blogs = ref(data)

const months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
      ]

export default {
  name: "BlogsSection",
  data() {
    return {
      localBlogs: this.formatBlog(blogs.value),
      showBlogArray: []
    }
  },
  mounted() {
    document.getElementById("blogs-section").scrollIntoView()
    this.showBlogArray = this.localBlogs.map(() => false)
  },
  methods: {
    getMonthIndex(monthName) {
      return months.indexOf(monthName);
    },
    formatBlog(allBlogs) {

      allBlogs = allBlogs.filter(blog => !blog.tags.includes('personal'))
      // Sort blogs by the given date string in the format "day month year"
      allBlogs.sort((a, b) => {
        let dateA = a.time.split(' ')
        let dateB = b.time.split(' ')

        // Convert month names to their indices
        let monthIndexA = this.getMonthIndex(dateA[1])
        let monthIndexB = this.getMonthIndex(dateB[1])

        // Compare years, then months, then days
        if (dateA[2] !== dateB[2]) return parseInt(dateA[2]) - parseInt(dateB[2])
        if (monthIndexA !== monthIndexB) return monthIndexA - monthIndexB
        return parseInt(dateA[0]) - parseInt(dateB[0])
      })
      return allBlogs.reverse()
    },
    toggleBlog(idx) {
      let blogState = this.showBlogArray[idx]
      this.showBlogArray = this.showBlogArray.map(() => false)
      this.showBlogArray[idx] = !blogState
    }
  },  
  components: {
  },
};
</script>

<style lang="scss" scoped>

.container {
  background: #222222;
  overflow-y: scroll;
}
.blogs-section {
  overflow-y: scroll;
  height: calc(100vh - 80px);
  background: transparent;
  backdrop-filter: blur(2px);
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;

  .greetings {
    margin-top: 20px;
    color: #fff;
    font-family: Bricolage;
    font-size: 40px;
    font-style: normal;
    font-weight: 600;
    line-height: 72px;
    letter-spacing: -1px;
  }

  .description {
    color: #fff;
    text-align: center;
    font-family: Bricolage;
    font-size: 21px;
    font-style: normal;
    font-weight: 400;
    line-height: 30px;
    margin-top: 20px;
  }
  .blog-card {
    margin-top: 30px;
    width: 80%;
    background: #111;
    border-radius: 5px;
    padding: 20px;
    cursor: pointer;
    box-shadow: 2px 2px 14px rgba(0, 0, 0, 0.3);

    .blog-name {
      font-size: 24px;
      font-weight: 700;
      text-align: left;
      font-family: Ubuntu, Bricolage;
      color: #fff;
    }

    .blog-date {
      margin-top: 5px;
      font-size: 14px;
      font-weight: 400;
      text-align: left;
      font-family: Ubuntu, Bricolage;
      color: #fff;
    }

    .blog-description {
      font-size: 15px;
      font-family: Bricolage;
      font-weight: 300;
      line-height: 22px;
      text-align: left;
      color: #fff;
      overflow-x: clip;
    }
  }
}
@media (max-width: 768px) {
  .container {
    padding-top: 60px;
    .blogs-section {
      height: auto;
      min-height: calc(100vh - 60px);
      .greetings {
        margin-top: 20px;
        font-size: 30px;
        font-weight: 700;
      }

      .description {
        padding: 0 20px;
        font-size: 15px;
        line-height: 20px;
      }
    }
  }
}
</style>