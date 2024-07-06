# TPintegrador_Programacion1_UNER
# Sistema de Gestión de Bibliotecas 📚

## Objetivo
Desarrollar una solución de software para gestionar el préstamo y devolución de libros en una biblioteca.

## Requerimientos

### Registro de Libros
- **ID de Libro:** número único y autoincremental
- **Título**
- **Autor**
- **Editorial**
- **Año de Publicación**
- **Género**
- **Cantidad Disponible**

### Gestión de Socios
- **ID de Socio:** número único y autoincremental
- **Nombre**
- **Apellido**
- **Fecha de Nacimiento**
- **Dirección**
- **Correo Electrónico**
- **Teléfono**

### Registro de Préstamos y Devoluciones
- **ID de Préstamo:** número único y autoincremental
- **ID de Socio**
- **ID de Libro**
- **Fecha de Préstamo**
- **Costo (en caso de que tuviera)**
- **Fecha de Devolución**
- **Estado del Préstamo:** En Curso/Devuelto

## Características del Software 🚀
- **Almacenamiento de Información:** utilización de archivos JSON para almacenar los datos.
- **Interfaces de usuario interactivas que permiten:**
  - Registrar, editar y eliminar libros.
  - Registrar, editar y eliminar socios.
  - Registrar préstamos y devoluciones.
  - Búsqueda de libros por título, género, autor y editorial.
  - Generar reportes de préstamos y devoluciones por socio, libro y rango de fechas.

### Funcionalidad Extra
A criterio del alumno/grupo, como desarrollo de interfaz gráfica, consumo de una API externa, búsquedas avanzadas, nuevas funcionalidades similares que aporten valor agregado.

### Funcionalidad Añadida
Se agregó la funcionalidad que genera un código QR para cada libro. Para usarla, instala la librería `pyqrcode`:
```sh
pip install pyqrcode
```

## Integrantes
- Noah Nicanor Peralta Cassutti
- Santiago Nicolás Bertorello
- María Belén Colado
