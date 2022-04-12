<template>
  <div id="app">
    <div id="mynetwork"></div>
  </div>
</template>

<script>
/* import { data } from 'vis-network'; */
const vis = require("vis-network");

export default {
  name: "GrafosMy",
  data() {
    return {
      nodes: [
        { id: 1, label: "Node 1" },
        { id: 2, label: "Node 2" },
        { id: 3, label: "Node 3" },
        { id: 4, label: "Node 4" },
      ],

      edges: [
        { from: 1, to: 3 },
        { from: 1, to: 2 },
        { from: 2, to: 4 },
      ],
      options: {
        manipulation: {
          enabled: false,
          initiallyActive: true,
          addEdge: function (edgeData, callback) {
            if (edgeData.from === edgeData.to) {
              var r = confirm("Do you want to connect the node to itself?");
              if (r === true) {
                callback(edgeData);
              }
            } else {
              callback(edgeData);
            }
          },
        },
        nodes: {
          physics: true,
        },
      },
      container: "",
      network: null,
    };
  },

  computed: {
    graph_data() {
      return {
        nodes: this.nodes,
        edges: this.edges,
      };
    },
  },

  mounted() {
    this.container = document.getElementById("mynetwork");

    this.network = new vis.Network(
      this.container,
      this.graph_data,
      this.options
    );
  },
};
</script>

<style>
#mynetwork {
  height: 500px;
  margin: 3px 0;
}
</style>
