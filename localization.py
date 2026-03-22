import sys
import locale

LOCALIZATION = {
    "en": {
        "title": "AlsoPlaying",
        "subtitle": "Play everything. Share everything.",
        "game_name": "Game name",
        "platform": "Platform",
        "platform_ex": "e.g. PS5, Switch, Xbox, PC…",
        "widget_icon": "Widget icon",
        "default": "Default",
        "custom": "Custom",
        "no_file": "No file selected",
        "browse": "Browse…",
        "generate": "⚡  GENERATE .EXE",
        "compiling": "Compiling… this may take a minute ⏳",
        "success_status": "✅  .exe generated on the Desktop",
        "success_title": "Done!",
        "success_msg": "File generated:\n{}\n\nAdd it to Steam as a 'Non-Steam Game'.",
        "error_status": "❌  Generation error",
        "error_title": "Compilation error",
        "error_msg": "PyInstaller failed:\n\n{}\n\nInstall it with:\n  pip install pyinstaller",
        "missing_data_title": "Missing data",
        "missing_data_msg": "Please fill in the game name and platform.",
        "no_icon_title": "No icon",
        "no_icon_msg": "Please select an icon file or use the default one.",
        "select_icon": "Select an icon",
        "ico_files": "ICO Icons",
        "python_not_found_title": "Python not found",
        "python_not_found_msg": "AlsoPlaying requires Python 3.13 to generate .exe files.\n\nPython was not detected on this computer.\n\nWould you like to open the Python download page now?",
        "instructions_title": "Instructions",
        "instructions_msg": "Download and install Python 3.13 from python.org.\n\n⚠️ During installation, make sure to check:\n\"Add Python to PATH\"\n\nThen reopen AlsoPlaying.",
        "python_old_title": "Python version too old",
        "python_old_msg": "Python {} was found but AlsoPlaying requires Python 3.13 or higher.\n\nWould you like to open the download page?",
        "missing_dep_title": "Missing dependency",
        "missing_dep_msg": "PyInstaller is not installed. It is required to generate .exe files.\n\nWould you like to install it automatically now?",
        "installing_title": "Installing dependencies…",
        "installing_msg": "Installing PyInstaller, please wait…",
        "install_success_msg": "PyInstaller installed successfully.\nAlsoPlaying is ready to use.",
        "install_error_title": "Error",
        "install_error_msg": "Could not install PyInstaller:\n\n{}",
        "warning_title": "Warning",
        "warning_msg": "Without PyInstaller, .exe files cannot be generated.\nYou can install it manually with:\n  pip install pyinstaller",
        "close": "■  CLOSE",
        "output_folder": "Output folder",
        "select_folder": "Select folder",
        "info_title": "AlsoPlaying V1.0",

        "info_msg": "Created by Fernando Guerrero Nuez\n\nhttps://fernandoguerreronuez.com",
        "fatal_error": "Fatal Error",
        "unexpected_error": "An unexpected error occurred:\n\n{}",
        "python_install_offer_title": "Auto-install Python?",
        "python_install_offer_msg": "Python 3.13 is missing or too old. Would you like to install it automatically now using winget?",
        "python_installing_title": "Installing Python 3.13…",
        "python_installing_msg": "Downloading and installing Python, please wait…",
        "python_install_success_title": "Python Installed!",
        "python_install_success_msg": "Python 3.13 has been installed successfully. Please restart AlsoPlaying to apply changes.",
        "python_install_error_title": "Installation Error",
        "python_install_error_msg": "Could not install Python 3.13:\n\n{}"
    },
    "es": {
        "title": "AlsoPlaying",
        "subtitle": "Juega a todo. Compártelo todo.",
        "game_name": "Nombre del juego",
        "platform": "Plataforma",
        "platform_ex": "Ej: PS5, Switch, Xbox, PC…",
        "widget_icon": "Icono del widget",
        "default": "Predeterminado",
        "custom": "Personalizado",
        "no_file": "Ningún archivo seleccionado",
        "browse": "Buscar…",
        "generate": "⚡  GENERAR .EXE",
        "compiling": "Compilando… puede tardar un minuto ⏳",
        "success_status": "✅  .exe generado en el Escritorio",
        "success_title": "¡Listo!",
        "success_msg": "Archivo generado:\n{}\n\nAñádelo a Steam como 'Juego que no es de Steam'.",
        "error_status": "❌  Error al generar",
        "error_title": "Error al compilar",
        "error_msg": "PyInstaller falló:\n\n{}\n\nInstálalo con:\n  pip install pyinstaller",
        "missing_data_title": "Faltan datos",
        "missing_data_msg": "Rellena el nombre del juego y la plataforma.",
        "no_icon_title": "Sin icono",
        "no_icon_msg": "Selecciona un archivo de icono o usa el predeterminado.",
        "select_icon": "Selecciona un icono",
        "ico_files": "Iconos ICO",
        "python_not_found_title": "Python no encontrado",
        "python_not_found_msg": "AlsoPlaying necesita Python 3.13 para generar los .exe.\n\nNo se ha detectado Python en este equipo.\n\n¿Quieres abrir la página de descarga de Python ahora?",
        "instructions_title": "Instrucciones",
        "instructions_msg": "Descarga e instala Python 3.13 desde python.org.\n\n⚠️ Durante la instalación marca la opción:\n\"Add Python to PATH\"\n\nDespués vuelve a abrir AlsoPlaying.",
        "python_old_title": "Python desactualizado",
        "python_old_msg": "Se encontró Python {} pero AlsoPlaying necesita Python 3.13 o superior.\n\n¿Quieres abrir la página de descarga?",
        "missing_dep_title": "Dependencia faltante",
        "missing_dep_msg": "PyInstaller no está instalado. Es necesario para generar los .exe.\n\n¿Quieres instalarlo ahora automáticamente?",
        "installing_title": "Instalando dependencias…",
        "installing_msg": "Instalando PyInstaller, por favor espera…",
        "install_success_msg": "PyInstaller instalado correctamente.\nAlsoPlaying está listo para usar.",
        "install_error_title": "Error",
        "install_error_msg": "No se pudo instalar PyInstaller:\n\n{}",
        "warning_title": "Aviso",
        "warning_msg": "Sin PyInstaller no se pueden generar .exe.\nPuedes instalarlo manualmente con:\n  pip install pyinstaller",
        "close": "■  CERRAR",
        "output_folder": "Carpeta de destino",
        "select_folder": "Seleccionar carpeta",
        "info_title": "AlsoPlaying V1.0",

        "info_msg": "Creado por Fernando Guerrero Nuez\n\nhttps://fernandoguerreronuez.com",
        "fatal_error": "Error Fatal",
        "unexpected_error": "Ha ocurrido un error inesperado:\n\n{}",
        "python_install_offer_title": "¿Auto-instalar Python?",
        "python_install_offer_msg": "Python 3.13 falta o es muy antiguo. ¿Quieres instalarlo automáticamente ahora usando winget?",
        "python_installing_title": "Instalando Python 3.13…",
        "python_installing_msg": "Descargando e instalando Python, por favor espera…",
        "python_install_success_title": "¡Python instalado!",
        "python_install_success_msg": "Python 3.13 se ha instalado correctamente. Por favor, reinicia AlsoPlaying para aplicar los cambios.",
        "python_install_error_title": "Error de instalación",
        "python_install_error_msg": "No se pudo instalar Python 3.13:\n\n{}"
    }
}

# Detect system language
current_lang = "en"
try:
    if sys.platform == 'win32':
        import ctypes
        windll = ctypes.windll.kernel32
        sys_lang = locale.windows_locale.get(windll.GetUserDefaultUILanguage())
    else:
        sys_lang = locale.getdefaultlocale()[0]
    
    if sys_lang and sys_lang.startswith("es"):
        current_lang = "es"
except Exception:
    pass

def _t(key, *args):
    text = LOCALIZATION.get(current_lang, LOCALIZATION["en"]).get(key, key)
    if args:
        return text.format(*args)
    return text
