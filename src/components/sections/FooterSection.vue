<template>
    <el-row class="footer-section">
        <el-col :span="12" class="policy-and-terms-section">
            © 2024 Shubham Singh. All rights reserved.
        </el-col>
    </el-row>
</template>
<script>
    export default {
        name: "FooterSection",
    };
</script>
<style scoped>
.footer-section {
    width: 100%;
    height: 50px;
    background: transparent;
    backdrop-filter: blur(2px);
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    align-self: center;
    border-top: 1px solid #261F221A;
}
.policy-and-terms-section {
    cursor: pointer;
    color: #ffffff;
    font-family: "Brandon";
    font-size: 16px;
    font-style: normal;
    font-weight: 500;
    line-height: 50px;
}
.social-section {
    a {
        margin: 0 10px;
    }
    img {
        width: auto;
        height: 20px;
    }
    .dribble-icon {
        height: 25px !important;
        margin-bottom: -4px;
    }
}
@media (max-width: 768px) {
    .footer-section {
        max-height: 250px;
        display: flex;
        flex-direction: column-reverse;
        justify-content: center;
        align-items: center;
        align-self: center;
    }
    .policy-and-terms-section {
        line-height: 20px;
        margin-bottom: 20px;
    }
    .social-section {
        margin-top: 20px;
        margin-bottom: 20px;
        a {
            margin: 0 10px;
        }
        img {
            width: auto;
            height: 20px;
        }
        .dribble-icon {
            height: 25px !important;
            margin-bottom: -4px;
        }
    }
}
</style>