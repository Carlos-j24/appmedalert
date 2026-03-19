// Mostrar fecha y hora actual
function actualizarHora() {
  const ahora = new Date();
  const fecha = ahora.toLocaleDateString();
  const hora = ahora.toLocaleTimeString();
  document.getElementById("fecha-hora").innerText = `${fecha} - ${hora}`;
}
setInterval(actualizarHora, 1000);

// Simular alertas al cargar el dashboard
window.onload = function () {
  if (document.getElementById("alertas")) {
    setTimeout(() => {
      document.getElementById("alertas").innerHTML += `
        <div class="alert">💊 Toma tu medicamento: Losartán 50mg</div>
      `;
    }, 1000);

    setTimeout(() => {
      document.getElementById("alertas").innerHTML += `
        <div class="alert">📅 Cita médica: 10:00 AM con el Dr. Pérez</div>
      `;
    }, 3000);
  }
};
// Alternar entre modo claro y oscuro
function toggleDarkMode() {
  document.body.classList.toggle("dark-mode");
}

