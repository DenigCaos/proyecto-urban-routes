### ayu es donde creamos las variables que se utilizaran en el archivo data.py
### estas variables son fijas y no cambian a excepcion de la url

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import helpers
class UrbanRoutesPage:
    log_principal = (By.CLASS_NAME, 'logo-image')
    def __init__(self, driver):
        self.driver = driver

### Desarrollo del set para las rutas y get para recoger el valor del cambo para chequearlo
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    def set_from_to(self, from_address, to_address):
        # Encuentra y envia los datos en el campo de la dirección de origen
        self.driver.find_element(*self.from_field).send_keys(from_address)
        # Encuentra y envia los datos en el campo de la dirección de destino
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from_to(self):
        return self.driver.find_element(*self.from_field).get_property('value'), self.driver.find_element(*self.to_field).get_property('value')

    ### click en boton confort y chequeo de aparicion de boton de etiqueta blanket
    botton_round = (By.XPATH, '/html/body/div/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    confort_select = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.tariff-cards > div:nth-child(5)')
    def click_botton_confort (self):
        #click en el boton del home page para pedir un taxi
        self.driver.find_element(*self.botton_round).click()
        #click en el boton de confort del home page
        self.driver.find_element(*self.confort_select).click()

    def click_check_confort_select (self):
        #chequea que el boton de confort se ha seleccionado
        elemento = self.driver.find_element(*self.blanket_label)
        confort_is_check= elemento.is_displayed()
        return confort_is_check

    ### pasos para ingresar numero de telefono, esperar codigo sms de numero de telefono y confirmación
    botton_phone_num = (By.CLASS_NAME, 'np-text')
    input_phone = (By.ID, 'phone')
    botton_phone_num_pop_up_window = (By.CSS_SELECTOR, '#root > div > div.number-picker.open > div.modal > div.section.active > form > div.buttons > button')
    botton_next_phone_code = (By.CSS_SELECTOR,'#root > div > div.number-picker.open > div.modal > div.section.active > form > div.buttons > button:nth-child(1)')
    sms_code_field = (By.XPATH, '/html/body/div/div/div[1]/div[2]/div[2]/form/div[1]/div/input')
    def set_steps_number_and_code_phone (self,number_phone):
        #click en el boton de home page para ingresar el numero de telefono
        self.driver.find_element(*self.botton_phone_num).click()
        # Encuentra y envia los datos en el campo del numero de telefono
        self.driver.find_element(*self.input_phone).send_keys(number_phone)
        #click en el boton para agregar el numero de telefono desde la ventana emergente
        self.driver.find_element(*self.botton_phone_num_pop_up_window).click()
        # El codigo no esta arrojando nada, hice pruebas con print y el valor era none
        codigo_confirmacion = helpers.retrieve_phone_code(self.driver)
        #self.set_sms_code(str(codigo_confirmacion))
        # Encuentra y envia los datos en el campo del numero del codigo sms
        self.driver.find_element(*self.sms_code_field).send_keys(str(codigo_confirmacion))
        #click para cerrar la ventana emergente del numero de telefono
        self.driver.find_element(*self.botton_next_phone_code).click()

    def get_phone_number(self):
        return self.driver.find_element(*self.botton_phone_num).get_property('outerText')

    ### pasos para ingreso de numero de tarjeta y codigo de tarjeta y chequeo para confirmación
    botton_payment_method = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.pp-button.filled')
    botton_add_card = (By.CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal > div.section.active > div.pp-selector > div.pp-row.disabled')
    card_number_field = (By.CLASS_NAME, 'card-input')
    card_code_number_field = (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/form/div[1]/div[2]/div[2]/div[2]/input')
    botton_agree_card=(By.CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal.unusual > div.section.active.unusual > form > div.pp-buttons > button:nth-child(1)')
    check_agree_card= (By.CSS_SELECTOR,'#root > div > div.payment-picker.open > div.modal > div.section.active > div.pp-selector > div:nth-child(3)')
    close_pop_up_card_windows=(By.CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal > div.section.active > button')
    def set_steps_payment_method(self, number_card, code_card):
        #click para el boton de metodo de pago de home page
        self.driver.find_element(*self.botton_payment_method).click()
        #click para el boton de añadir una tarjeta
        self.driver.find_element(*self.botton_add_card).click()
        # Encuentra y envia los datos en el campo del numero de tarjeta
        self.driver.find_element(*self.card_number_field).send_keys(number_card)
        # Encuentra el campo del código de la tarjeta y envía el código
        code_field = self.driver.find_element(*self.card_code_number_field)
        code_field.send_keys(code_card)
        # Envía la tecla TAB para cambiar el enfoque
        code_field.send_keys(Keys.TAB)
        helpers.wait_to_be_clickable_of_element(self.driver, self.botton_agree_card, 3)
        # click para el boton de añadir una tarjeta en la segunda ventana emergente
        self.driver.find_element(*self.botton_agree_card).click()

    def click_close_pop_up_card_windows(self):
       #click para cerrar la ventana emergente del numero de telefono
       self.driver.find_element(*self.close_pop_up_card_windows).click()
    def check_agree_tcard(self):
        #chequea que el boton de confort se ha seleccionado
        elemento = self.driver.find_element(*self.check_agree_card)
        agree_tcard = elemento.is_displayed()
        return agree_tcard

    ### pasos para mensaje del driver
    message_for_driver_field=(By.ID, 'comment')
    def set_message_for_driver(self, driver_message):
        # Encuentra y envia los datos en el campo de mensaje para el conductor
        self.driver.find_element(*self.message_for_driver_field).send_keys(driver_message)
    def get_message_for_driver(self):
        return self.driver.find_element(*self.message_for_driver_field).get_property('value')

    ### pasos activar selector del blanket
    blanket_selector=(By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div:nth-child(1) > div > div.r-sw > div > span')
    blanket_value=(By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div:nth-child(1) > div > div.r-sw > div > input')
    blanket_label = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div:nth-child(1) > div')

    def click_blanket_selector(self):
        # click para seleccionar manta y pañuelos
        self.driver.find_element(*self.blanket_selector).click()
    def get_blanket_value(self):
        return self.driver.find_element(*self.blanket_value).get_property('value')

    ### pasos para agregar 2 helados
    ice_cream_plus=(By.CSS_SELECTOR,'#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div.r.r-type-group > div > div.r-group-items > div:nth-child(1) > div > div.r-counter > div > div.counter-plus')
    ice_cream_count = (By.CSS_SELECTOR,'#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div.r.r-type-group > div > div.r-group-items > div:nth-child(1) > div > div.r-counter > div > div.counter-value')
    def click_ice_cream_plus(self):
        # click para agregar helados
        self.driver.find_element(*self.ice_cream_plus).click()

    def get_ice_cream_value(self):
        return self.driver.find_element(*self.ice_cream_count).get_property('outerText')

    ### pasos para solicitar el taxi y verificar que el conductor haya sido seleccionado
    botton_find_taxi = (By.CSS_SELECTOR, '#root > div > div.workflow > div.smart-button-wrapper > button')
    taxi_driver_selected = (By.XPATH,'/html/body/div/div/div[5]/div[2]/div[2]/div[1]/div[1]/div[1]/img')
    order_header_title = (By.CLASS_NAME, 'order-header-title')
    def click_find_taxi(self):
        # click para pedir un taxi
        self.driver.find_element(*self.botton_find_taxi).click()
    def check_botton_find_taxi(self):
        #chequea que el boton de buscar taxi aparezca
        elemento = self.driver.find_element(*self.botton_find_taxi)
        botton_find_taxi = elemento.is_displayed()
        return botton_find_taxi
    def check_taxi_driver_selected(self):
        #chequea que el boton de confort se ha seleccionado
        elemento = self.driver.find_element(*self.taxi_driver_selected)
        taxi_driver_selected = elemento.is_displayed()
        return taxi_driver_selected
    def check_order_header_title(self):
        #chequea que el boton de confort se ha seleccionado
        elemento = self.driver.find_element(*self.order_header_title)
        order_header_title_show = elemento.is_displayed()
        return order_header_title_show
