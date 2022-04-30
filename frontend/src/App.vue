<template>
  <div class="d-flex w-100 h-100 mx-auto flex-column">
    <HeaderVue></HeaderVue>
    <div class="space"></div>
    <div class="container py-5">
      <div class="row justify-content-md-center">
        <div id="mynetwork" class="col"></div>
      </div>
    </div>
  </div>
</template>

<script>
/* import { data } from 'vis-network'; */
import HeaderVue from "./components/HeaderVue.vue";
const vis = require("vis-network");

export default {
  name: "App",

  components: {
    HeaderVue,
  },
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
        locale: "es",
        height: "100%",
        width: "100%",
        manipulation: {
          enabled: true,
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
  methods: {
    addNode() {
      /* const id = new Date().getTime(); */
      console.log(this.network.nodes);
    },
    addEdge() {
      const n1 = Math.floor(Math.random() * this.network.nodes.length);
      const n2 = Math.floor(Math.random() * this.network.nodes.length);
      this.network.edges.push({
        id: `${this.network.nodes[n1].id}-${this.network.nodes[n2].id}`,
        from: this.network.nodes[n1].id,
        to: this.network.nodes[n2].id,
      });
    },
    resetNetwork() {
      this.network = {
        nodes: this.nodes.slice(0),
        edges: this.edges.slice(0),
        options: {},
      };
    },
    removeNode() {
      this.network.nodes.splice(0, 1);
    },
    removeEdge() {
      this.network.edges.splice(0, 1);
    },
  },
};
</script>

<style>
#mynetwork {
  height: 400px;
  border: 1px solid #000;
}
</style>
