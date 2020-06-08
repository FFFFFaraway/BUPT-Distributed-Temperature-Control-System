<template>
  <div>
    <router-view></router-view>
  </div>
</template>
<script>
export default {
  name: "App",
  sockets: {
    connect() {
      console.log("connect");
    },
    disconnect() {
      console.log("disconnect");
    },
    message(message) {
      console.log(message);
    },
    ping() {
      console.log("keep alive");
    }
  },
  mounted() {
    this.$socket.client.emit("update_rooms");
  }
};
</script>

<style></style>
