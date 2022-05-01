<template>
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
                aria-labelledby="navbarScrollingDropdown"
              >
                <li class="nav-item dropdown">
                  <a
                    id="navbarScrollingDropdown"
                    class="nav-link dropdown-toggle"
                    href="#"
                    role="button"
                    data-bs-toggle="dropdown"
                    aria-expanded="false"
                  >
                    Nuevo grafo
                  </a>
                  <ul
                    class="dropdown-menu"
                    aria-labelledby="navbarScrollingDropdown"
                  >
                    <li><a class="dropdown-item" href="#">Personalizado</a></li>
                    <li>
                      <a class="dropdown-item" href="#">Aleatorio</a>
                    </li>
                  </ul>
                </li>
                <li>
                  <button
                    class="dropdown-item"
                    type="button"
                    @click="$emit('funcion')"
                  >
                    Grafo Aleatorio
                  </button>
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
                  <button class="dropdown-item" type="button">
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
                  <button class="dropdown-item" type="button">Imprimir</button>
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
                  <button class="dropdown-item" type="button">Deshacer</button>
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
</template>