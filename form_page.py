from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:

    def __init__(self, driver):
        self.driver = driver

    # Ouvrir le formulaire
    def ouvrir(self):
        self.driver.get(
            "https://www.selenium.dev/selenium/web/web-form.html"
        )

    # Remplir le champ texte
    def remplir_champ(self, texte):
        champ = self.driver.find_element(By.NAME, "my-text")
        champ.send_keys(texte)

    # Cliquer sur le bouton
    def envoyer(self):
        bouton = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[type='submit']")
            )
        )

        # Faire défiler la page jusqu'au bouton
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            bouton
        )

        # Cliquer sur le bouton
        bouton.click()

    # Récupérer le message de confirmation
    def recuperer_message(self):
        message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "message"))
        )
        return message.text
