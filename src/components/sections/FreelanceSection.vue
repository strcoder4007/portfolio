<template>
    <div class="freelance-section">
        <el-row>
            <el-col>
                <span class="title">I’m currently available for freelance work.</span>
                <span class="subtitle">If you’re looking for a designer and developer that likes to get stuff done, let’s talk.</span>
            </el-col>
        </el-row>
        <div class="contact-container">
            <el-button class="email-btn" @click="copyToClipboard('mynameshubham23@gmail.com', 'Email')">mynameshubham23@gmail.com</el-button>
            <el-button class="phone-btn" @click="copyToClipboard('+918126062707', 'Phone Number')">+(91) 8126062707</el-button>
        </div>
        <button class="connect" @click="sendMail()">Got a project in mind? Let’s talk!</button>
    </div>
</template>
<script>
    export default {
        name: "FreelanceSection",
        methods: {
            copyToClipboard(text, textType) {
                navigator.permissions.query({name: "clipboard-write"}).then(result => {
                    if (result.state == "granted" || result.state == "prompt") {
                        navigator.clipboard.writeText(text)
                            .then(() => this.$message({ message: textType + ' Copied', type: 'success'}))
                            .catch(() => console.log('failure'))
                    }
                });
            },
            sendMail() {
                let emailTo = 'mynameshubham23@gmail.com'
                let emailString = 'mailto:' + emailTo
                window.location.href = emailString
            }
        }
    };
</script>
<style scoped>
.freelance-section {
    height: auto;
    max-height: 600px;
    min-height: 300px;
    background: transparent;
    backdrop-filter: blur(2px);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: start;
    padding: 100px 20vw;
}
.title {
    display: block;
    color: var(--Black, #261F22);
    font-family: Brandon;
    font-size: 36px;
    font-style: normal;
    font-weight: 700;
    line-height: 48px;
    text-align: left;
    margin-bottom: 20px;
}
.subtitle {
    display: block;
    color: #ffffff;
    font-family: Bricolage;
    font-size: 18px;
    font-style: normal;
    font-weight: 400;
    line-height: 26px;
}
.contact-container {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    padding: 40px 0;

}
.email-btn {
    display: flex;
    width: 300px;
    padding: 32px;
    flex-direction: column;
    align-items: center;
    border: none;
    border-radius: 8px;
    background: var(--Accent, #FC3A79);
    color: #FFF;
    letter-spacing: 2px;

    font-family:'Courier New', Courier, monospace;
    font-size: 15px;
    font-style: normal;
    font-weight: 600;
    line-height: 24px;
}
.phone-btn {
    display: flex;
    width: 300px;
    padding: 32px;
    flex-direction: column;
    align-items: center;
    border: none;
    border-radius: 8px;
    background: #ffffff;
    color: #000;

    font-family: Brandon;
    font-size: 18px;
    font-style: normal;
    font-weight: 450;
    line-height: 24px;
}
.connect {
    color: #FFF;
    font-family: Bricolage;
    font-size: 18px;
    font-style: normal;
    font-weight: 600;
    line-height: 26px;

    display: flex;
    margin-top: 40px;
    margin-bottom: 100px;
    padding: 24px 48px;
    align-items: center;
    border-radius: 100px;
    border: none;
    background: #0c0f11 ;
    box-shadow: 0px 2.767px 2.214px 0px rgba(0, 0, 0, 0.02), 0px 6.65px 5.32px 0px rgba(0, 0, 0, 0.03), 0px 12.522px 10.017px 0px rgba(0, 0, 0, 0.04), 0px 22.336px 17.869px 0px rgba(0, 0, 0, 0.04);
}
@media (max-width: 768px) {
    .freelance-section {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 40px;
    }
    .title {
        font-size: 30px;
        line-height: 30px;
    }
    .subtitle {
        font-size: 15px;
        font-style: normal;
        font-weight: 400;
        line-height: 24px;
        text-align: left;
    }
    .contact-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 30px 0;
    }
    .email-btn {
        padding: 20px;
        margin-bottom: 20px;
    }
    .phone-btn {
        padding: 20px;
        margin: 0;
    }
    .connect {
        font-size: 15px;
        font-style: normal;
        font-weight: 600;
        line-height: 25px;

        margin-top: 20px;
        margin-bottom: 60px;
        padding: 12px 40px;
        align-items: center;
    }
}
</style>