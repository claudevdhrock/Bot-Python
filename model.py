from selenium import webdriver

CLICK = "CLICK"
JAVASCRIPT_CLICK = "JAVASCRIPT_CLICK"
CLICK_TIPOS = [CLICK, JAVASCRIPT_CLICK]


class ScraperBot():
    driver = None

    def __init__(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.maximize_window()

    def ir_a(self, url):
        self.driver.set_page_load_timeout(30)
        self.driver.get(url)

    def test(self):
        javaScript = "document.getElementsByName('username')[0].click();"
        self.driver.execute_script(javaScript)

    def esperar_por(self, xpath, REINTENTOS=10, CLICK=CLICK):
        resultado = []
        while REINTENTOS > 0:
            REINTENTOS = REINTENTOS - 1
            try:
                resultado = self.driver.find_elements_by_xpath(xpath)
                break
            except:
                pass
        if len(resultado) == 1:
            if CLICK:
                resultado.click()

            return resultado[0]
        else:
            return resultado

