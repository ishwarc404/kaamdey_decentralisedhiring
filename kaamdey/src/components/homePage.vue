<template>
  <v-app id="homePage">
    <div class="d-flex justify-content-center">
      <img src="../assets/kaamdey.png" id="homePageLogo" alt />
    </div>
    <div class="d-flex justify-content-center" id="searchBar">
      <v-text-field
        outlined
        v-model="searchContent"
        label="Search for help"
        append-icon="mdi-magnify"
        class="shrink"
      ></v-text-field>
    </div>
    <div class="d-flex justify-content-center" id="searchButton">
      <v-btn small color="primary" large width="200" to="search">Search</v-btn>
    </div>
    <div class="d-flex justify-content-center" id="sposorButton">
      <v-btn small color="primary" large to="sponsor">Become a sponsor!</v-btn>
    </div>
        <div class="d-flex justify-content-center" id="whatsaAppButton">
      <v-btn small color="green" large @click="whatsapp">
        <v-icon large color="white">mdi-whatsapp</v-icon>
        WhatsApp Service</v-btn>
    </div>
  </v-app>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "App",

  components: {},

  data() {
    return {
      searchContent: null,
    };
  },
  methods: {
    ...mapActions(["updatesearchContent"]),
    whatsapp: function () {   
          window.open("https://wa.me/14155238886", "_blank");    
      }
  },
  watch: {
    searchContent: function() {
      this.updatesearchContent(this.searchContent);
    },

  },
};
</script>
