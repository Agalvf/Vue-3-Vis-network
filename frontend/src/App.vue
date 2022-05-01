<template>
  <div class="d-flex w-100 h-100 mx-auto flex-column">
    <!-- <div class="space"></div> -->
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
            <i class="fas fa-bars"></i>
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
                          @click="crearVacio()"
                        >
                          Vació
                        </button>
                      </li>
                      <li>
                        <button
                          type="button"
                          class="dropdown-item"
                          @click="grafoAleatorio()"
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
                    <button class="dropdown-item" type="button">Cerrar</button>
                  </li>
                  <li>
                    <button class="dropdown-item" type="button">Guardar</button>
                  </li>
                  <li>
                    <button class="dropdown-item" type="button">
                      Guardar como
                    </button>
                  </li>
                  <li>
                    <button
                      class="dropdown-item"
                      type="button"
                      @click="exportarJson()"
                    >
                      Exportar datos
                    </button>
                  </li>
                  <li>
                    <button class="dropdown-item" type="button">
                      Importar datos
                    </button>
                  </li>
                  <li>
                    <button class="dropdown-item" type="button">Inicio</button>
                  </li>
                  <li>
                    <button
                      class="dropdown-item"
                      type="button"
                      @click="imprimirCanvas()"
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
                  Editar
                </a>
                <ul
                  class="dropdown-menu"
                  aria-labelledby="navbarScrollingDropdown"
                >
                  <li>
                    <button class="dropdown-item" type="button">
                      Deshacer
                    </button>
                  </li>
                  <li>
                    <button class="dropdown-item" type="button">Nodo</button>
                  </li>
                  <li>
                    <button class="dropdown-item" type="button">Arco</button>
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
                    <button class="dropdown-item" type="button">Gráfica</button>
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
              <i class="fas fa-shopping-cart"></i>
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
                <i class="fas fa-bell"></i>
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
    <div class="container py-5">
      <div class="row justify-content-md-center">
        <div id="mynetwork" class="col"></div>
        <div class="col">
          <button class="btn btn-light" type="button" @click="añadirNodo()">
            Añadir nodo
          </button>
          <button
            type="button"
            class="btn btn-light"
            data-bs-toggle="modal"
            data-bs-target="#staticBackdrop"
            @click="añadirArista()"
          >
            Añadir arista
          </button>
        </div>
      </div>
    </div>

    <!-- Modal añadir arista -->
    <div
      id="staticBackdrop"
      class="modal fade"
      data-bs-backdrop="static"
      data-bs-keyboard="false"
      tabindex="-1"
      aria-labelledby="staticBackdropLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 id="staticBackdropLabel" class="modal-title">Añadir arista</h5>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            <div class="container-fluid">
              <div class="row">
                <div class="col">
                  <p>Nodo 1: <input type="text" /></p>
                </div>
                <div class="col">
                  <p>Nodo 2: <input type="text" /></p>
                </div>
              </div>
              <div class="row">
                <div class="col">
                  <p>Peso: <input type="text" /></p>
                </div>
                <div class="row form-check">
                  <div class="col">
                    <input
                      id="flexCheckChecked"
                      class="form-check-input"
                      type="checkbox"
                      value=""
                      checked
                    />
                    <label class="form-check-label" for="flexCheckChecked">
                      ¿Es dirigido?
                    </label>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <button
              type="button"
              class="btn btn-secondary"
              data-bs-dismiss="modal"
            >
              Cerrar
            </button>
            <button type="button" class="btn btn-primary">Aceptar</button>
          </div>
        </div>
      </div>
    </div>
    <!--  -->
  </div>
</template>

<script>
import { Network } from "vis-network";
import { DataSet } from "vis-data";

export default {
  name: "App",
  data() {
    return {
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
          physics: false,
        },
      },
      container: "",
      network: null,
    };
  },
  computed: {
    graph_data() {
      this.nodes.add([
        { id: 1, label: "Node 1" },
        { id: 2, label: "Node 2" },
        { id: 3, label: "Node 3" },
        { id: 4, label: "Node 4" },
      ]);
      this.edges.add([
        { from: 1, to: 3 },
        { from: 1, to: 2 },
        { from: 2, to: 4 },
      ]);
      return {
        nodes: this.nodes,
        edges: this.edges,
      };
    },
  },

  mounted() {
    this.nodes = new DataSet();
    this.edges = new DataSet();
    this.container = document.getElementById("mynetwork");
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
      console.log(this.nodes);
    },
    crearVacio() {
      this.nodes = new DataSet();
      this.edges = new DataSet();
      this.network = new Network(
        this.container,
        { edges: this.edges, nodes: this.nodes },
        this.options
      );
    },
    grafoAleatorio() {
      const numeroNodos = Math.floor(Math.random() * (6 - 1) + 3);
      const nodes = Array(numeroNodos)
        .fill(0)
        .map((_, i) => {
          return { id: i, label: `Node ${i}` };
        });

      var arr = [];

      for (var id = 0; id < numeroNodos; id++) {
        arr.push({
          from: id,
          to: nodes[Math.floor(Math.random() * numeroNodos)]["id"],
        });
      }

      this.nodes = new DataSet();
      this.edges = new DataSet();
      this.nodes.add(nodes);
      this.edges.add(arr);

      this.network = new Network(
        this.container,
        { edges: this.edges, nodes: this.nodes },
        this.options
      );
    },

    imprimirCanvas() {
      const win1 = window.open();
      var canvas = document.getElementBy("canvas");
      win1.document.write("<img src = '" + canvas.toDataURL() + "'/>");
      win1.print();
      win1.location.reload();
    },
  },
};
</script>

<style>
@import "./assets/styles.css";
#mynetwork {
  height: 400px;
  border: 1px solid #000;
}
</style>
