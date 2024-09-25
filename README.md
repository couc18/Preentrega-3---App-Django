# Preentrega-3-Django App Django

## Estructura del Proyecto

- **models.py**: Define los modelos `Author`, `Book` y `Publisher`. El modelo `Author` incluye un campo de nombre y correo electrónico, mientras que `Book` tiene un título y una referencia a un autor. El modelo `Publisher` tiene un nombre y una relación con los libros.
  
- **forms.py**: Contiene los formularios para manejar la entrada de datos para `Author`, `Book`, y `Publisher`. Se ha añadido un campo personalizado para ingresar el título del libro directamente en el formulario de la editorial (`PublisherForm`).

- **views.py**: Contiene las vistas para agregar nuevos datos (`add_data`) y buscar libros en la base de datos (`search_data`). Las vistas se encargan de procesar los formularios y de manejar la lógica de consulta en la base de datos.
  
- **urls.py**: Define las rutas de la aplicación, incluidas las páginas de inicio, agregar datos y buscar libros.

- **templates/**: Contiene los archivos HTML que renderizan las páginas web. Estos archivos extienden una plantilla base `base.html`.
- 
## Explicación de Funcionalidades

### 1. **Agregar Autores, Libros y Editoriales**
- URL: `/add/`
  
En esta página, los usuarios pueden ingresar información de un autor, libro y editorial. El formulario permite ingresar el nombre del autor, su correo electrónico, el título de un libro, y la editorial a la que pertenece el libro.

### 2. **Buscar Libros Existentes**
- URL: `/search/`

Los usuarios pueden buscar libros por su título. El formulario realiza una búsqueda insensible a mayúsculas/minúsculas y devuelve una lista de coincidencias de libros junto con el autor correspondiente. Además, muestra todos los libros existentes en la base de datos.

### 3. **Visualización de Resultados**
En la página de búsqueda, si se encuentran libros, estos se muestran en una lista. Si no se encuentra ningún libro, se muestra un mensaje informando al usuario. Este mensaje solo aparece después de que se realiza una búsqueda.
