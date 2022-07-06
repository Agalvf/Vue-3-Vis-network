<script lang="ts">
import { defineComponent } from "vue";
import { IdType, network, Network } from "vis-network";
import { DataSet } from "vis-data";
import "https://unpkg.com/vis-network/standalone/umd/vis-network.min.js";
import "https://unpkg.com/default-passive-events";
import axios from "axios";
import * as XLSX from 'xlsx/xlsx.mjs';

import { jsPDF } from "jspdf";

export default defineComponent({
  name: "App",
  data() {
    return {
      nodes: DataSet.prototype,
      edges: DataSet.prototype,
      container: HTMLElement.prototype,
      network: Network.prototype,
      mostrarModal: false,
      origenArista: 0,
      destinoArista: 0,
      pesoArista: "0",
      mostrarMensaje: "",
      usarBoton: false,
      nodosStr: "",
      aristaEliminar: "",
      idEdges: 0,
      eventos: [],
      esDirigido: false,
      matriz: [] as number[][],
      vista: true,
      options: {
        locale: "es",
        height: "100%",
        width: "100%",
        manipulation: {
          enabled: false,
          initiallyActive: true,
        },
        nodes: {
          physics: false,
        },
        interaction: {
          multiselect: true,
          selectConnectedEdges: false,
        },
      },
    };
  },

  computed: {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    graph_data(): any {
      this.nodes.add([
        { id: 0, label: "Node 0" },
        { id: 1, label: "Node 1" },
        { id: 2, label: "Node 2" },
        { id: 3, label: "Node 3" },
      ]);

      this.edges.add([
        { id: 0, from: 0, to: 2, label: "" + Math.floor(Math.random() * (12 - 1) + 3) },
        { id: 1, from: 0, to: 1, label: "" + Math.floor(Math.random() * (12 - 1) + 3) },
        { id: 2, from: 1, to: 3, label: "" + Math.floor(Math.random() * (12 - 1) + 3) },
      ]);

      return {
        nodes: this.nodes,
        edges: this.edges,
      };

    },

    verificar(): boolean {

      if (
        this.origenArista < 0 ||
        this.origenArista > this.nodes.length ||
        this.destinoArista < 0 ||
        this.destinoArista > this.nodes.length
      ) {
        return true;
      } else {
        return false;
      }
    },
  },

  beforeMount() {
    this.nodes = new DataSet();
    this.edges = new DataSet();
    this.convertirMatriz();
    window.addEventListener("touchmove", function (event) { event.preventDefault(); }, { passive: false });
  },

  mounted() {
    this.container = document.getElementById("mynetwork") as HTMLInputElement;
    this.network = new Network(this.container, this.graph_data, this.options);
    this.convertirMatriz();
  },

  methods: {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    seleccionarNodos(nodes: { update: (arg0: { id: IdType; color: string; }) => void; }, edges, network) {
      this.network.on('selectNode', function (this: Network, params) {
        this.getSelectedNodes().forEach(function (nodo) {
          nodes.update({ id: nodo, color: '#ff0000' });
          network.getConnectedEdges(nodo).forEach(function (edge) {
            edges.update({ id: edge, color: '#ff0000' });
          });
        });
        /* this.getSelectedNodes().forEach(function (node: IdType) {
          nodes.update({ id: node, color: '#ff0000' });
        }); */
      });
    },

    algoritmoKrager() {
      const lista = {}
      let alphabet = 'abcdefghijklmnopqrstuvwxyz';

      this.nodes.get().forEach(function (nodes) {
        lista[alphabet[nodes.id]] = {}
      })

      this.edges.get().forEach(function (edges) {
        lista[alphabet[edges.from]][alphabet[edges.to]] = 1
        lista[alphabet[edges.to]][alphabet[edges.from]] = 1

      })
      axios.post("http://localhost:5000/karger_mincut", { lista })
        .then((response) => {
          this.mostrarMensaje = "Se ha encontrado una solución optima de " + response.data.mincut_num + " arista(s)" + "  - tiempo de ejecución: " + response.data.time + " milisegundos";
          for (let [key, value] of response.data.mincut_edges) {
            this.edges.get().forEach(function (this: DataSet, edges: { from: number; to: number; id: number; }) {
              if (edges.from == alphabet.indexOf(key) && edges.to == alphabet.indexOf(value)
                || edges.from == alphabet.indexOf(value) && edges.to == alphabet.indexOf(key)) {
                this.edges.update({ id: edges.id, color: '#ff0000' });
              }
            }.bind(this))
          }
        })
        .catch(() => {
          this.mostrarMensaje = "No se ha encontrado una solución optima";
          this.usarBoton = false;
        });
    },

    algoritmoStoerWagner() {
      const lista = [] as number[];
      this.edges.get().forEach(function (edges) {
        lista.push([edges.from, edges.to, parseInt(edges.label)]);
      }.bind(this))

      axios.post("http://localhost:5000/stoer-wagner", { lista })
        .then((response) => {
          this.mostrarMensaje = "Se ha encontrado una solución optima de " + response.data.mincut_num + " arista(s)" + "  - tiempo de ejecución: " + response.data.time + " milisegundos";
          console.log(response.data.mincut_edges)
          console.log(response.data.partition[0])
          this.obtenerAristasAdyacentes(response.data.partition[0])
        })

    },

    añadirNodo() {
      this.mostrarMensaje = "Haz click sobre el grafo para agregar un nodo";
      this.network.once("click", function (params) {
        this.body.data.nodes.add({
          id: this.body.data.nodes.length,
          label: `Node ${this.body.data.nodes.length}`,
          x: params.pointer.canvas.x,
          y: params.pointer.canvas.y,
        });
      });
    },

    añadirArista() {
      if (this.destinoArista != null || this.origenArista != null) {
        if (this.esDirigido == true) {
          this.edges.add({
            from: this.origenArista,
            to: this.destinoArista,
            label: this.pesoArista,
            arrows: "to",
          });
        } else {
          this.edges.add({
            from: this.origenArista,
            to: this.destinoArista,
            label: this.pesoArista,
          });
        }
      }
    },


    eliminarNodo() {
      this.mostrarMensaje = "Haz click sobre el nodo que deseas eliminar";
      this.network.once("click", function (this: Network, params) {
        this.body.data.edges.remove(this.getConnectedEdges(params.nodes[0]));
        this.body.data.nodes.remove(params.nodes[0]);
      });
    },


    eliminarArista(edges: { remove: (arg0: IdType) => void }) {
      this.mostrarMensaje = "Seleccione una arista para eliminarla";
      this.network.once("selectEdge", function (this: Network, params) {
        edges.remove(this.getEdgeAt(params.pointer.DOM) as IdType);
      });
    },

    crearVacio() {
      this.nodes.clear();
      this.edges.clear();
      this.idEdges = 0;
      this.matriz = [];
      this.vista = true;
    },

    grafoAleatorio() {
      this.nodes.clear();
      this.edges.clear();
      const numeroNodos = Math.floor(Math.random() * (12 - 1) + 3);
      const nodes = Array(numeroNodos)
        .fill(1)
        .map((_, i) => {
          return { id: i, label: `Node ${i}` };
        });

      var arr = [];

      for (var id = 0; id < numeroNodos; id++) {
        arr.push({
          id: id,
          from: id,
          to: function () {
            var random = Math.floor(Math.random() * (numeroNodos - 1));
            if (random == id) {
              random = random + 1;
            }
            return random;
          }(),
          label: `${Math.floor(Math.random() * (15 - 1) + 1)}`,
        });
      }

      this.nodes.add(nodes);
      this.edges.add(arr);

      this.network = new Network(
        this.container,
        { edges: this.edges, nodes: this.nodes },
        this.options
      );
      this.convertirMatriz();
    },

    imprimirCanvas() {
      var canvas = document.querySelector(
        "#mynetwork canvas"
      ) as HTMLCanvasElement;
      var png = canvas.toDataURL("image/png");
      var windowContent = '<img src="' + png + '">}';

      var printWin =
        window.open("", "", "width=800,height=800,scrollbars=yes") ?? window;
      printWin.document.write(windowContent);
      printWin.document.close();
      printWin.focus();
      printWin.print();
    },

    convertirMatriz() {
      this.matriz = [];
      for (let i = 0; i < this.nodes.length; i++) {
        this.matriz[i] = [];
        this.matriz[i].length = this.nodes.length;
        this.matriz[i].fill(0);
      }

      this.edges.get().forEach((edge) => {
        this.matriz[edge.from][edge.to] = 1;
      });
    },

    exportarPDF() {
      var imgData = (
        document.querySelector("#mynetwork canvas") as HTMLCanvasElement
      ).toDataURL("image/png", 1.0);
      var pdf = new jsPDF({
        orientation: "landscape",
        unit: "in",
        format: [14, 4],
      });
      pdf.addImage(imgData, "JPEG", 0, 0, 0, 0);
      pdf.save("download.pdf");
    },

    exportarImagen() {
      var link = document.createElement("a");
      link.href = (
        document.querySelector("#mynetwork canvas") as HTMLCanvasElement
      ).toDataURL("image/png", 1.0);
      link.download = "mynetwork.png";
      link.click();
    },

    guardar() {
      const json = {
        nodes: this.nodes.get(),
        edges: this.edges.get(),
      };
      const jsonString = JSON.stringify(json);
      const blob = new Blob([jsonString], { type: "application/json" });
      const url = URL.createObjectURL(blob);
      const link = document.createElement("a");
      link.href = url;
      link.download = "grafo.json";
      link.click();
    },
    cargar() {
      const input = document.createElement("input");
      input.type = "file";
      input.onchange = (e): void => {
        const file = e.target?.files[0] as File;
        const reader = new FileReader();
        reader.onload = (e) => {
          const json = JSON.parse(e.target?.result as string);
          this.nodes.clear();
          this.edges.clear();
          this.nodes.add(json.nodes);
          this.edges.add(json.edges);
          this.network = new Network(
            this.container,
            { edges: this.edges, nodes: this.nodes },
            this.options
          );
          this.convertirMatriz();
        };
        reader.readAsText(file);
      };
      input.click();
    },
    exportarExcelMatriz() {
      var wb = XLSX.utils.book_new();
      var ws = XLSX.utils.json_to_sheet(this.matriz);
      XLSX.utils.book_append_sheet(wb, ws, "Matriz");
      XLSX.writeFile(wb, "Matriz.xlsx");
    },
    obtenerAristasAdyacentes(nodosStr) {
      const nodos = nodosStr
      console.log(nodos)
      // Obtenemos las aristas para cada nodo (filtradas)
      for (const nodo of nodos) {
        const demasNodos = nodos.filter((n) => n != nodo);
        // TODO: obtener el nodo de vis usando nodo como inidce.

        /* Se obtiene los nodos que estan en demasNodos que son los cortados y se les cambia de color */
        demasNodos.forEach((n) => {
          this.nodes.update({
            id: n,
            color: {
              background: "#ff0000", //Aqui se le asigna el color a rojo, para que se vea que esta cortado.
            },
          });
        })

        this.edges.get().forEach((edge) => {
          if (edge.to === nodo) {
            // nodo es un destino, entonces validamos que los otros nodos
            // (ingresados por el usuario) no sean un origen
            const algunoDeLosDemasEsOrigen = demasNodos.includes(edge.from);
            if (algunoDeLosDemasEsOrigen) {
              console.log("Se descarta la arista", edge);
            } else {
              this.edges.update([{ ...edge, dashes: true, color: "#ff0000" }]); //Aquí se le asigna el color a rojo, para que se vea que esta cortado.
              // TODO: cambiar el estilo del nodo.
            }
          }
          if (edge.from === nodo) {
            // nodo es un origen, entonces validamos que los otros nodos
            // (ingresados por el usuario) no sean un destino
            const algunoDeLosDemasEsDestino = demasNodos.includes(edge.to);
            if (algunoDeLosDemasEsDestino) {
              console.log("Se descarta la arista", edge);
            } else {
              this.edges.update([{ ...edge, dashes: true, color: "#ff0000" }]); //Aquí se le asigna el color a rojo, para que se vea que esta cortado.
              // TODO: cambiar el estilo del nodo.
            }
          }
        });
        //this.nodes.get().forEach((nodes) => {
        //if(nodes.thisNodes()==nodo){
        //nodes.editNode();
        //}
        //});
      }
    },
  },
});
</script>

