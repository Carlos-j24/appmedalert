from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import time

# 📂 carpeta evidencias
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
# 📅 IR A CITAS
# ===============================
driver.get("http://127.0.0.1:5500/frontend/citas.html")

wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

input("📸 Captura FORMULARIO CITAS")

# ===============================
# 📝 LLENAR FORMULARIO (SI EXISTE)
# ===============================
try:
    driver.find_element(By.ID, "fecha").send_keys("30/04/2026")
    driver.find_element(By.ID, "hora").send_keys("09:00AM")
    driver.find_element(By.ID, "medico").send_keys("Dr. Sneider Riveros")
    driver.find_element(By.ID, "especialidad").send_keys("Medicina General")

    input("📸 Captura DATOS DE CITA")

    driver.find_element(By.ID, "guardar-btn").click()

    print("✅ Cita ingresada correctamente")

except:
    print("⚠️ No se detectó formulario (puede ser solo visual)")

# ===============================
# ⏳ ESPERA
# ===============================
time.sleep(2)

input("📸 Captura RESULTADO")

# ===============================
# 🔚 CIERRE
# ===============================
input("ENTER para cerrar")
driver.quit()