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
    </div>
    <div class="d-flex justify-content-center" v-if="cardData.length==0">
      <h4>No results</h4>
    </div>
    <div class="d-flex justify-content-center" style="flex-wrap: wrap;" v-if="cardData.length!=0">
      
      <v-card
        width="344"
        style="padding-top:2% padding-bottom:2%"
        :key="individual"
        v-for="individual in cardData"
      >
        <v-card-text>
          <div>Professional</div>
          <p class="display-1 text--primary">{{individual.sponsor_individualname}}</p>
          <p>{{professions_dict[individual.sponsor_individualprofession]}}</p>
          <div class="d-flex">
            <div>
              <div class="text--primary">
                <b>Review:</b>
                {{individual.sponsor_individualreview}}
              </div>
              <div class="text--primary">
                <b>Sponsor Name:</b>
                {{individual.sponsor_name}}
                <br />
                <b>Sponsor Contact:</b>
                {{individual.sponsor_number}}
              </div>
            </div>
            <div class="ml-auto">
              <img :src="individual.sponsor_individualpicture" style="height:100px;" alt />
            </div>
          </div>
        </v-card-text>
        <v-card-actions>
          <a
            v-bind:href="'tel:'+ ''+ individual.sponsor_individualnumber+''"
            style="decoration: none;"
          >
            <v-btn text color="deep-purple accent-4">Call professional</v-btn>
          </a>
        </v-card-actions>
      </v-card>
    </div>
  </v-app>
</template>

<script>
import { mapGetters } from "vuex";
import axios from "axios";

export default {
  name: "searchPage",

  components: {},
  computed: mapGetters(["getsearchContent"]),
  data() {
    return {
      cardData: [],
      professions_dict: {
        "1": "House Help",
        "2": "Car Wash",
        "3": "Electrician"
      },
      reverser_dict:{
        "house help": "1", 
        "car wash":"2",
        "electrician":"3"
      }
    };
  },
  methods: {
    async updateContent() {
      let keyword = this.getsearchContent;
      if (keyword[0] == "5") {
        let data = await axios.get(
          `http://b3d4105f7736.ngrok.io/data?sponsor_individualaddress=${keyword.slice(0,6)}`
        );
        data = data.data;
        this.cardData = data;
      } else {
        let data = await axios.get(
          `http://b3d4105f7736.ngrok.io/data?sponsor_individualprofession=${this.reverser_dict[keyword.toLowerCase()]}`
        );
        data = data.data;
        this.cardData = data;
      }

      
    }
  },

  mounted() {
    this.updateContent();
    //will need to access the database here with whatever value the user entered in searchbar
  }
};
</script>
