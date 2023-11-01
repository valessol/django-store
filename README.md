# Proyecto Django Store

## App Store

### Carga de productos a mostrar

Existen dos productos cargados en la base de datos de sqlite3, sin embargo, pueden añadirse más productos a partir del formulario correspondiente, el cual se encuentra en el menú 'Agregar' de la barra de navegación.

### Carga de productos en el carrito

Es posible que un cliente agregue productos al carrito mediante el formulario que se encuentra accediendo por en el mismo lugar que el formulario anterior.

Los productos del carrito se agregan, pero no existe aún una vista que permita renderizarlos.

Por otro lado, la idea final sería añadir estos productos desde un botón directamente desde la vista de detalle del producto, y no mediante formulario, el cual se realiza en este caso a los fines de cumplir la consigna del desafío.

### Formulario de consultas y sugerencias

Permite a los clientes dejar consultas y/o sugerencias relacionadas al sitio.
Se accede mediante el menú 'Contacto', en la barra de navegación.

## Características a destacar de este proyecto

- Herencia de HTML
- Formularios mediante HTML
- Formularios de django
- Formulario de búsqueda de productos
- Arquitectura MVT