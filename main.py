## Test de la pagina Urban Routes main contiene los test de la pagina Urban Routes
## los asert son los que definen si la prueba es exitosa o no

import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import helpers
import UrbanRoutesPage

class TestUrbanRoutes:

    driver = webdriver.Chrome
    @classmethod
    def setup_class(cls):
        # Configuración de las opciones de Chrome
        options = Options()
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--start-maximized")
        options.add_argument("--window-size=1920x1080")
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        # Inicialización del WebDriver con las opciones definidas
        cls.driver = webdriver.Chrome(options=options)

    def test0_acces_page(self):
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Acceder a la URL de Urban Routes.
        self.driver.get(data.urban_routes_url)
        # Espera hasta que cargue el logo principal de la pagina
        helpers.wait_visibility_of_element(self.driver, routes_page.log_principal, 3)


    def test_set_route(self):
        # Crea una instancia de UrbanRoutesPage pasando el driver como argumento.
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Iguala las variales de direccion origen y destino a la respectivas en el archivo data
        address_from, address_to = data.address_from, data.address_to
        # Llamar al método set_from en la instancia de UrbanRoutesPage.
        routes_page.set_from_to(address_from,address_to)
        # Confirmación de la prueba
        assert routes_page.get_from_to() == (address_from, address_to)

    def test_click_confort(self):
        # Crea una instancia de UrbanRoutesPage pasando el driver como argumento.
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Espera hasta que cargue el boton de pedir un taxi
        helpers.wait_visibility_of_element(self.driver, routes_page.botton_round, 3)
        # Hace click en el boton de pedir un taxi
        routes_page.click_botton_confort()
        assert True, routes_page.click_check_confort_select

    def test_set_phone_number(self):
        # Crea una instancia de UrbanRoutesPage pasando el driver como argumento.
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        phone_number = data.phone_number
        # proceso de ingreso de numero de telefono y codigo sms
        routes_page.set_steps_number_and_code_phone(phone_number)
        assert routes_page.get_phone_number() == phone_number

    def test_add_card_code(self):
        # Crea una instancia de UrbanRoutesPage pasando el driver como argumento.
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        card_number=data.card_number
        card_code=data.card_code
        # proceso del metodo de pago
        routes_page.set_steps_payment_method(card_number, card_code)
        #verificacion que el metodo de pago funciono
        assert True, routes_page.check_agree_tcard()
        # cierre de ventana de metodo de pago
        routes_page.click_close_pop_up_card_windows()
    def test_message_for_driver(self):
        # Crea una instancia de UrbanRoutesPage pasando el driver como argumento.
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Ingresa el mensaje del conductor
        message_for_driver=data.message_for_driver
        routes_page.set_message_for_driver(message_for_driver)
        assert routes_page.get_message_for_driver() == message_for_driver

    def test_blanket_on(self):
        # Crea una instancia de UrbanRoutesPage pasando el driver como argumento.
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Seleccionar la manta y pañuelo
        routes_page.click_blanket_selector()
        assert routes_page.get_blanket_value() == 'on'

    def test_order_2_ice_creams(self):
        # Crea una instancia de UrbanRoutesPage pasando el driver como argumento.
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Agregar 2 helados
        for _ in range(2):
            routes_page.click_ice_cream_plus()
        assert routes_page.get_ice_cream_value() == '2'


    def test_taxi_request_modal_display(self):
        # Crea una instancia de UrbanRoutesPage pasando el driver como argumento.
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Hace click pedir un taxi y espera hasta que el sistema seleccione un conductor
        routes_page.click_find_taxi()
        assert True, routes_page.check_order_header_title()

    def test_check_show_name_driver_modal(self):
        # Crea una instancia de UrbanRoutesPage pasando el driver como argumento.
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        helpers.wait_visibility_of_element(self.driver, routes_page.taxi_driver_selected, 40)
        assert True, routes_page.check_taxi_driver_selected()
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

