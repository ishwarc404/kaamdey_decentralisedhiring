<template>
  <v-app id="homePage">
    <div class="d-flex justify-content-center" style="padding-top:3%;">
      <div>
        <h4 style="padding-left:15%;">Please fill the below form</h4>
        <br />
        <div class="d-flex justify-content-center">
          <h5 style="padding-top:4%;">Your Name:</h5>
          <v-text-field outlined v-model="sponsor_data.sponsor_name" label="Name" class="shrink"></v-text-field>
        </div>
        <div class="d-flex justify-content-center">
          <h5 style="padding-top:4%;">Your Address:</h5>
          <v-text-field
            outlined
            v-model="sponsor_data.sponsor_address"
            label="ZIP Code"
            class="shrink"
          ></v-text-field>
        </div>
        <div class="d-flex justify-content-center">
          <h5 style="padding-top:4%;">Your Number:</h5>
          <v-text-field
            outlined
            v-model="sponsor_data.sponsor_number"
            label="Contact number"
            class="shrink"
          ></v-text-field>
        </div>
        <hr />
        <h5 style="padding-left:25%;">Professional's details</h5>
        <div class="d-flex justify-content-center">
          <h5 style="padding-top:4%;">Name:</h5>
          <v-text-field
            outlined
            v-model="sponsor_data.sponsor_individualname"
            label="Name"
            class="shrink"
          ></v-text-field>
        </div>
        <div class="d-flex justify-content-center">
          <h5 style="padding-top:4%;">Profession:</h5>
          <v-text-field
            outlined
            v-model="sponsor_data.sponsor_individualprofession"
            label="Profession"
            class="shrink"
          ></v-text-field>
        </div>
        <div class="d-flex justify-content-center">
          <h5 style="padding-top:4%;">Address:</h5>
          <v-text-field
            outlined
            v-model="sponsor_data.sponsor_individualaddress"
            label="Address"
            class="shrink"
          ></v-text-field>
        </div>
        <div class="d-flex justify-content-center">
          <h5 style="padding-top:4%;">Number:</h5>
          <v-text-field
            outlined
            v-model="sponsor_data.sponsor_individualnumber"
            label="Number"
            class="shrink"
          ></v-text-field>
        </div>
        <div class="d-flex justify-content-center">
          <h5 style="padding-top:4%;">Wages:</h5>
          <v-text-field
            outlined
            v-model="sponsor_data.sponsor_individualwages"
            label="Wages"
            class="shrink"
          ></v-text-field>
        </div>
        <div class="d-flex justify-content-center">
          <h5 style="padding-top:4%;">Review:</h5>
          <v-text-field
            outlined
            v-model="sponsor_data.sponsor_individualreview"
            label="Review"
            class="shrink"
          ></v-text-field>
        </div>
        <div class="d-flex justify-content-center">
          <h5 style="padding-top:4%;">Picture:</h5>
          <v-file-input label="File input" filled prepend-icon="mdi-camera"></v-file-input>
        </div>
        <div class="d-flex justify-content-center" id="searchButton">
          <v-btn color="primary" large @click="submitData">Submit</v-btn>
          <v-btn small large to="/home">Return Home</v-btn>
        </div>
      </div>
    </div>
  </v-app>
</template>

<script>
import axios from "axios";

export default {
  name: "App",

  components: {},

  data() {
    return {
      sponsor_data: {
        sponsor_name: null,
        sponsor_address: null,
        sponsor_number: null,
        sponsor_individualname: null,
        sponsor_individualprofession: null,
        sponsor_individualaddress: null,
        sponsor_individualnumber: null,
        sponsor_individualwages: null,
        sponsor_individualreview: null,
        sponsor_individualpicture: null,
        uuid: null
      }
    };
  },
  methods: {
    async submitData() {
      await axios.post("http://c8143a2e1248.ngrok.io/data", this.sponsor_data);
      alert("done");
    }
  },
  watch: {}
};
</script>
