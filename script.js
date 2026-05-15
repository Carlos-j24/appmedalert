// ===============================
// 🌙 MODO OSCURO
// ===============================
function toggleDarkMode() {
  document.body.classList.toggle("dark-mode");
}

// ===============================
// 🕒 FECHA Y HORA
// ===============================
function actualizarFechaHora() {
  const fechaHora = document.getElementById("fecha-hora");
  if (fechaHora) {
    const ahora = new Date();
    fechaHora.textContent = ahora.toLocaleString();
  }
}

setInterval(actualizarFechaHora, 1000);

// ===============================
// 🔐 LOGIN
// ===============================
const loginForm = document.getElementById("loginForm");

if (loginForm) {
  loginForm.addEventListener("submit", function (e) {
    e.preventDefault();

    const user = document.getElementById("username").value;
    const pass = document.getElementById("password").value;
    const role = document.getElementById("role").value;

    const errorMsg = document.getElementById("error-msg");

    if (user === "admin" && pass === "123456") {
      window.location.href = "dashboard.html";
    } else {
      if (errorMsg) {
        errorMsg.style.display = "block";
      }
    }
  });
}

// ===============================
// 💊 GUARDAR MEDICAMENTO
// ===============================
const formMed = document.getElementById("form-med");

if (formMed) {
  formMed.addEventListener("submit", function (e) {
    e.preventDefault();

    const nombre = document.getElementById("nombre").value;
    const dosis = document.getElementById("dosis").value;
    const horario = document.getElementById("horario").value;

    const nuevoMed = {
      nombre,
      dosis,
      horario
    };

    let medicamentos = JSON.parse(localStorage.getItem("medicamentos")) || [];

    medicamentos.push(nuevoMed);

    localStorage.setItem("medicamentos", JSON.stringify(medicamentos));

    alert("✅ Medicamento guardado");

    // Redirigir a lista
    window.location.href = "medicamentos.html";
  });
}

// ===============================
// 📋 MOSTRAR MEDICAMENTOS
// ===============================
const listaMed = document.getElementById("lista-medicamentos");

if (listaMed) {
  let medicamentos = JSON.parse(localStorage.getItem("medicamentos")) || [];

  if (medicamentos.length === 0) {
    listaMed.innerHTML = "<p>No hay medicamentos registrados</p>";
  } else {
    medicamentos.forEach(med => {
      const item = document.createElement("div");
      item.innerHTML = `💊 ${med.nombre} - ${med.dosis} - ${med.horario}`;
      listaMed.appendChild(item);
    });
  }
}

// ===============================
// 🔔 ALERTAS (SIMULACIÓN)
// ===============================
const alertasDiv = document.getElementById("alertas");

if (alertasDiv) {
  setTimeout(() => {
    const alerta = document.createElement("div");
    alerta.innerHTML = "🔔 Es hora de tomar tu medicamento";
    alerta.style.background = "#ffdddd";
    alerta.style.padding = "10px";
    alerta.style.marginTop = "10px";
    alertasDiv.appendChild(alerta);
  }, 3000);
}

// ===============================
// 📅 REGISTRO DE CITAS
// ===============================
const formCita = document.querySelector("form");

if (formCita && window.location.href.includes("citas.html")) {
  formCita.addEventListener("submit", function (e) {
    e.preventDefault();

    alert("✅ Cita médica registrada correctamente");
  });
}
// ===============================
// 🚪 LOGOUT
// ===============================
document.addEventListener("DOMContentLoaded", function () {

  const logoutBtn = document.getElementById("logout-btn");

  if (logoutBtn) {
    logoutBtn.addEventListener("click", function () {

      console.log("Cerrando sesión...");

      // (Opcional) limpiar datos
      localStorage.clear();

      // 🔥 REDIRECCIÓN CORRECTA
      window.location.href = "index.html";

    });
  }

});