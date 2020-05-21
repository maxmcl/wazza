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

import { highlightSelection } from "../Highlight";

let api_url = "http://127.0.0.1:5000";

function getContent() {
  return document
    .getElementsByClassName("html-content")[0]
    .getElementsByTagName("p")[0].innerHTML;
}

export default {
  name: "HtmlView",
  data() {
    return {
      content: null,
      id: null,
      content_history: []
    };
  },
  methods: {
    getNext: function() {
      if (this.isHistoryChanged()) {
        this.send(
          this.id,
          this.content_history[this.content_history.length - 1]
        );
      }
      this.getNextData();
    },
    send: function() {
      axios
        .post(api_url + "/post")
        .then(response => console.log(response))
        .catch(err => console.log(err));
    },
    getNextData: function() {
      axios
        .get(api_url + "/get")
        .then(response => {
          this.content = response.data.html_page;
          this.id = response.data.id;
          this.content_history = [this.content];
        })
        .catch(err => console.log(err));
    },
    isHistoryChanged: function() {
      return this.content_history.length > 1;
    },
    undoChange: function() {
      if (this.isHistoryChanged()) {
        console.log("Reverting to previous change");
        console.log(this.content_history.length);
        this.content_history.pop();
        console.log(this.content_history.length);
        this.content = this.content_history[this.content_history.length - 1];
      }
    }
  },
  mounted() {
    window.addEventListener("keyup", event => {
      if (event.keyCode === 13) {
        highlightSelection();
        let content = getContent();
        this.content = content;
        this.content_history.push(content);
      } else if (event.keyCode === 78) {
        this.getNext();
      } else if (event.keyCode === 90) {
        this.undoChange();
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
