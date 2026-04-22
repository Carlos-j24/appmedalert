from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import time

if not os.path.exists("evidencias"):
    os.makedirs("evidencias")

service = Service("C:/Users/USUARIO/Desktop/desarrollo SENA/selenium/chromedriver-win64/chromedriver.exe")

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10)

# ===============================
# 🔐 LOGIN
# ===============================
driver.get("http://127.0.0.1:5500/frontend/index.html")

wait.until(EC.presence_of_element_located((By.ID, "username")))

input("📸 Captura LOGIN")

driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "role").send_keys("Paciente")

input("📸 Captura DATOS")

driver.find_element(By.ID, "login-btn").click()

# ===============================
# 🏠 DASHBOARD
# ===============================
wait.until(lambda d: "dashboard" in d.current_url)

input("📸 Captura DASHBOARD")

# ===============================
# 💊 IR A AGREGAR MEDICAMENTO
# ===============================
driver.get("http://127.0.0.1:5500/frontend/agregar_medicamento.html")

wait.until(EC.presence_of_element_located((By.ID, "nombre")))

input("📸 Captura FORMULARIO")

# ===============================
# ✍️ LLENAR FORMULARIO
# ===============================
driver.find_element(By.ID, "nombre").send_keys("Diclofenaco")
driver.find_element(By.ID, "dosis").send_keys("500 mg")
driver.find_element(By.ID, "horario").send_keys("0800 AM")

input("📸 Captura DATOS")

# ===============================
# 💾 GUARDAR
# ===============================
driver.find_element(By.ID, "guardar-med").click()
# 🔥 CERRAR ALERTA
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.accept()

# Espera redirección
wait.until(lambda d: "medicamentos" in d.current_url)

input("📸 Captura RESULTADO")

# ===============================
# ✅ VALIDACIÓN
# ===============================
lista = driver.find_element(By.ID, "lista-medicamentos")

if "Diclofenaco" in lista.text:
    print("✅ CP007 OK - Medicamento registrado")
else:
    print("❌ CP007 FALLÓ")

# ===============================
# 🔚 CIERRE
# ===============================
input("ENTER para cerrar")
driver.quit()