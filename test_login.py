from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os

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

# 📸 1 - Pantalla inicial
input("📸 Toma captura LOGIN (pantalla inicial) y presiona ENTER...")

# ingresar datos correctos
driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "role").send_keys("Paciente")

# 📸 2 - Datos ingresados
input("📸 Toma captura DATOS CORRECTOS y presiona ENTER...")

# click login
wait.until(EC.element_to_be_clickable((By.ID, "login-btn"))).click()

# ===============================
# 🏠 DASHBOARD
# ===============================
wait.until(lambda d: "dashboard" in d.current_url)

# 📸 3 - Acceso exitoso
input("📸 Toma captura DASHBOARD (login exitoso) y presiona ENTER...")

# ===============================
# ✅ VALIDACIÓN
# ===============================
if "dashboard" in driver.current_url:
    print("✅ CP001 OK - Login exitoso")
else:
    print("❌ CP001 FALLÓ")

# ===============================
# 🔚 CIERRE
# ===============================
input("🔍 Presiona ENTER para cerrar navegador...")
driver.quit()