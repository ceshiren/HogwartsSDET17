<template>
    <v-list rounded>
      <v-subheader>REPORTS</v-subheader>
      <v-list-item-group v-model="selectedItem" color="primary">
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          @click="click_button(item)"
        >
          <v-list-item-icon>
            <v-icon v-text="item.icon"></v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title v-text="item.text"></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>
    </v-list>
</template>

<script>
export default {
  data: () => ({
    selectedItem: 0,
    items: [
      { text: "测试用例", icon: "mdi-clock", router: "TestCase" },
      { text: "测试任务", icon: "mdi-account" },
      { text: "测试报告", icon: "mdi-flag", router: "TestReport" },
    ],
  }),
  methods: {
    click_button(item) {
      this.$router.push({ name: item.router });
    },
  },
};
</script>