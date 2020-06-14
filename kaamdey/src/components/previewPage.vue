<template>
  <v-app>
    <div class="d-flex justify-content-center" style="padding-top:2% padding-bottom:4%">
      <h1>Your search results</h1>
    </div>
    <div class="d-flex justify-content-center" style="flex-wrap: wrap;">
      <v-card
        class="mx-auto"
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
  name: "preview",

  components: {},
  computed: mapGetters(["getsearchContent"]),
  data() {
    return {
      cardData: [],
      professions_dict: {
        "1": "House Help",
        "2": "Car Wash",
        "3": "Electrician"
      }
    };
  },
  methods: {
    async loadData() {
      //will need to access the database here with whatever value the user entered in searchbar
      let url = window.location.href;
      let uuid = url.slice(url.indexOf("=") + 1);
      console.log("UUID is:", uuid);
      //now we need to get the data related to this from the database
      let datalaoded = await axios.get(
        `http://c8143a2e1248.ngrok.io/previewdata?uuid=${uuid}`
      );
      datalaoded = datalaoded.data[0];
      let uuidlist = datalaoded["uuidlist"];
      for (var i = 0; i < uuidlist.length; i++) {
        let individualdata = await axios.get(
          `http://c8143a2e1248.ngrok.io/data?uuid=${uuidlist[i]}`
        );
        this.cardData.push(individualdata.data[0]);
      }
    }
  },

  mounted() {
    this.loadData();
  }
};
</script>
