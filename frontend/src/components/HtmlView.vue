<template>
  <div class="html-view">
    <button v-on:click="getNext">Get next</button>
    <div class="html-content">
      <p v-on:keyup.e="highlightSelection" v-html="content"></p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

import highlightSelection from "../Highlight";

let api_url = "http://127.0.0.1:5000/";

export default {
  name: "HtmlView",
  data() {
    return {
      content: null,
      id: null
    };
  },
  methods: {
    getNext: function() {
      axios
        .get(api_url)
        .then(response => {
          this.content = response.data.html_page;
          this.id = response.data.id;
        })
        .catch(err => console.log(err));
    },
    highlight: function() {
      highlightSelection();
    }
  },
  mounted() {
    this.getNext();
    window.addEventListener("keyup", event => {
      if (event.keyCode === 13) {
        this.highlight();
      }
    });
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
