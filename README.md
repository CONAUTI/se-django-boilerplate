## se-archetype-django

Este proyecto utiliza un `Makefile` para gestionar varias tareas comunes relacionadas con el desarrollo, ejecución y mantenimiento del entorno de la aplicación.

## Tabla de Contenidos

- [Estructura del Makefile](#estructura-del-makefile)
- [Comandos Disponibles](#comandos-disponibles)
- [Agregar Variables al Makefile](#agregar-variables-al-makefile)
- [Ejemplos](#ejemplos)

---

## Estructura del Makefile

### General
- **OWNER**: Nombre del propietario del proyecto. En este caso, `conauti`.
- **PROJECT_NAME**: Obtiene dinámicamente el nombre del proyecto usando el comando `basename "$(PWD)"`.
- **IMAGE**: Define la imagen de Docker con la etiqueta `latest`.
- **PROJECT_DIR**: Directorio principal de la aplicación, que es `app`.
- **MODULE_NAME**: Obtiene dinámicamente el nombre del módulo desde `package.json`.
- **WORKDIR**: Directorio de trabajo dentro del contenedor.
- **HTTP_PORT**: Puerto HTTP, con un valor predeterminado de `8080`.
- **APP_ENV**: Entorno de la aplicación (`local` por defecto).
- **ENV**: Entorno genérico (`local` por defecto).

### Tareas Comunes
El archivo `Makefile` incluye comandos predefinidos para tareas como:
- Ejecutar la aplicación localmente.
- Crear nuevas aplicaciones.
- Realizar migraciones de base de datos.
- Construir y destruir imágenes de Docker.
- Ejecutar contenedores.

---

## Comandos Disponibles

### Comandos Generales

| Comando             | Descripción                                                                                  |
|---------------------|----------------------------------------------------------------------------------------------|
| `make help`         | Muestra la lista de comandos disponibles y su descripción.                                   |

### Comandos de la Aplicación

| Comando             | Descripción                                                                                  |
|---------------------|----------------------------------------------------------------------------------------------|
| `make app.local`    | Ejecuta la aplicación en el entorno local.                                                   |
| `make app.add`      | Crea una nueva aplicación en el directorio `app`.                                             |
| `make app.migrate`  | Realiza migraciones de base de datos (creación de archivos y actualización de la base).       |

### Comandos de Docker

| Comando               | Descripción                                                                                  |
|-----------------------|----------------------------------------------------------------------------------------------|
| `make copy_package`   | Copia los requisitos de Python al directorio `docker/dev`.                                   |
| `make ct.build.image` | Construye la imagen de Docker para el proyecto sin usar caché.                               |
| `make ct.destroy.image` | Elimina la imagen de Docker asociada al proyecto.                                           |
| `make ct.run`         | Ejecuta el contenedor de Docker con las configuraciones especificadas.                       |

---

## Agregar Variables al Makefile

Para agregar nuevas variables al `Makefile`, sigue estos pasos:

1. **Define la Variable**  
   Las variables deben definirse en la sección correspondiente. Por ejemplo:
   ```makefile
   ## GENERAL ##
   NUEVA_VARIABLE = valor_por_defecto
