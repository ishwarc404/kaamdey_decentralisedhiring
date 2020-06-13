<template>
  <v-app id="searchResults">
    <div class="d-flex justify-content-center">
      <img src="../assets/kaamdey.png" id="searchPageLogo" alt />
    </div>
      <div class="d-flex justify-content-center" id="returnHomeButton">
        <v-btn small large to="/home">Return Home</v-btn>
    </div>
    <div class="d-flex justify-content-center" id="resultsHeader">
      <p>Search Results</p>
      {{getsearchContent}}
    </div>
  </v-app>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "searchPage",

  components: {},
 computed: mapGetters(["getsearchContent"]),
  data() {
    return {

    };
  },

  mounted(){
  //will need to access the database here with whatever value the user entered in searchbar
  }
};
</script>
