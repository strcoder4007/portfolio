<template>
  <div class="container" id="intro-section">
    <div class="intro-section">
      <div class="intro-text">
        <div class="profile-block">
          <span class="role mono-meta">// role</span>
          <h1 class="role-title heading-display">Sr. AI<br>Engineer</h1>
        </div>
        <div class="contact-block">
          <a class="contact-link" @click="copyToClipboard('+918126062707', 'Phone Number')">
            (+91) 8126062707
            <span class="copy-hint">[`copy`]</span>
          </a>
          <a class="contact-link" @click="copyToClipboard('mynameshubham23@gmail.com', 'Email')">
            mynameshubham23@gmail.com
            <span class="copy-hint">[`copy`]</span>
          </a>
        </div>

        <section class="about">
          <p>
            I'm a Senior AI/ML Engineer with around seven years of hands-on experience — about two years deep into GenAI, agentic systems, RAG, and LLMs, and five years building and deploying ML systems.<br><br>Over the years, I've worked on projects across government, healthcare, education, and even cultural heritage — actually putting AI into production where it matters. Outside of work, I like to stay sharp with algorithms and problem-solving — I've solved over 800 problems on Codeforces.<br><br>Open to AI Engineering roles.
          </p>
        </section>

        <div class="cta-row">
          <a href="#/about" class="btn-angular btn-angular-ghost" @click.prevent="goToAbout">
            More details...
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
          </a>
          <a href="https://drive.google.com/file/d/1SIoPoYCGpk9E8U_VdmdZguvivdUEoZU6/view?usp=sharing"
             target="_blank" class="btn-angular">
            Resume
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
          </a>
        </div>

        <div class="social-section">
          <a href="https://www.linkedin.com/in/str4007" target="_blank" class="social-link" aria-label="LinkedIn">
            <svg class="social-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
              <path d="M20.45 20.45h-3.55v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.36V9h3.41v1.56h.05c.47-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zM7.12 20.45H3.56V9h3.56v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.72v20.56C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.72V1.72C24 .77 23.2 0 22.22 0z"/>
            </svg>
            <span>LinkedIn</span>
          </a>
          <a href="https://github.com/strcoder4007" target="_blank" class="social-link" aria-label="GitHub">
            <svg class="social-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
              <path d="M12 .3a12 12 0 0 0-3.79 23.39c.6.11.82-.26.82-.58 0-.29-.01-1.05-.02-2.06-3.34.73-4.04-1.61-4.04-1.61-.55-1.39-1.34-1.76-1.34-1.76-1.09-.74.08-.73.08-.73 1.21.08 1.84 1.24 1.84 1.24 1.07 1.84 2.81 1.31 3.5 1 .11-.78.42-1.31.76-1.61-2.66-.3-5.47-1.33-5.47-5.93 0-1.31.47-2.38 1.24-3.22-.13-.3-.54-1.52.11-3.18 0 0 1.01-.32 3.3 1.23a11.5 11.5 0 0 1 6 0c2.29-1.55 3.3-1.23 3.3-1.23.65 1.66.24 2.88.12 3.18.77.84 1.24 1.91 1.24 3.22 0 4.61-2.81 5.62-5.49 5.92.43.37.81 1.1.81 2.22 0 1.61-.01 2.9-.01 3.29 0 .32.22.7.83.58A12 12 0 0 0 12 .3z"/>
            </svg>
            <span>GitHub</span>
          </a>
        </div>

        <div class="footer">
          <span class="source-code">
            Built with Vue 3 —
            <a href="https://github.com/strcoder4007/portfolio" target="_blank">Code</a>
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  mounted() {
    setTimeout(() => {
      document
        .querySelectorAll("mark")
        .forEach((e) => (e.style.color = "black"));
    }, 2000);
  },
  methods: {
    copyToClipboard(text, textType) {
      navigator.permissions
        .query({ name: "clipboard-write" })
        .then((result) => {
          if (result.state == "granted" || result.state == "prompt") {
            navigator.clipboard
              .writeText(text)
              .then(() =>
                this.$message({
                  message: textType + " Copied",
                  type: "success",
                })
              )
              .catch(() => console.log("failure"));
          }
        });
    },
    scrollToWork() {
      document.getElementById("projects-section").scrollIntoView();
    },
    goToAbout() {
      this.$router.push({ name: "About" });
    },
    download() {
      const link = document.createElement("a");
      link.href = "https://strcoder4007.github.io/portfolio/resume.pdf";
      link.download = "Shubham_Resume.pdf";
      link.click();
    }
  },
};
</script>

<style lang="scss" scoped>
.container {
  background: transparent;
  height: 100%;
}

.intro-section {
  height: 100%;
  min-height: 600px;
  background: transparent;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 64px 48px;
  color: var(--color-text);
}

.intro-text {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.profile-block {
  margin-bottom: 32px;
}
.role {
  display: block;
  margin-bottom: 12px;
}

.role-title {
  padding-top: 30px;
  font-size: clamp(38px, 4.5vw, 62px);
  line-height: 0.9;
  color: var(--color-text);
  text-transform: uppercase;
}

.contact-block {
  display: flex;
  flex-direction: column;
  gap: 6px;
  margin-bottom: 36px;
}

.contact-link {
  font-family: var(--font-mono);
  font-size: 14px;
  color: var(--color-text);
  cursor: pointer;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  transition: color 0.15s ease;
}

.contact-link:hover {
  color: var(--color-text);
}

.copy-hint {
  color: var(--color-text-dim);
  font-size: 11px;
  opacity: 0;
  transition: opacity 0.15s ease;
}

.contact-link:hover .copy-hint {
  opacity: 1;
}

.about {
  max-width: 540px;
  margin-bottom: 40px;
  font-family: var(--font-body);
  font-size: 16px;
  line-height: 1.7;
  color: var(--color-text-dim);
}

.about p {
  margin: 0 0 12px 0;
}

.cta-row {
  display: flex;
  flex-wrap: nowrap;
  gap: 12px;
  margin-bottom: 40px;
}

@media (max-width: 480px) {
  .cta-row {
    flex-wrap: wrap;
  }
}

.social-section {
  display: flex;
  gap: 20px;
  margin-bottom: 48px;
}

.social-link {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-family: var(--font-heading);
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  color: var(--color-text-dim);
  text-decoration: none;
  transition: color 0.15s ease;
}

.social-icon {
  width: 20px;
  height: 20px;
  flex-shrink: 0;
}

.footer {
  margin-top: auto;
  padding-top: 32px;
  border-top: 1px solid var(--color-border);
}

.source-code {
  font-family: var(--font-mono);
  font-size: 12px;
  color: var(--color-text-dim);
}

.source-code a {
  color: var(--color-text);
  text-decoration: none;
}

.source-code a:hover {
  text-decoration: underline;
}

@media (max-width: 900px) {
  .intro-section {
    padding: 48px 32px;
  }
  .role-title {
    font-size: clamp(28px, 5vw, 44px);
  }
}

@media (max-width: 768px) and (max-height: 700px) {
  .intro-section {
    justify-content: flex-start;
    padding: 32px 24px;
  }
  .role-title {
    font-size: 26px;
  }
  .about {
    font-size: 14px;
    line-height: 1.6;
    margin-bottom: 24px;
  }
  .cta-row {
    flex-wrap: wrap;
  }
}
</style>