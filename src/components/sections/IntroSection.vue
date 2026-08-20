<template>
  <div class="container" id="intro-section">
    <div class="intro-section">
      <div class="intro-text">
        <div class="profile-block">
          <span class="role mono-meta">// role</span>
          <h1 class="role-title heading-display">Sr. AI/ML<br>Engineer</h1>
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
          <a href="https://drive.google.com/file/d/1SIoPoYCGpk9E8U_VdmdZguvivdUEoZU6/view?usp=sharing"
             target="_blank" class="btn-angular">
            Resume
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
          </a>
          <a href="#" class="btn-angular btn-angular-ghost" @click.prevent="openCalendly">
            Schedule time
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
          </a>
        </div>

        <div class="social-section">
          <a href="https://www.linkedin.com/in/str4007" target="_blank" class="social-link">LinkedIn</a>
          <a href="https://github.com/strcoder4007" target="_blank" class="social-link">GitHub</a>
        </div>

        <div class="footer">
          <span class="source-code">
            Built with Vue 3 —
            <a href="https://github.com/strcoder4007/portfolio" target="_blank">Code</a>
            © 2026 Shubham Singh. All rights reserved.
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
    download() {
      const link = document.createElement("a");
      link.href = "https://strcoder4007.github.io/portfolio/resume.pdf";
      link.download = "Shubham_Resume.pdf";
      link.click();
    },
    openCalendly() {
      const url = 'https://calendly.com/mynameshubham23/discussion?hide_event_type_details=1&hide_gdpr_banner=1'
      if (window.Calendly && typeof window.Calendly.initPopupWidget === 'function') {
        window.Calendly.initPopupWidget({ url });
      } else {
        window.open(url, '_blank');
      }
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
  font-family: var(--font-heading);
  font-size: clamp(36px, 4.5vw, 60px);
  font-weight: 700;
  letter-spacing: -0.03em;
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
  color: var(--color-text-dim);
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
  color: var(--color-accent);
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
  flex-wrap: wrap;
  gap: 14px;
  margin-bottom: 40px;
}

.social-section {
  display: flex;
  gap: 20px;
  margin-bottom: 48px;
}

.social-link {
  font-family: var(--font-heading);
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  color: var(--color-text-dim);
  text-decoration: none;
  transition: color 0.15s ease;
}

.social-link:hover {
  color: var(--color-text);
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
  color: var(--color-accent);
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