<template>
  <!-- App.vue -->

  <v-app>
    <!-- 属于左侧边栏 -->
    <v-navigation-drawer app clipped>
      <MainLeftLists />
    </v-navigation-drawer>

    <!-- Sizes your content based upon application components -->
    <v-main>
      <!-- Provides the application the proper gutter -->
      <v-container fluid>
        <!-- If using vue-router -->
        <router-view></router-view>
      </v-container>
    </v-main>

    <v-footer app>
      <!-- -->
    </v-footer>
  </v-app>
</template>
<script>
import MainLeftLists from "./MainLeftLists.vue";
export default {
  components: {
    MainLeftLists,
  },
};
</script>
<style scoped>
</style>