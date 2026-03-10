# AlsoPlaying - Change Log

## [English Version]

### 🚀 Major Improvements & New Features

*   **Plug & Play Logic**: The application is now fully standalone. It no longer requires users to have Python pre-installed to open the main interface.
*   **Automated Python Setup**: Added a "one-click" recovery system. If a user tries to generate a tracker and doesn't have Python, the app offers to download and install Python 3.13 automatically in the background.
*   **Smart Python Detection**: Implemented a "Deep Search" function (`find_all_pythons`) that scans the Windows Registry and system folders. This fixes the common bug where Windows tries to open the Microsoft Store instead of using a real Python installation.
*   **Advanced Icon Engine**:
    *   Added support for extracting icons directly from `.exe` files.
    *   Integrated a professional embedded icon for the main app.
    *   Improved support for custom `.ico` files during tracker generation.
*   **Safety & Stability**:
    *   Fixed a critical bug that caused recursive window opening ("infinite tabs") when running as a compiled `.exe`.
    *   Separated the user interface logic from the PyInstaller compilation environment.
*   **Modern UI/UX**:
    *   Upgraded the interface with a "Premium Dark Mode" aesthetic.
    *   Updated dialogs and messages to be more user-friendly for non-technical players.
*   **Robust Tracker Generation**:
    *   **Tkinter Fixed**: Implemented an "Aggressive Compilation" mode (`--collect-all`) to ensure that generated trackers always include the graphical interface, fixing the "No module named tkinter" error.
    *   **Proactive Validation**: The app now pre-checks if the detected Python version supports graphical interfaces before starting the build.
*   **Professional Repository Setup**:
    *   Configured a standard `.gitignore` to keep the project clean of temporary build files and environment subproducts.

---

## [Versión en Español]

*   **Icon Stability Fix**: Resolved a garbage collection issue in Tkinter that caused icons to disappear or "break" when interacting with the system grid or resizing windows.
*   **Unique Instance Assets**: Implemented a content-based hashing system for temporary icon files, preventing asset conflicts when running multiple tracker instances simultaneously.
*   **Code Cleanup**: Removed all legacy debug print statements and optimized empty lines for a cleaner, production-ready codebase.

---

## [Versión en Español]

### 🚀 Mejoras Principales y Nuevas Funciones

*   **Estabilidad de Iconos Corregida**: Solucionado un problema de recolección de basura en Tkinter que causaba que los iconos desaparecieran o se "rompieran" al interactuar con la interfaz del sistema o cambiar el tamaño de las ventanas.
*   **Activos de Instancia Únicos**: Implementado un sistema de hashing basado en contenido para los nombres de iconos temporales, evitando conflictos entre múltiples trackers abiertos a la vez.
*   **Limpieza de Producción**: Eliminados todos los enunciados `print` de depuración y optimizadas las líneas de código para una ejecución más limpia y profesional.
*   **Lógica "Plug & Play"**: La aplicación ahora es totalmente independiente. Ya no requiere que los usuarios tengan Python instalado para abrir la interfaz principal.
*   **Configuración de Python Automatizada**: Se ha añadido un sistema de recuperación de "un solo clic". Si un usuario intenta generar un tracker y no tiene Python, la app se ofrece a descargar e instalar Python 3.13 automáticamente en segundo plano.
*   **Búsqueda Inteligente de Python**: Implementada la función `find_all_pythons` que escanea el Registro de Windows y carpetas del sistema. Esto soluciona el error común donde Windows intenta abrir la Microsoft Store en lugar de usar un Python real.
*   **Motor de Iconos Avanzado**:
    *   Soporte para extraer iconos directamente de archivos `.exe`.
    *   Icono profesional embebido para la aplicación principal.
    *   Mejorado el soporte para archivos `.ico` personalizados al generar trackers.
*   **Seguridad y Estabilidad**:
    *   Corregido un error crítico que causaba la apertura recursiva de ventanas ("pestañas infinitas") al ejecutarse como un `.exe` compilado.
    *   Separada la lógica de la interfaz de usuario del entorno de compilación de PyInstaller.
*   **Interfaz Moderna (UI/UX)**:
    *   Interfaz actualizada con una estética "Premium Dark Mode".
    *   Mensajes y diálogos rediseñados para ser más amigables para usuarios normales (no técnicos).
*   **Generación de Trackers Robusta**:
    *   **Error de Tkinter Solucionado**: Implementado un modo de "Compilación Agresiva" (`--collect-all`) para asegurar que los trackers generados incluyan siempre la interfaz gráfica, eliminando el fallo "No module named tkinter".
    *   **Validación Proactiva**: La app ahora comprueba si el Python detectado soporta interfaces antes de iniciar la creación del archivo.
*   **Configuración Profesional del Proyecto**:
    *   Configurado un archivo `.gitignore` profesional para mantener el repositorio limpio de archivos temporales de compilación y subproductos del entorno.
