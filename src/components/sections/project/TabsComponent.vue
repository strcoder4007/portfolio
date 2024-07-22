<template>
    <div class="project-tabs-page">
        <el-row>
            <div class="tab-card">
                <button id="show_all" class="tab active" @click="selectTab('show_all')">Show all</button>
                <button id="ml" class="tab" @click="selectTab('ml')">ML</button>
                <button id="web_dev" class="tab" @click="selectTab('web_dev')">Web Dev</button>
                <button id="algo" class="tab" @click="selectTab('algo')">Algorithms</button>
            </div>
        </el-row>
    </div>
</template>

<script>
export default {
    name: "ProjectTabsPage",

    setup() {

    },
    data() {
        return {
            activeTab: 'show_all'
        }
    },
    mounted() {
        
    },
    methods: {
        removeAllActiveClasses() {
            let tabs = ['show_all', 'ml', 'web_dev', 'algo']
            for (let i in tabs) {
                let tab = tabs[i]
                let btn = document.getElementById(tab)
                btn.classList.remove('active')
            }
        },
        selectTab(tab) {
            this.removeAllActiveClasses()
            this.activeTab = tab
            var btn = document.getElementById(tab)
            btn.classList.add('active')

            this.$emit('tabChange', this.activeTab)
        }
    },
    components: {

    },
};
</script>

<style lang="scss" scoped>

.tab-card {
    display: flex;
    justify-content: center;
    align-items: center;

    margin: 20px 0;

    width: 500px;
    gap: 20px;
    height: 60px;
    background-color: #111111;
    border-radius: 5px;
    box-shadow: 2px 2px 14px rgba(0, 0, 0, 0.3);

    .tab {
        background-color: #222222;
        border: none;
        width: 90px;
        padding: 5px 10px;
        gap: 10px;
        color: #ffffff;
        font-size: 14px;
        font-family: Ubuntu, Brandon, sans-serif;
    }

    .tab.active {
        border: 2px solid white;
    }
}
@media (max-width: 768px) {

}
</style>