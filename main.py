from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    # Ouvrir le formulaire
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    # Trouver le champ texte
    champ = driver.find_element(By.NAME, "my-text")

    # Écrire dans le champ
    champ.send_keys("Bonjour Selenium")

    # Trouver le bouton et cliquer
    bouton = driver.find_element(By.CSS_SELECTOR, "button")
    bouton.click()

    # Attendre le message de confirmation
    message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )

    print("Message :", message.text)

    # Vérifier le résultat
    assert message.text == "Received!"

    print("Test réussi !")

    input("Appuie sur Entrée pour fermer Chrome...")

finally:
    driver.quit()
