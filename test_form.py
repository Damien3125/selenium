import pytest
from selenium import webdriver
from form_page import FormPage

def test_formulaire():

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)

    try:
        formulaire = FormPage(driver)

        formulaire.ouvrir()
        formulaire.remplir_champ("Bonjour Selenium")
        formulaire.envoyer()

        message = formulaire.recuperer_message()

        assert message == "Received!"
        print("Test réussi !")

    finally:
        driver.quit()