<template>
  <div>
    <div class=""></div>
    <div class="d-flex w-100 h-100 mx-auto flex-column page">
      <header class="mb-auto">
        <nav class="navbar navbar-expand-md navbar-expand-lg navbar-dark bg-faded">
          <div class="container-fluid">
            <ul class="navbar-nav mx-auto">
              <li class="nav-item dropdown text-center text-light">
                <a id="navbarScrollingDropdown" class="nav-link dropdown-toggle" href="#" role="button"
                  data-bs-toggle="dropdown" aria-expanded="false">
                  Archivo
                </a>
                <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                  <li>
                    <a href="#" class="dropdown-item">Nuevo grafo &raquo;</a>
                    <ul class="dropdown-menu dropdown-submenu">
                      <li>
                        <button class="dropdown-item" type="button" @click="crearVacio">
                          Vació
                        </button>
                      </li>
                      <li>
                        <button type="button" class="dropdown-item" @click="grafoAleatorio">
                          Aleatorio
                        </button>
                      </li>
                    </ul>
                  </li>
                  <li>
                    <a href="#" class="dropdown-item">Exportar datos &raquo;</a>
                    <ul class="dropdown-menu dropdown-submenu">
                      <li>
                        <button class="dropdown-item" type="button" @click="exportarExcelMatriz">
                          Excel
                        </button>
                      </li>
                      <li>
                        <button type="button" class="dropdown-item" @click="exportarImagen">
                          Imagen
                        </button>
                      </li>
                      <li>
                        <button type="button" class="dropdown-item" @click="exportarPDF">
                          PDF
                        </button>
                      </li>
                      <li>
                        <button type="button" class="dropdown-item" @click="guardar">
                          JSON
                        </button>
                      </li>
                    </ul>
                  </li>
                  <li>
                    <button class="dropdown-item" type="button" @click="cargar">
                      Importar JSON
                    </button>
                  </li>
                  <li>
                    <button class="dropdown-item" type="button" @click="imprimirCanvas">
                      Imprimir
                    </button>
                  </li>
                </ul>
              </li>

              <li class="nav-item dropdown text-center">
                <a id="navbarScrollingDropdown" class="nav-link dropdown-toggle" href="#" role="button"
                  data-bs-toggle="dropdown" aria-expanded="false">
                  Analizar
                </a>
                <ul class="dropdown-menu" aria-labelledby="navbarScrollingDropdown">
                  <li>
                    <button class="dropdown-item" type="button" @click="seleccionarNodos(nodes, edges, network)">
                      Algoritmo de partición de nodos
                    </button>
                  </li>
                  <li>
                    <button class="dropdown-item" type="button" @click="algoritmoKrager">
                      Algoritmo de Kruger
                    </button>
                  </li>
                  <li>
                    <button class="dropdown-item" type="button" @click="algoritmoStoerWagner">
                      Algoritmo de Stoer-Wagner
                    </button>
                  </li>
                </ul>
              </li>

              <li class="nav-item dropdown text-center">
                <a id="navbarScrollingDropdown" class="nav-link dropdown-toggle" href="#" role="button"
                  data-bs-toggle="dropdown" aria-expanded="false">
                  Ventana
                </a>
                <ul class="dropdown-menu" aria-labelledby="navbarScrollingDropdown">
                  <li>
                    <button class="dropdown-item" type="button" @click="vista = true">
                      Gráfica
                    </button>
                    <button class="dropdown-item" type="button" @click="vista = false, convertirMatriz()">Tabla</button>
                  </li>
                </ul>
              </li>
            </ul>
          </div>
        </nav>
      </header>

      <section>
        <div class="container py-3">
          <div class="row justify-content-md-center">
            <div v-show="mostrarMensaje.length != 0" class="alert alert-success text-center" role="alert">
              {{ mostrarMensaje }}
            </div>
            <div v-show="vista" id="mynetwork" class="col" />
            <div v-show="!vista" class="py-5">
              <div class="table-responsive">
                <table class="table table-dark table-striped table-bordered">
                  <thead>
                    <tr>
                      <th scope="col"># Nodo</th>
                      <th v-for="(item) in nodes.get() " :key="item.id">
                        {{ item.label.slice(4) }}
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(item, index) in nodes.get()" :key="item.id">
                      <th scope="row">{{ item.label.slice(4) }}</th>
                      <td v-for="(item2, index2) in matriz" :key="index2">
                        {{ item2[index] }}
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section>
        <ul class="nav nav-pills justify-content-center">
          <li class="nav-item">
            <button id="botones" class="btn btn-primary" type="button" :disabled="!vista" @click="añadirNodo()">
              Añadir nodo
            </button>
          </li>
          <li class="nav-item">
            <button id="botones" class="btn" :disabled="!vista" @click="mostrarModal = true">
              Añadir arista
            </button>
          </li>
          <li class="nav-item">
            <button id="botones" class="btn" :disabled="!vista" @click="eliminarNodo">
              Eliminar nodo
            </button>
          </li>
          <li class="nav-item">
            <button id="botones" class="btn" :disabled="!vista" @click="eliminarArista(edges)">
              Eliminar arista
            </button>
          </li>
        </ul>
      </section>
    </div>

    <teleport to="body">
      <div v-if="mostrarModal" class="modal fade show" tabindex="-1" aria-labelledby="exampleModalLabel"
        aria-hidden="true" role="dialog" style="display: block">
        <div class="modal-dialog modal-dialog-centered modal-backdrop-bg" :draggable="true">
          <div class="modal-content modal-backdrop-bg" :draggable="true">
            <div class="modal-header" :draggable="true">
              <h5 id="exampleModalLabel" class="modal-title">Añadir arista</h5>
              <button type="button" class="btn-close" @click="mostrarModal = false" />
            </div>
            <div class="modal-body">
              <div class="container-fluid">
                <div class="row">
                  <div class="col">
                    <p>
                      Origen:
                      <input v-model="origenArista" type="number" @change="
                        () => {
                          if (
                            origenArista > nodes.length ||
                            origenArista < 0
                          ) {
                            origenArista = 0;
                          }
                        }
                      " />
                    </p>
                  </div>
                  <div class="col">
                    <p>
                      Destino:
                      <input v-model="destinoArista" type="number" @change="
                        () => {
                          if (
                            destinoArista > nodes.length ||
                            destinoArista < 0
                          ) {
                            destinoArista = nodes.length;
                          }
                        }
                      " />
                    </p>
                  </div>
                </div>
                <div class="row">
                  <p class="col">
                    Peso: <input v-model="pesoArista" class="col" type="text" />
                  </p>
                  <div class="col py-4">
                    <div class="custom-control custom-checkbox">
                      <input id="defaultChecked2" v-model="esDirigido" type="checkbox" class="custom-control-input"
                        checked />
                      <label class="custom-control-label" for="defaultChecked2">¿Es dirigido?</label>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" @click="mostrarModal = false">
                Cancelar
              </button>
              <button type="button" class="btn btn-primary" :disabled="verificar"
                @click="añadirArista(), (mostrarModal = false)">
                Guardar
              </button>
            </div>
          </div>
        </div>
      </div>
    </teleport>
  </div>
</template>

<style>
#mynetwork {
  height: 400px;
  border: 1px solid #000;
}
</style>
