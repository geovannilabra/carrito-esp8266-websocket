# 🚗 Carrito IoT Controlado por WebSockets (NodeMCU ESP8266 + Python + SQL)

Este repositorio contiene el sistema completo para el control y monitoreo en tiempo real de un vehículo robótico mediante una arquitectura IoT distribuida, utilizando WebSockets para una comunicación bidireccional de baja latencia.

---

## 📊 Arquitectura General del Proyecto

El proyecto está dividido en tres capas principales que trabajan sincronizadas:
1. **Front-end (Aplicaciones Web):** Dos interfaces de usuario montadas en internet que permiten interactuar con el sistema.
2. **Back-end (Servidor de Control):** Una API en Python que gestiona el flujo de datos, procesa peticiones y se comunica con la base de datos.
3. **Firmware (Hardware):** Código en C++ cargado en el NodeMCU ESP8266 para la manipulación física de los motores y lectura del entorno.

---

## 🌐 Aplicaciones Web (Front-end)

El proyecto cuenta con dos aplicaciones web independientes que corren del lado del cliente:

### 🎮 1. Aplicación Web de Control (`control.html`)
* **Propósito:** Interfaz de usuario diseñada para la manipulación y conducción del vehículo.
* **Funcionalidad:** Cuenta con un panel de botones interactivos para enviar comandos de dirección (Adelante, Atrás, Izquierda, Derecha, Parar) hacia el servidor de Python en formato JSON a través de un canal de WebSocket seguro.
* **Diseño:** Cuenta con una interfaz moderna en modo oscuro, optimizada con estilos responsivos y favicons personalizados.

### 🖥️ 2. Aplicación Web de Monitoreo (`monitor.html`)
* **Propósito:** Panel de supervisión de eventos y telemetría del estado del vehículo.
* **Funcionalidad:** Escucha el canal de comunicación para reflejar el estado actual del carrito, desplegando registros en tiempo real cada vez que se ejecuta una orden de movimiento o cuando el backend reporta alertas del sistema.

---

## 🐍 Servidor y Lógica (Back-end)

* **Tecnología:** Python (`app.py`).
* **Función:** Actúa como el puente central de comunicación. Recibe los comandos provenientes del Front-end (vía HTTP/WebSockets globales), los procesa, genera los registros correspondientes y los retransmite de forma inmediata al carrito físico por medio de la red local.

---

## 🗄️ Base de Datos y Persistencia

* **Tecnología:** Servidor SQL (Esquema relacional y Stored Procedures).
* **Persistencia:** Cada movimiento enviado por las interfaces de control se valida y se registra de forma estructurada en la base de datos a través de procedimientos almacenados para mantener un histórico de trayectorias, tiempos de ejecución e identificadores únicos de movimiento.

---
