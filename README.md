Diego Mendoza cohote 9 srpint 8 

Este código de pruebas automatizadas para una aplicación de servicio
Urban-Routes de taxi o transporte que proporcionan métodos para interactuar
con la interfaz de usuario de la aplicación.

Se crearon cuatro archivos, los archivos main.py, urban routepage.py, helpers.py donde se desarrollan todos los
metodos y el archivo data.py donde se declaran todos los valores de la variables.

Se definieron los localizadores y métodos necesarios en la clase UrbanRoutesPage
y las pruebas en la clase TestUrbanRoutes.

Las pruebas cubren las siguientas acciones:

1) Configurar la dirección.
2) Seleccionar la tarifa Comfort.
3) Rellenar el número de teléfono.
4) Agregar una tarjeta de crédito.
5) Escribir un mensaje para el conductor.
6) Pedir una manta y pañuelos.
7) Pedir 2 helados.
8) Solicitar la busqueda del taxi.
9) Se espera a que aparezca la información del conductor para finalizar la automatización.

Lo métodos para Interactuar con la Página Web:

set_from(self, from_address): Este método toma una dirección de origen
como argumento y la ingresa en el campo correspondiente en la página web.

set_to(self, to_address): Similar al método anterior, pero para la
dirección de destino.

get_from(self): Recupera y devuelve el valor actual del campo de dirección
de origen.

get_to(self): Recupera y devuelve el valor actual del campo de dirección de
destino.

click_botton_round(self): Simula un clic en el botón que probablemente inicia
la búsqueda de un taxi o un viaje en la aplicación.

click_confort_select(self): Simula un clic en una opción de selección de confort,
que podría ser una clase de servicio de taxi como económico, estándar, o de lujo. 


click_phone_number_home_page(self): Simula un clic en el botón para ingresar un
número de teléfono en la página principal.

set_phone_number(self, number_phone): Ingresa un número de teléfono proporcionado
en el campo correspondiente.

click_phone_number_pop_up_window(self): Simula un clic en el botón de confirmación
después de ingresar el número de teléfono en una ventana emergente.

set_sms_code(self, code_sms): Ingresa un código SMS proporcionado en el campo
correspondiente, probablemente para la verificación de dos pasos.

click_closet_pop_up_window_phone_number(self): Cierra la ventana emergente donde
se ingresó el número de teléfono.

click_payment_method(self): Simula un clic en el botón para seleccionar un
método de pago.

click_add_card(self): Simula un clic en el botón para añadir una nueva tarjeta de
crédito o débito.

set_card_number(self, number_card): Ingresa el número de una tarjeta en el campo
correspondiente.

set_code_number(self, code_card): Ingresa el código CVV de la tarjeta y simula la presión
de la tecla TAB para cambiar el enfoque del campo, lo cual podría ser necesario para
activar el botón de confirmación.

click_add_card_2nd_pop_up_window(self): Confirma la adición de la tarjeta en una segunda
ventana emergente.

click_closet_pop_up_window_payment_method(self): Cierra la ventana emergente del método de pago.

set_message_for_driver(self, driver_message): Ingresa un mensaje para el conductor en el
campo correspondiente.

click_blanket_selector(self): Selecciona una manta y pañuelos, lo que sugiere que la aplicación
permite personalizar el viaje con comodidades adicionales.

click_ice_cream_plus(self): Añade helados al pedido, lo que indica que la aplicación podría
ofrecer productos o servicios adicionales.

click_find_taxi(self): Inicia la búsqueda de un taxi disponible.

Clase TestUrbanRoutes:

Esta clase contiene métodos para configurar el entorno de prueba (setup_class)
y para realizar pruebas específicas (test_set_route).
setup_class(cls): Configura el navegador Chrome con capacidades especiales para
registrar el rendimiento, necesario para la función retrieve_phone_code.

test_set_route(self): Realiza una prueba automatizada que navega a una URL específica
 y realiza acciones en la página utilizando la clase UrbanRoutesPage.

 Tecnologias :
   Phyton
   postman
