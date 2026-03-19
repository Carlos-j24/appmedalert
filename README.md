# 🩺 MedAlert – Aplicación Web de Alertas Médicas

MedAlert es una **aplicación web** diseñada para apoyar a las personas en el **control y seguimiento de sus medicamentos y alertas médicas**, facilitando la organización de horarios, dosis y recordatorios de forma clara, accesible y confiable.

Este proyecto se desarrolla como parte de un **proceso formativo**, aplicando buenas prácticas de análisis, diseño y desarrollo de software.

---

## 📑 Tabla de Contenido

* [Descripción del Proyecto](#-descripción-del-proyecto)
* [Objetivo General](#-objetivo-general)
* [Objetivos Específicos](#-objetivos-específicos)
* [Alcance del Proyecto](#-alcance-del-proyecto)
* [Características Principales](#-características-principales)
* [Arquitectura del Sistema](#-arquitectura-del-sistema)
* [Tecnologías Utilizadas](#-tecnologías-utilizadas)
* [Instalación y Uso](#-instalación-y-uso)
* [Ejecución del Proyecto](#-ejecución-del-proyecto)
* [Estructura del Proyecto](#-estructura-del-proyecto)
* [Metodología de Desarrollo](#-metodología-de-desarrollo)
* [Estado del Proyecto](#-estado-del-proyecto)
* [Autor](#-autor)

---

## 🧾 Descripción del Proyecto

MedAlert surge como una solución tecnológica ante la dificultad que muchas personas presentan para recordar **horarios de medicamentos, dosis y tratamientos médicos**.

La aplicación busca reducir errores, olvidos y riesgos asociados al incumplimiento de tratamientos, ofreciendo una plataforma digital sencilla, intuitiva y accesible desde la web.

---

## 🎯 Objetivo General

Desarrollar una **aplicación web** que permita gestionar alertas médicas, facilitando el control de medicamentos, horarios y recordatorios para los usuarios.

---

## 🎯 Objetivos Específicos

* Diseñar una interfaz clara y fácil de usar.
* Permitir el registro de medicamentos y horarios.
* Generar alertas visuales para el cumplimiento del tratamiento.
* Aplicar buenas prácticas de desarrollo y documentación.
* Estructurar el proyecto bajo una arquitectura organizada.

---

## 📌 Alcance del Proyecto

El proyecto MedAlert contempla:

* Gestión básica de medicamentos.
* Registro de horarios y alertas.
* Visualización de información médica del usuario.
* Aplicación web funcional en su versión inicial (PMV).

No incluye, por el momento, integraciones externas ni notificaciones por SMS o correo electrónico.

---

## 🚀 Características Principales

* 📋 Registro de medicamentos.
* ⏰ Programación de horarios.
* 🔔 Alertas visuales.
* 🧑‍⚕️ Organización de información médica.
* 💻 Acceso desde navegador web.
* 🎨 Interfaz amigable y comprensible.

---

## 🏗️ Arquitectura del Sistema

MedAlert sigue una arquitectura básica cliente-servidor, organizada en:

* **Frontend:** Interfaz gráfica para la interacción del usuario.
* **Backend:** Implementado con PocketBase para la gestión de datos y lógica del sistema.
* **Base de datos:** Integrada mediante PocketBase (SQLite).

---

## 🧪 Tecnologías Utilizadas

* **Frontend:**

  * HTML5
  * CSS3
  * JavaScript

* **Backend:**

  * PocketBase (Backend ligero con base de datos integrada)

* **Base de datos:**

  * SQLite (gestionada por PocketBase)

* **Control de versiones:**

  * Git
  * GitHub

---

## ⚙️ Instalación y Uso

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/Carlos-j24/appmedalert.git
   ```

2. Ingresar al proyecto:

   ```bash
   cd appmedalert
   ```

---

## ▶️ Ejecución del Proyecto

1. Ir a la carpeta del backend:

   ```bash
   cd backend/pocketbase
   ```

2. Ejecutar el servidor:

   ```bash
   .\pocketbase serve
   ```

3. Abrir en el navegador:

   ```
   http://127.0.0.1:8090/_/
   ```

---

## 🗂 Estructura del Proyecto

```
appmedalert/
│
├── backend/pocketbase → Servidor PocketBase
├── frontend → Interfaz de usuario
├── database → Script SQL del sistema
├── docs → Diagrama Entidad-Relación
├── README.md → Documentación del proyecto
```

---

## 🧠 Metodología de Desarrollo

El desarrollo del proyecto se basa en buenas prácticas de ingeniería de software, incluyendo:

* Análisis de requerimientos
* Diseño del modelo entidad-relación
* Construcción de base de datos
* Desarrollo incremental
* Documentación del proceso

---

## 📊 Estado del Proyecto

🟡 En desarrollo

Actualmente se cuenta con:

* Modelo de base de datos completo
* Implementación en PocketBase
* Estructura del proyecto organizada
* Documentación inicial

---

## 👨‍💻 Autor

Carlos Castro

---

## 🔔 Módulo de Recordatorios

El módulo de recordatorios permitirá al usuario:

* Programar alertas para la toma de medicamentos.
* Recibir notificaciones en horarios configurados.
* Visualizar el historial de alertas atendidas.

Este módulo hace parte de las funcionalidades principales de MedAlert.
