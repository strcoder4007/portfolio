<template>
    <div class="links-section">
        <span class="header">Links</span>
        <span class="subheader">You can find my work here</span>
        <div class="social-section">
            <a href="https://www.behance.net/rinyyadav" target="_blank"><img src="../../assets/icons/behance-icon-colored.svg" alt="Behance Icon" class="social-icon" /></a>
            <a href="https://www.linkedin.com/in/riny-yadav-a24a90238/" target="_blank"><img src="../../assets/icons/linkedin-icon-colored.svg" alt="LinkedIn Icon" class="social-icon" /></a>
            <a href="" target="_blank"><img src="../../assets/icons/wix-icon-colored.svg" alt="Wix Icon" class="social-icon" /></a>
            <a href="https://dribbble.com/rinydesigns" target="_blank"><img src="../../assets/icons/dribble-icon-colored.svg" alt="Dribble Icon" class="social-icon" /></a>
            <a href="" target="_blank"><img src="../../assets/icons/pintrest-icon-colored.svg" alt="Pintrest Icon" class="social-icon" /></a>
        </div>
    </div>
</template>
<script>
    export default {
        name: "FooterSection",
    };
</script>
<style scoped>
.links-section {
    padding-top: 70px;
    padding-bottom: 30px;
    height: auto;
    min-height: 300px;
    width: 100vw;
    background: linear-gradient(180deg, #ffffff 0%, #FF745B 100%);
    backdrop-filter: blur(2px);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    border-top: 1px solid #261F221A;

    .header {
        color: var(--Black, #261F22);
        font-family: "Brandon";
        font-size: 59px;
        font-style: normal;
        font-weight: 330;
        line-height: 72px; /* 122.034% */
        letter-spacing: -1.77px;
    }

    .subheader {
        color: #000;
        font-family: 'Bricolage';
        font-size: 21px;
        font-style: normal;
        font-weight: 400;
        line-height: 30px;
    }
    
    .social-section {
        display: flex;
        justify-content: center;
        align-items: center;
        width: auto;
        min-width: 300px;
        margin: 50px 0;
        a {
            margin: 0 15px;
        }
        img {
            width: 50px;
            height: auto;
        }
    }
}
</style>