<template>
  <div>
    <v-nav />
    <div v-if="login_adminEmail==''" class="container">
      <h1>Admin Page</h1>
      <p>Please sign in for more information</p>
    </div>
    <div v-else>
      <br />
      <v-center admin="true" />
      <br />
      <b-overlay :show="loading" rounded="sm">
        <div class="container">
          <h1>Rooms:</h1>
          <b-table :items="rooms.data" :fields="fields" striped responsive="sm">
            <template v-slot:cell(show_details)="row">
              <b-button
                size="sm"
                @click="row.toggleDetails"
                class="mr-2"
              >{{ row.detailsShowing ? 'Hide' : 'Show'}} Details</b-button>
            </template>

            <template v-slot:row-details="details">
              <b-form>
                <b-form-group id="input-group-1" label="ID card number:" label-for="input-1">
                  <b-form-input
                    id="input-1"
                    v-model="details.item.idCard"
                    type="number"
                    required
                    placeholder="Enter ID card number"
                  ></b-form-input>
                </b-form-group>

                <b-form-group id="input-group-2" label="Name:" label-for="input-2">
                  <b-form-input
                    id="input-1"
                    v-model="details.item.name"
                    type="text"
                    required
                    placeholder="Enter name"
                  ></b-form-input>
                </b-form-group>

                <b-button-group>
                  <b-button @click="checkIn(details.item.id)" variant="primary">Check In</b-button>
                  <b-button @click="checkOut(details.item.id)" variant="danger">Check Out</b-button>
                </b-button-group>
              </b-form>
            </template>
          </b-table>
        </div>
      </b-overlay>
    </div>
  </div>
</template>

<script>
import VNav from "../components/VNav.vue";
import VCenter from "../components/VCenter.vue";
import Vuex from "vuex";

const mapState = Vuex.mapState;
const mapActions = Vuex.mapActions;

export default {
  data() {
    return {
      fields: [
        "id",
        "name",
        "checkInDate",
        "cost",
        "state",
        "expectSpeed",
        "expectTemp",
        "speed",
        "temp",
        "show_details"
      ]
    };
  },
  computed: {
    ...mapState("auth", ["login_adminEmail"]),
    ...mapState("rooms", ["rooms", "loading"])
  },
  methods: {
    ...mapActions("rooms", ["getRooms", "checkIn", "checkOut"])
  },
  components: {
    VCenter,
    VNav
  },
  created() {
    this.getRooms();
  }
};
</script>