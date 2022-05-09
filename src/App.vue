<script lang="ts">
  import { defineComponent } from 'vue';
  import { Network } from 'vis-network';
  import { DataSet } from 'vis-data';
  import 'https://unpkg.com/vis-network/standalone/umd/vis-network.min.js';
  import { jsPDF } from 'jspdf';

  export default defineComponent({
    name: 'App',
    data() {
      return {
        nodes: DataSet.prototype,
        edges: DataSet.prototype,
        container: HTMLElement.prototype,
        network: Network.prototype,
        mostrarModal: false,
        origenArista: 0,
        destinoArista: 0,
        pesoArista: '0',
        options: {
          locale: 'es',
          height: '100%',
          width: '100%',
          manipulation: {
            enabled: true,
            initiallyActive: true,
          },
          nodes: {
            physics: false,
          },
        },
      };
    },

    computed: {
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      graph_data(): any {
        this.nodes.add([
          { id: 1, label: 'Node 1' },
          { id: 2, label: 'Node 2' },
          { id: 3, label: 'Node 3' },
          { id: 4, label: 'Node 4' },
        ]);

        this.edges.add([
          { from: 1, to: 3, label: '0' },
          { from: 1, to: 2, label: '0' },
          { from: 2, to: 4, label: '0' },
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
          console.log('False');
          return false;
        }
      },
    },

    mounted() {
      this.nodes = new DataSet();
      this.edges = new DataSet();
      this.container = document.getElementById('mynetwork') as HTMLInputElement;
      this.network = new Network(this.container, this.graph_data, this.options);
    },

    methods: {
      añadirNodo() {
        this.nodes.add({
          id: this.nodes.length + 1,
          label: `Node ${this.nodes.length + 1}`,
        });
      },
      añadirArista() {
        console.log(this.origenArista, this.destinoArista, this.pesoArista);
        if (this.destinoArista != null) {
          this.edges.add({
            from: this.origenArista,
            to: this.destinoArista,
            label: this.pesoArista,
          });
        }
      },

      crearVacio() {
        this.nodes.clear();
        this.edges.clear();
      },

      grafoAleatorio() {
        this.nodes.clear();
        this.edges.clear();

        const numeroNodos = Math.floor(Math.random() * (12 - 1) + 3);
        const nodes = Array(numeroNodos)
          .fill(0)
          .map((_, i) => {
            return { id: i, label: `Node ${i}` };
          });

        var arr = [];

        for (var id = 0; id < numeroNodos; id++) {
          arr.push({
            from: id,
            to: nodes[Math.floor(Math.random() * numeroNodos)]['id'],
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
      },

      imprimirCanvas() {
        var canvas = document.querySelector(
          '#mynetwork canvas'
        ) as HTMLCanvasElement;
        var png = canvas.toDataURL('image/png');
        var windowContent = '<img src="' + png + '">';

        var printWin =
          window?.open('', '', 'width=340,height=260') ?? Window.prototype;
        console.log(printWin);
        printWin.document.open();
        printWin.document.write(windowContent);
        printWin.document.close();

        printWin.print();
      },

      exportarPDF() {
        var imgData = (
          document.querySelector('#mynetwork canvas') as HTMLCanvasElement
        ).toDataURL('image/png', 1.0);
        var pdf = new jsPDF({
          orientation: 'landscape',
          unit: 'in',
          format: [14, 4],
        });

        pdf.addImage(imgData, 'JPEG', 0, 0, 0, 0);
        pdf.save('download.pdf');
      },

      exportarImagen() {
        var link = document.createElement('a');
        link.download = 'filename.png';
        link.href = (
          document.querySelector('#mynetwork canvas') as HTMLCanvasElement
        ).toDataURL('image/png', 1.0);
        link.click();
      },

      guardar() {
        const json = {
          nodes: this.nodes.get(),
          edges: this.edges.get(),
        };
        let text = JSON.stringify(json);
        let filename = 'network.json';
        let element = document.createElement('a');
        element.setAttribute(
          'href',
          'data:application/json;charset=utf-8,' + encodeURIComponent(text)
        );
        element.setAttribute('download', filename);

        element.style.display = 'none';
        document.body.appendChild(element);

        element.click();
        document.body.removeChild(element);
      },
    },
  });
</script>

<!-- <script setup lang="ts">
import { onMounted, computed,ref } from 'vue';
import { Network } from "vis-network";
import { DataSet } from "vis-data";
import "https://unpkg.com/vis-network/standalone/umd/vis-network.min.js";
import { jsPDF } from "jspdf";

let nodes = DataSet.prototype;
let edges = DataSet.prototype;
let network = Network.prototype
let container = HTMLElement.prototype
const origenArista = ref(0);
const destinoArista = ref(0);
const options = {
  locale: "es",
  height: "100%",
  width: "100%",
  manipulation: {
    enabled: true,
    initiallyActive: true,
  },
  nodes: {
    physics: false,
  }
}

const graphData = computed(() => {
  nodes.add([
    { id: 1, label: "Node 1" },
    { id: 2, label: "Node 2" },
    { id: 3, label: "Node 3" },
    { id: 4, label: "Node 4" },
  ]),

  edges.add([
    { from: 1, to: 3, label: "0" },
    { from: 1, to: 2, label: "0" },
    { from: 2, to: 4, label: "0" },
  ])
  return {edges,nodes}
})

onMounted(() => {
  nodes = new DataSet()
  edges = new DataSet()

  const container = document.getElementById("mynetwork") as HTMLElement;
  console.log(graphData.value)
  const network = new Network(container, graphData.value, options);
  console.log(graphData)
})

function añadirNodo() {
  nodes.add({
    id: nodes.length + 1,
    label: `Node ${nodes.length + 1}`,
  });
};

function añadirArista() {
  console.log(nodes);
}

function crearVacio() {
  edges.clear()
  nodes.clear()
};

function grafoAleatorio() {
  const numeroNodos = Math.floor(Math.random() * (12 - 1) + 3);
  const nodesAleatorio = Array(numeroNodos)
    .fill(0)
    .map((_, i) => {
      return { id: i, label: `Node ${i}` };
    });

  var arr = [];

  for (var id = 0; id < numeroNodos; id++) {
    arr.push({
      from: id,
      to: nodesAleatorio[Math.floor(Math.random() * numeroNodos)]["id"],
      label: `${Math.floor(Math.random() * (15 - 1) + 1)}`
    });
  }
  nodes.clear()
  edges.clear()
  nodes.add(nodesAleatorio);
  edges.add(arr);
  network = Network.prototype;
  network = new Network(container, { edges, nodes }, options)
};

function imprimirCanvas() {
  var canvas = document.querySelector('#mynetwork canvas') as HTMLCanvasElement
  var png = canvas.toDataURL("image/png");
  var windowContent = '<img src="' + png + '">';

  var printWin = window.open('', '', 'width=340,height=260')!;
  printWin.document.open();
  printWin.document.write(windowContent);
  printWin.document.close();

  printWin.print();
};

function importarDatos() {

};

function exportarPDF() {
  var imgData = (document.querySelector('#mynetwork canvas') as HTMLCanvasElement).toDataURL("image/png", 1.0);
  var pdf = new jsPDF({
    orientation: "landscape",
    unit: "in",
    format: [14, 4]
  });

  pdf.addImage(imgData, 'JPEG', 0, 0, 0, 0);
  pdf.save("download.pdf");
};

function exportarImagen() {
  var link = document.createElement('a');
  link.download = 'filename.png';
  link.href = (document.querySelector('#mynetwork canvas') as HTMLCanvasElement).toDataURL("image/png", 1.0);
  link.click();
};

function guardar() {
  const json = {
    nodes: nodes.get(),
    edges: edges.get()
  }
  console.log(json)
  let text = JSON.stringify(json);
  let filename = 'network.json';
  let element = document.createElement('a');
  element.setAttribute('href', 'data:application/json;charset=utf-8,' + encodeURIComponent(text));
  element.setAttribute('download', filename);

  element.style.display = 'none';
  document.body.appendChild(element);

  element.click();
  document.body.removeChild(element);
};
</script> -->

<template>
  <div>
    <!-- <div class=""></div> -->
    <div class="d-flex w-100 h-100 mx-auto flex-column page">
      <header class="mb-auto">
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
          <div class="container-fluid">
            <button
              class="navbar-toggler"
              type="button"
              data-mdb-toggle="collapse"
              data-mdb-target="#navbarSupportedContent"
              aria-controls="navbarSupportedContent"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <i class="fas fa-bars" />
            </button>
            <div id="navbarSupportedContent" class="collapse navbar-collapse">
              <a class="navbar-brand mt-2 mt-lg-0" href="#">
                <img
                  src="https://mdbcdn.b-cdn.net/img/logo/mdb-transaprent-noshadows.webp"
                  height="15"
                  alt="MDB Logo"
                  loading="lazy"
                />
              </a>

              <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item dropdown">
                  <a
                    id="navbarScrollingDropdown"
                    class="nav-link dropdown-toggle"
                    href="#"
                    role="button"
                    data-bs-toggle="dropdown"
                    aria-expanded="false"
                  >
                    Archivo
                  </a>
                  <ul
                    class="dropdown-menu"
                    aria-labelledby="navbarDropdownMenuLink"
                  >
                    <li>
                      <a href="#" class="dropdown-item">Nuevo grafo &raquo;</a>
                      <ul class="dropdown-menu dropdown-submenu">
                        <li>
                          <button
                            class="dropdown-item"
                            type="button"
                            @click="crearVacio"
                          >
                            Vació
                          </button>
                        </li>
                        <li>
                          <button
                            type="button"
                            class="dropdown-item"
                            @click="grafoAleatorio"
                          >
                            Aleatorio
                          </button>
                        </li>
                      </ul>
                    </li>
                    <li>
                      <button class="dropdown-item" type="button">Abrir</button>
                    </li>
                    <li>
                      <button class="dropdown-item" type="button">
                        Cerrar
                      </button>
                    </li>
                    <li>
                      <button
                        class="dropdown-item"
                        type="button"
                        @click="guardar"
                      >
                        Guardar
                      </button>
                    </li>
                    <li>
                      <button class="dropdown-item" type="button">
                        Guardar como
                      </button>
                    </li>
                    <li>
                      <a href="#" class="dropdown-item"
                        >Exportar datos &raquo;</a
                      >
                      <ul class="dropdown-menu dropdown-submenu">
                        <li>
                          <button class="dropdown-item" type="button">
                            Excel
                          </button>
                        </li>
                        <li>
                          <button
                            type="button"
                            class="dropdown-item"
                            @click="exportarImagen"
                          >
                            Imagen
                          </button>
                        </li>
                        <li>
                          <button
                            type="button"
                            class="dropdown-item"
                            @click="exportarPDF"
                          >
                            PDF
                          </button>
                        </li>
                      </ul>
                    </li>
                    <li>
                      <button class="dropdown-item" type="button">
                        Importar datos
                      </button>
                    </li>
                    <li>
                      <button class="dropdown-item" type="button">
                        Inicio
                      </button>
                    </li>
                    <li>
                      <button
                        class="dropdown-item"
                        type="button"
                        @click="imprimirCanvas"
                      >
                        Imprimir
                      </button>
                    </li>
                  </ul>
                </li>

                <li class="nav-item dropdown">
                  <a
                    id="navbarScrollingDropdown"
                    class="nav-link dropdown-toggle"
                    href="#"
                    role="button"
                    data-bs-toggle="dropdown"
                    aria-expanded="false"
                  >
                    Analizar
                  </a>
                  <ul
                    class="dropdown-menu"
                    aria-labelledby="navbarScrollingDropdown"
                  >
                    <li>
                      <button class="dropdown-item" type="button">
                        Algoritmos
                      </button>
                    </li>
                  </ul>
                </li>

                <li class="nav-item dropdown">
                  <a
                    id="navbarScrollingDropdown"
                    class="nav-link dropdown-toggle"
                    href="#"
                    role="button"
                    data-bs-toggle="dropdown"
                    aria-expanded="false"
                  >
                    Ventana
                  </a>
                  <ul
                    class="dropdown-menu"
                    aria-labelledby="navbarScrollingDropdown"
                  >
                    <li>
                      <button class="dropdown-item" type="button">
                        Gráfica
                      </button>
                      <button class="dropdown-item" type="button">Tabla</button>
                    </li>
                  </ul>
                </li>
              </ul>
            </div>
            <!-- Collapsible wrapper -->

            <!-- Right elements -->
            <div class="d-flex align-items-center">
              <!-- Icon -->
              <a class="text-reset me-3" href="#">
                <i class="fas fa-shopping-cart" />
              </a>

              <!-- Notifications -->
              <div class="dropdown">
                <a
                  id="navbarDropdownMenuLink"
                  class="text-reset me-3 dropdown-toggle hidden-arrow"
                  href="#"
                  role="button"
                  data-mdb-toggle="dropdown"
                  aria-expanded="false"
                >
                  <i class="fas fa-bell" />
                  <span class="badge rounded-pill badge-notification bg-danger"
                    >1</span
                  >
                </a>
                <ul
                  class="dropdown-menu dropdown-menu-end"
                  aria-labelledby="navbarDropdownMenuLink"
                >
                  <li>
                    <a class="dropdown-item" href="#">Some news</a>
                  </li>
                  <li>
                    <a class="dropdown-item" href="#">Another news</a>
                  </li>
                  <li>
                    <a class="dropdown-item" href="#">Something else here</a>
                  </li>
                </ul>
              </div>

              <!-- Avatar -->
              <div class="dropdown">
                <a
                  id="navbarDropdownMenuAvatar"
                  class="dropdown-toggle d-flex align-items-center hidden-arrow"
                  href="#"
                  role="button"
                  data-mdb-toggle="dropdown"
                  aria-expanded="false"
                >
                  <img
                    src="https://mdbcdn.b-cdn.net/img/new/avatars/2.webp"
                    class="rounded-circle"
                    height="25"
                    alt="Black and White Portrait of a Man"
                    loading="lazy"
                  />
                </a>
                <ul
                  class="dropdown-menu dropdown-menu-end"
                  aria-labelledby="navbarDropdownMenuAvatar"
                >
                  <li>
                    <a class="dropdown-item" href="#">My profile</a>
                  </li>
                  <li>
                    <a class="dropdown-item" href="#">Settings</a>
                  </li>
                  <li>
                    <a class="dropdown-item" href="#">Logout</a>
                  </li>
                </ul>
              </div>
            </div>
            <!-- Right elements -->
          </div>
          <!-- Container wrapper -->
        </nav>
      </header>

      <section>
        <div class="container py-5">
          <div class="row justify-content-md-center">
            <div id="mynetwork" class="col" />
          </div>
        </div>
      </section>

      <section>
        <ul class="nav nav-pills justify-content-center">
          <li class="nav-item">
            <button
              id="botones"
              class="btn"
              type="button"
              @click="añadirNodo()"
            >
              Añadir nodo
            </button>
          </li>
          <li class="nav-item">
            <button id="botones" class="btn" @click="mostrarModal = true">
              Añadir arista
            </button>
          </li>
          <li class="nav-item">
            <button id="botones" class="btn">&#8651; Deshacer</button>
          </li>
        </ul>
      </section>
    </div>

    <!-- Modal -->
    <teleport to="body">
      <div
        v-if="mostrarModal"
        class="modal draggable fade show"
        tabindex="-1"
        aria-labelledby="exampleModalLabel"
        aria-hidden="true"
        role="dialog"
        style="display: block"
      >
        <div class="modal-dialog modal-dialog-centered">
          <div class="modal-content">
            <div class="modal-header">
              <h5 id="exampleModalLabel" class="modal-title">Añadir arista</h5>
              <button
                type="button"
                class="btn-close"
                @click="mostrarModal = false"
              />
            </div>
            <div class="modal-body">
              <p>
                Origen:
                <input
                  v-model="origenArista"
                  type="number"
                  @change="
                    () => {
                      if (origenArista > nodes.length || origenArista < 0) {
                        origenArista = 0;
                      }
                    }
                  "
                />
              </p>
              <p>
                Destino:
                <input
                  v-model="destinoArista"
                  type="number"
                  @change="
                    () => {
                      if (destinoArista > nodes.length || destinoArista < 0) {
                        destinoArista = nodes.length;
                      }
                    }
                  "
                />
              </p>
              <p>Peso <input v-model="pesoArista" type="text" /></p>
            </div>
            <div class="modal-footer">
              <button
                type="button"
                class="btn btn-secondary"
                @click="mostrarModal = false"
              >
                Close
              </button>
              <button
                type="button"
                class="btn btn-primary"
                :disabled="verificar"
                @click="añadirArista(), (mostrarModal = false)"
              >
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
