<template>
  <v-app id="homePage">
    <div class="d-flex justify-content-center">
      <img src="./assets/kaamdev.png" id="homePageLogo" alt />
    </div>
    <div class="d-flex justify-content-center" id="searchBar">
        <v-text-field outlined  label="Search for help" append-icon="mdi-magnify" class="shrink"></v-text-field>
    </div>
    <div class="d-flex justify-content-center" id="searchButton">
        <v-btn small color="primary" large width="200">Search</v-btn>
    </div>
    <div class="d-flex justify-content-center" id="sposorButton">
        <v-btn small color="primary" large>Become a sponsor</v-btn>
    </div>
  </v-app>
</template>

<script>
export default {
  name: "App",

  components: {},

  data() {
    return {};
  }
};
</script>
