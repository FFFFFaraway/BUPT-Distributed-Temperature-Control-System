<template>
  <div>
    <v-nav/>
    <br>
    <div v-if="login_roomId==''" class="container">
        <h1>Room</h1>
        <p>Please sign in for more information</p>
    </div>
    <div v-else>
      <v-center admin="false"/>
      <br>
      <v-slave/>
    </div>
  </div>
</template>

<script>
import VNav from '../components/VNav.vue'
import VSlave from '../components/VSlave.vue'
import VCenter from '../components/VCenter.vue'
import { mapState } from 'vuex'

export default {
  computed:{
    ...mapState('auth',['login_roomId'])
  },
  components:{
      VNav,
      VCenter,
      VSlave,
  }
}
</script>