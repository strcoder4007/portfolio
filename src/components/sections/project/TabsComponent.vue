<template>
    <div class="project-tabs-page">
        <el-row>
            <div class="tab-card">
                <button id="show_all" class="tab active" @click="selectTab('show_all')">All</button>
                <button id="ml" class="tab" @click="selectTab('ml')">AI/ML</button>
                <button id="web_dev" class="tab" @click="selectTab('web_dev')">Web Apps</button>
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
    flex-wrap: wrap;

    margin: 20px 0;

    max-width: 500px;
    width: 90vw;
    gap: 10px;
    height: auto;
    min-height: 60px;
    padding: 10px;
    background-color: #111111;
    border-radius: 5px;
    box-shadow: 2px 2px 14px rgba(0, 0, 0, 0.3);

    .tab {
        background-color: #222222;
        border: none;
        min-width: 70px;
        padding: 8px 12px;
        gap: 10px;
        color: #ffffff;
        font-size: 14px;
        font-family: 'Space Grotesk', Brandon, sans-serif;
        cursor: pointer;
        border-radius: 3px;
    }

    .tab.active {
        border: 2px solid white;
    }
}
@media (max-width: 768px) {
    .tab-card {
        width: 95vw;
        max-width: 95vw;
        gap: 8px;
        padding: 8px 6px;

        .tab {
            min-width: 60px;
            padding: 6px 8px;
            font-size: 12px;
        }
    }
}
@media (max-width: 360px) {
    .tab-card {
        gap: 4px;
        .tab {
            min-width: 50px;
            padding: 5px 6px;
            font-size: 11px;
        }
    }
}
</style>