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

# 🌐 abrir login
driver.get("http://127.0.0.1:5500/frontend/index.html")

# ⏳ esperar que cargue
wait.until(EC.presence_of_element_located((By.ID, "username")))

# 📸 1 (pantalla inicial)
input("📸 Toma la captura del LOGIN y presiona ENTER...")

# ✍️ escribir datos incorrectos
driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("0000")
driver.find_element(By.ID, "role").send_keys("Paciente")

# 📸 2 (datos llenos)
input("📸 Toma la captura con DATOS INCORRECTOS y presiona ENTER...")

# 🔘 click login
wait.until(EC.element_to_be_clickable((By.ID, "login-btn"))).click()

# ⏳ esperar que aparezca el error
wait.until(EC.visibility_of_element_located((By.ID, "error-msg")))

# 📸 3 (mensaje de error)
input("📸 Toma la captura del ERROR y presiona ENTER...")

# ✅ validación
error = driver.find_element(By.ID, "error-msg")

if error.is_displayed():
    print("✅ CP002 OK - Error mostrado correctamente")
else:
    print("❌ CP002 FALLÓ")

# 🔚 cerrar cuando quieras
input("🔍 Presiona ENTER para cerrar navegador...")
driver.quit()