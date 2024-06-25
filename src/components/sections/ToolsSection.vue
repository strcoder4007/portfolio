<template>
    <div class="tools-section">
        <span class="title">Tools I use</span>
        <el-row class="container">
            <el-col :xs="12" :md="6" class="tool-container">
                <div class="tool">
                    <img src="../../assets/tools/figma.png" alt="Figma" class="tool-icon" />
                    <span>Figma</span>
                </div>
            </el-col>
            <el-col :xs="12" :md="6" class="tool-container">
                <div class="tool">
                    <img src="../../assets/tools/photoshop.png" alt="Adobe Photoshop" class="tool-icon" />
                    <span>Adobe Photoshop</span>
                </div>
            </el-col>
            <el-col :xs="12" :md="6" class="tool-container">
                <div class="tool">
                    <img src="../../assets/tools/illustrator.png" alt="Adobe Illustrator" class="tool-icon" />
                    <span>Adobe Illustrator</span>
                </div>
            </el-col>
            <el-col :xs="12" :md="6" class="tool-container">
                <div class="tool">
                    <img src="../../assets/tools/firefly.png" alt="Adobe Firefly" class="tool-icon" />
                    <span>Adobe Firefly</span>
                </div>
            </el-col>
            <el-col hidden-md-only :md="4"></el-col>
            <el-col :xs="12" :md="8" class="tool-container">
                <div class="tool">
                    <img src="../../assets/tools/chatgpt.png" alt="ChatGPT DallE" class="tool-icon" />
                    <span>ChatGPT/Dall E</span>
                </div>
            </el-col>
            <el-col :xs="12" :md="8" class="tool-container">
                <div class="tool">
                    <img src="../../assets/tools/midjourney.png" alt="Midjourney" class="tool-icon" />
                    <span>Midjourney</span>
                </div>
            </el-col>
        </el-row>
    </div>
</template>
<script>
    export default {
        name: "ToolsSection",
        methods: {}
    };
</script>
<style scoped>
.tools-section {
    height: auto;
    max-height: 1200px;
    min-height: 200px;
    background: transparent;
    backdrop-filter: blur(2px);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: start;
    margin: 10px 150px 20px 150px;
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
    .container {
        width: 100%;
        padding-top: 20px;
        .tool-container {
            display: flex;
            justify-content: center;
            align-items: center;
            .tool {
                background: linear-gradient(180deg, #ffffff 0%, #FF7262 100%);
                height: 100px;
                width: 65%;
                box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
                border-radius: 10px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                align-self: center;
                padding: 20px;
                margin-bottom: 60px;
                img {
                    width: auto;
                    height: 30px;
                    object-fit: contain;
                    margin-bottom: 10px;
                }
                span {
                    font-weight: 600;
                }
            }
        }

    }

}

@media (max-width: 768px) {
    .tools-section {
        margin: 60px 30px 50px 30px;
        min-height: 100px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: baseline;
        .title {
            font-size: 30px;
            line-height: 30px;
        }
    }
}
</style>