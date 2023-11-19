<div align="center">

# Proyecto Django Blog

Blog realizado en Python con Django, como parte del proyecto final del curso "Python" de Coderhouse.

</div>

**Tabla de contenidos**

- [Funcionalidades](#funcionalidades)
    - [App de usuarios](#app-de-usuarios)
    - [App de blog y comentarios](#app-de-blog-y-comentarios)
    - [Implementaciones del proyecto](#implementaciones-del-proyecto)
- [Dependencias utilizadas](#dependencias-utilizadas)
- [Instalación](#instalación)

## Funcionalidades

### App de usuarios

- Registro y login de usuarios mediante autenticación con Django
- Vista de perfil de usuario con el detalle de cantidad de entradas y comentarios realizados, con los respectivos títulos y links de las entradas afectadas en cada caso.
- Edición de perfil de usuario, pudiendo incorporar biografía y avatar si lo desea. El avatar una vez añadido, puede eliminarse también.
- Edición de password separada del resto de campos editables.
- Eliminación de cuenta de usuario, con la respectiva eliminación de las entradas y comentarios por él mismo realizados.

### App de blog y comentarios

Todos los usuarios, logueados o no, tienen acceso a la vista principal del blog, así como al detalle de las entradas. Sin embargo, para acceder a ciertas funcionalidades, éstos deberán estar registrados y logueados. Éstas funcionalidades son:
    - Creación de entradas nuevas (con campo de texto enriquecido)
    - Edición de entradas (un usuario sólo podrá editar si él mismo es el autor de la entrada)
    - Eliminación de entradas (sólo podrá eliminar una entrada quien la haya creado)
    - Comentar una entrada
    - Eliminar el comentario (sólo si el usuario es quien lo ha realizado)

Por su parte, dentro de cada entrada se puede visualizar un apartado de "Entradas relacionadas", el cuál se basa en mostrar aquellas que pertenezcan a la misma categoría que la entrada a la que se ha accedido.

Finalmente, en la pantalla de inicio se observa el listado de entradas, con un apartado de búsqueda por título; y el acceso a la vista "About" desde la barra de navegación.

### Panel de admin

Registrando un superusuario, es posible acceder al panel de admin de Django y acceder a toda la información de los modelos.

## Implementaciones del proyecto

- Herencia de HTML
- Formularios: 
    - mediante HTML
    - que heredan de los modelos de Form de django
    - de búsqueda
    - con campos de texto enriquecido
- Arquitectura MVT
- Uso de clases basadas en vistas
- Uso de decoradores y mixins
- Registro de los modelos en el panel de admin de Django

## Dependencias utilizadas

- Django
- django-ckeditor
- Pillow

## Instalación

```
git clone https://github.com/valessol/django-store.git
cd django-store
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

#### Autor: Valeria Silveira