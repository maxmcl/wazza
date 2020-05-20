<template>
  <div id="app">
      <HtmlView />
  </div>
</template>

<script>
import HtmlView from "./components/HtmlView.vue";

export default {
  name: "App",
  components: {
    HtmlView
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
