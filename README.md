# Prueba de Entrada - Desarrollo de Software CC3S2

Este repositorio reúne la solución a la prueba de entrada del curso de Desarrollo de Software. Aquí muestro cómo combino varias habilidades: crear programas de línea de comandos (CLI), automatizar tareas con Bash y Make, programar en Python con pruebas unitarias, aplicar un flujo de trabajo organizado en Git y explorar temas de redes y APIs.

## Sección 2.3: Explicación del Flujo de Git

A continuación se explica de manera breve las estrategias de Git utilizadas en este proyecto:

*   **Merge Fast-Forward (FF):** Esta es la manera más simple de fusionar. Si la rama de destino no se ha movido desde que se abre la rama de trabajo, Git solo adelanta el puntero y el historial se ve limpio y lineal.

*   **Rebase:** Con rebase, tomo los commits de mi rama y los “reaplico” sobre la versión más actual de main. Esto da la sensación de que siempre trabajé desde lo último, evitando commits de merge innecesarios.

*   **Cherry-pick:** Este comando es ideal cuando se quiere traer solo un cambio específico (como un arreglo rápido) sin necesidad de arrastrar todo lo que está en la otra rama.

## Sección 3.2: Header de la Respuesta de API

Al consultar a la API `https://jsonplaceholder.typicode.com/posts/1`, el header que indica el tipo de contenido devuelto es:

*   **Content-Type**: `application/json; charset=UFT-8