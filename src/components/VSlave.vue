<template>
  <div>
    <div class="container">
      <!-- Air Conditioning Info -->
      <b-card :title="'Room ' + roomId + ' Air Conditioning'" header-tag="header" bg-variant="light">
      <template v-slot:header>
        <h6 class="mb-0">Air Conditioning Panel</h6>
      </template>

      <b-button-toolbar size="sm">
        <b-button-group size="sm" class="mb-1" right>
          <b-button variant="outline-success" disabled>Temperature Now</b-button>
          <b-button :variant="this.slave.temp<25?'outline-info':'outline-danger'" disabled>{{ this.slave.temp }}</b-button>
        </b-button-group>
      </b-button-toolbar>

      <b-button :variant="this.slave.power ? 'outline-danger':'outline-info'" @click="flipPower" class="mb-2" size="sm">
        <b-icon icon="power" aria-hidden="true"></b-icon> {{ this.slave.power ? "Power Off":"Power On" }}
      </b-button>

      <b-button-toolbar size="sm" v-if="this.slave.power">
        <b-button-group size="sm" class="mb-1" right>
          <b-button variant="outline-success" disabled>Temperature Set</b-button>
          <b-button :variant="this.slave.expectTemp<25?'outline-info':'outline-danger'" disabled>{{ this.slave.expectTemp }}</b-button>
        </b-button-group>
        <b-button-group size="sm" class="mb-1 ml-1">
          <b-button variant="outline-primary" disabled>Speed</b-button>
          <b-button :variant="this.slave.speed=='High'?'outline-warning':'outline-success'" disabled>{{ this.slave.speed }}</b-button>
        </b-button-group>
      </b-button-toolbar>


      <b-button size="sm" v-b-toggle.setting_slave v-if="this.slave.power" variant="outline-secondary">
        <b-icon icon="gear-fill" aria-hidden="true"></b-icon> Settings
      </b-button>
      <b-collapse id="setting_slave" class="mt-2" v-if="this.slave.power">
      <b-button-toolbar size="sm">
        <b-button-group size="sm" right>
          <b-button :variant="mode=='Cold'?'outline-info':'outline-danger'" @click="temp_up"><b-icon icon="arrow-up"></b-icon></b-button>
          <b-button variant="outline-success" disabled>Temperature</b-button>
          <b-button :variant="mode=='Cold'?'outline-info':'outline-danger'" @click="temp_down"><b-icon icon="arrow-down"></b-icon></b-button>
        </b-button-group>

        <b-button-group size="sm" class="ml-1" right>
          <b-button :variant="mode=='Cold'?'outline-info':'outline-danger'" @click="speed_up"><b-icon icon="arrow-up"></b-icon></b-button>
          <b-button variant="outline-primary" disabled>Speed</b-button>
          <b-button :variant="mode=='Cold'?'outline-info':'outline-danger'" @click="speed_down"><b-icon icon="arrow-down"></b-icon></b-button>
        </b-button-group>
      </b-button-toolbar>
      </b-collapse>

    </b-card>
    <br>
    <!-- User info -->
    <b-card :title="'Hope you feel at home. Welcome ' + this.slave.name + '!'" header-tag="header" bg-variant="light">
      <template v-slot:header>
        <h6 class="mb-0">User Panel</h6>
      </template>
      <p>Your ID Card Number: {{ this.slave.idCard }}</p>
      <p>Your Check In Date: {{ this.slave.checkInDate }}</p>
      <p>Your Cost : {{ this.slave.cost }}</p>
    </b-card>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState, mapGetters } from 'vuex'

export default {
    computed:{
      ...mapGetters('slave',['slave','roomId']),
      ...mapState('center', ['mode']),
    },
    methods:{
      ...mapActions('slave',['flipPower', 'temp_add', 'set_speed']),
      temp_up(){
        if (this.mode == 'Cold') {
            if (this.slave.expectTemp == 25) return;
            return this.temp_add(1);
        }
        if (this.slave.expectTemp == 30) return;
        return this.temp_add(1);
      },
      temp_down(){
        if (this.mode == 'Cold') {
            if (this.slave.expectTemp == 18) return;
            return this.temp_add(-1);
        }
        if (this.slave.expectTemp == 25) return;
        return this.temp_add(-1);
      },
      speed_up(){
        if(this.slave.speed=='Low')return this.set_speed('Mid');
        if(this.slave.speed=='Mid')return this.set_speed('High');
      },
      speed_down(){
        if(this.slave.speed=='High')return this.set_speed('Mid');
        if(this.slave.speed=='Mid')return this.set_speed('Low');
      },
    },
}
</script>