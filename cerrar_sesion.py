from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os

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
# 🚪 LOGOUT
# ===============================
wait.until(EC.element_to_be_clickable((By.ID, "logout-btn")))

input("📸 Captura BOTÓN LOGOUT")

driver.find_element(By.ID, "logout-btn").click()

# ===============================
# ✅ VALIDACIÓN
# ===============================
wait.until(lambda d: "index" in d.current_url)

input("📸 Captura RESULTADO (Login)")

if "index" in driver.current_url:
    print("✅ CP008 OK - Logout exitoso")
else:
    print("❌ CP008 FALLÓ")

# ===============================
# 🔚 CIERRE
# ===============================
input("ENTER para cerrar")
driver.quit()