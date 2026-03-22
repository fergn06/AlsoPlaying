import tkinter as tk
from tkinter import messagebox, filedialog
import subprocess
import os
import sys
import threading
import shutil
import tempfile
import base64
import time

# Módulos personalizados
from localization import _t, current_lang
from resources import DEFAULT_ICON_B64, MAIN_ICON_B64
from templates import WIDGET_TEMPLATE

# ══════════════════════════════════════════════════════════════════════════════
#  MANEJADOR GLOBAL DE EXCEPCIONES
# ══════════════════════════════════════════════════════════════════════════════
def handle_exception(exc_type, exc_value, exc_traceback):
    """Muestra un mensaje de error legible en lugar de cerrar la app en silencio."""
    import traceback
    error_details = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    print(error_details)  # Para debugging por consola
    messagebox.showerror(_t("fatal_error"), _t("unexpected_error", str(exc_value)))

# ══════════════════════════════════════════════════════════════════════════════
#  ESTILOS
# ══════════════════════════════════════════════════════════════════════════════
BG       = "#1a1a2e"
ACCENT   = "#e94560"
FG       = "#ffffff"
FG_DIM   = "#aaaacc"
ENTRY_BG = "#16213e"
HOVER    = "#c73652"
DEFAULT_OUT_DIR = os.path.join(os.path.expanduser("~"), "Desktop")

# ══════════════════════════════════════════════════════════════════════════════
#  APP CREADORA
# ══════════════════════════════════════════════════════════════════════════════
class CreatorApp:
    def __init__(self):
        self.root = tk.Tk()
        # Global exception handler
        self.root.report_callback_exception = handle_exception
        self.root.title("AlsoPlaying")
        self.root.configure(bg=BG)
        self.root.resizable(False, False)

        self.custom_icon_path: str | None = None
        self.python_path: str | None = None
        self.name_var = tk.StringVar()
        self.plat_var = tk.StringVar()
        self.icon_mode = tk.StringVar(value="default")
        self.out_dir_var = tk.StringVar(value=DEFAULT_OUT_DIR)
        
        self.icon_file_row: tk.Frame | None = None
        self.icon_path_var = tk.StringVar(value=_t("no_file"))
        self.gen_btn: tk.Button | None = None
        self.status_var = tk.StringVar()
        self.status_lbl: tk.Label | None = None

        w, h = 420, 560
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        self.root.geometry(f"{w}x{h}+{(sw-w)//2}+{(sh-h)//2}")

        self._build_ui()

    def _build_ui(self):
        # Apply default icon to creator window
        try:
            _ico = os.path.join(tempfile.gettempdir(), "alsoplaying.ico")
            if not os.path.exists(_ico):
                with open(_ico, "wb") as _f:
                    _f.write(base64.b64decode(MAIN_ICON_B64))
            self.root.iconbitmap(_ico)
        except Exception:
            pass

        tk.Frame(self.root, bg=ACCENT, height=5).pack(fill="x")

        tk.Label(self.root, text=_t("title"),
                 font=("Segoe UI", 14, "bold"), fg=FG, bg=BG).pack(pady=(18, 2))
        tk.Label(self.root, text=_t("subtitle"),
                 font=("Segoe UI", 9), fg=FG_DIM, bg=BG).pack(pady=(0, 18))

        form = tk.Frame(self.root, bg=BG)
        form.pack(padx=40, fill="x")

        # Game name
        tk.Label(form, text=_t("game_name"),
                 font=("Segoe UI", 9, "bold"), fg=FG_DIM, bg=BG, anchor="w").pack(fill="x")
        tk.Entry(form, textvariable=self.name_var,
                 font=("Segoe UI", 11), bg=ENTRY_BG, fg=FG,
                 insertbackground=FG, relief="flat", bd=6).pack(fill="x", pady=(2, 12), ipady=5)

        # Platform
        tk.Label(form, text=_t("platform"),
                 font=("Segoe UI", 9, "bold"), fg=FG_DIM, bg=BG, anchor="w").pack(fill="x")
        tk.Entry(form, textvariable=self.plat_var,
                 font=("Segoe UI", 11), bg=ENTRY_BG, fg=FG,
                 insertbackground=FG, relief="flat", bd=6).pack(fill="x", pady=(2, 0), ipady=5)
        tk.Label(form, text=_t("platform_ex"),
                 font=("Segoe UI", 8), fg=FG_DIM, bg=BG, anchor="w").pack(fill="x", pady=(2, 16))

        # ── Output folder section ─────────────────────────────────────────────
        tk.Label(form, text=_t("output_folder"),
                 font=("Segoe UI", 9, "bold"), fg=FG_DIM, bg=BG, anchor="w").pack(fill="x")
        out_row = tk.Frame(form, bg=BG)
        out_row.pack(fill="x", pady=(4, 16))
        
        tk.Label(out_row, textvariable=self.out_dir_var,
                 font=("Segoe UI", 8), fg=FG_DIM, bg=ENTRY_BG,
                 anchor="w", padx=6).pack(side="left", fill="x", expand=True, ipady=4)
        tk.Button(out_row, text="...",
                  font=("Segoe UI", 8, "bold"),
                  fg=FG, bg=ACCENT, activebackground=HOVER, activeforeground=FG,
                  relief="flat", cursor="hand2", padx=10,
                  command=self._pick_output_dir).pack(side="left", padx=(4, 0))

        # ── Icon section ─────────────────────────────────────────────────────
        tk.Label(form, text=_t("widget_icon"),
                 font=("Segoe UI", 9, "bold"), fg=FG_DIM, bg=BG, anchor="w").pack(fill="x")

        icon_row = tk.Frame(form, bg=BG)
        icon_row.pack(fill="x", pady=(4, 0))

        rb_default = tk.Radiobutton(
            icon_row, text=_t("default"), variable=self.icon_mode,
            value="default", font=("Segoe UI", 9),
            fg=FG, bg=BG, selectcolor=ENTRY_BG,
            activebackground=BG, activeforeground=FG,
            command=self._on_icon_mode)
        rb_default.pack(side="left")

        rb_custom = tk.Radiobutton(
            icon_row, text=_t("custom"), variable=self.icon_mode,
            value="custom", font=("Segoe UI", 9),
            fg=FG, bg=BG, selectcolor=ENTRY_BG,
            activebackground=BG, activeforeground=FG,
            command=self._on_icon_mode)
        rb_custom.pack(side="left", padx=(16, 0))

        self.icon_file_row = tk.Frame(form, bg=BG)
        tk.Label(
            self.icon_file_row, textvariable=self.icon_path_var,
            font=("Segoe UI", 8), fg=FG_DIM, bg=ENTRY_BG,
            anchor="w", padx=6).pack(side="left", fill="x", expand=True, ipady=4)

        tk.Button(
            self.icon_file_row, text=_t("browse"),
            font=("Segoe UI", 8, "bold"),
            fg=FG, bg=ACCENT, activebackground=HOVER, activeforeground=FG,
            relief="flat", cursor="hand2", padx=8,
            command=self._pick_icon).pack(side="left", padx=(4, 0))

        # ── Generate button ───────────────────────────────────────────────────
        self.gen_btn = tk.Button(
            form, text=_t("generate"),
            font=("Segoe UI", 11, "bold"),
            fg=FG, bg=ACCENT, activebackground=HOVER, activeforeground=FG,
            relief="flat", cursor="hand2",
            command=self._on_generate, pady=12)
        self.gen_btn.pack(fill="x", pady=(20, 0))

        # Info button
        info_btn = tk.Button(
            self.root, text="ℹ",
            font=("Segoe UI", 8, "bold"),
            fg=FG_DIM, bg=BG,
            activebackground=BG, activeforeground=FG,
            relief="flat", cursor="hand2", bd=0,
            command=self._show_info)
        info_btn.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

        self.status_lbl = tk.Label(self.root, textvariable=self.status_var,
                                    font=("Segoe UI", 9), fg=FG_DIM, bg=BG)
        self.status_lbl.pack(pady=(10, 30))

    def _on_icon_mode(self):
        if self.icon_mode.get() == "custom":
            self.icon_file_row.pack(fill="x", pady=(6, 0), before=self.gen_btn)
        else:
            self.icon_file_row.pack_forget()
            self.custom_icon_path = None
            self.icon_path_var.set(_t("no_file"))

    def _pick_icon(self):
        path = filedialog.askopenfilename(
            title=_t("select_icon"),
            filetypes=[(_t("ico_files"), "*.ico")])
        if path:
            self.custom_icon_path = path
            self.icon_path_var.set(os.path.basename(path))

    def _pick_output_dir(self):
        path = filedialog.askdirectory(title=_t("select_folder"))
        if path:
            self.out_dir_var.set(os.path.normpath(path))

    def _on_generate(self):
        game = self.name_var.get().strip()
        plat = self.plat_var.get().strip()
        out_dir = self.out_dir_var.get().strip()

        if not game or not plat or not out_dir:
            messagebox.showwarning(_t("missing_data_title"), _t("missing_data_msg"))
            return

        if self.icon_mode.get() == "custom" and not self.custom_icon_path:
            messagebox.showwarning(_t("no_icon_title"), _t("no_icon_msg"))
            return

        self.gen_btn.config(state="disabled")
        self._set_status(_t("compiling"))

        threading.Thread(target=self._build_exe,
                         args=(game, plat, out_dir), daemon=True).start()

    def _build_exe(self, game: str, plat: str, out_dir: str):
        tmp_dir = tempfile.mkdtemp(prefix="gtracker_")
        try:
            if self.icon_mode.get() == "custom" and self.custom_icon_path:
                with open(self.custom_icon_path, "rb") as f:
                    icon_b64 = base64.b64encode(f.read()).decode("utf-8")
                icon_ext = os.path.splitext(self.custom_icon_path)[1].lower()
                icon_file = self.custom_icon_path
            else:
                icon_b64 = DEFAULT_ICON_B64
                icon_ext = ".ico"
                ico_tmp = os.path.join(tmp_dir, "default.ico")
                with open(ico_tmp, "wb") as _f:
                    _f.write(base64.b64decode(DEFAULT_ICON_B64))
                icon_file = ico_tmp

            code = (
                WIDGET_TEMPLATE
                .replace("{{GAME_NAME}}", game.replace('"', '\\"'))
                .replace("{{PLATFORM}}",  plat.replace('"', '\\"'))
                .replace("{{ICON_B64}}",  icon_b64)
                .replace("{{CLOSE_TEXT}}", _t("close"))
            )

            script = os.path.join(tmp_dir, "tracker_tmp.py")
            with open(script, "w", encoding="utf-8") as f:
                f.write(code)

            def safe(s):
                return "".join(c for c in s if c.isalnum() or c in " _-").strip()
            exe_name = f"{safe(game)} - {safe(plat)}"

            # Robust Python path
            python_exe = getattr(self, "python_path", None)
            if not python_exe or not os.path.exists(python_exe):
                python_exe = sys.executable
            
            cmd = [
                python_exe, "-m", "PyInstaller",
                "--onefile", "--noconsole",
                f"--name={exe_name}",
                f"--distpath={tmp_dir}",
                f"--workpath={os.path.join(tmp_dir, 'build')}",
                f"--specpath={tmp_dir}",
            ]

            if icon_file and icon_ext == ".ico":
                cmd.append(f"--icon={icon_file}")

            cmd.append(script)

            creation_flags = 0x08000000 if sys.platform == "win32" else 0
            result = subprocess.run(cmd, capture_output=True, text=True,
                                    creationflags=creation_flags)

            if result.returncode != 0:
                raise RuntimeError(result.stderr[-800:] or result.stdout[-800:])

            built = os.path.join(tmp_dir, exe_name + ".exe")
            if not os.path.exists(built):
                raise FileNotFoundError(f"PyInstaller failed to create: {built}")

            if not os.path.exists(out_dir):
                os.makedirs(out_dir, exist_ok=True)
                
            dest = os.path.join(out_dir, exe_name + ".exe")
            shutil.move(built, dest)

            shutil.rmtree(tmp_dir, ignore_errors=True)
            self.root.after(0, self._on_success, dest)

        except Exception as e:
            shutil.rmtree(tmp_dir, ignore_errors=True)
            self.root.after(0, self._on_error, str(e))

    def _on_success(self, dest: str):
        self.gen_btn.config(state="normal")
        self._set_status(_t("success_status"), color="#4caf50")
        messagebox.showinfo(_t("success_title"), _t("success_msg", dest))

    def _on_error(self, err: str):
        self.gen_btn.config(state="normal")
        self._set_status(_t("error_status"), color=ACCENT)
        messagebox.showerror(_t("error_title"), _t("error_msg", err))

    def _show_info(self):
        messagebox.showinfo(_t("info_title"), _t("info_msg"))

    def _set_status(self, msg: str, color: str = FG_DIM):
        self.status_var.set(msg)
        self.status_lbl.config(fg=color)

    def run(self):
        self.root.mainloop()

# ══════════════════════════════════════════════════════════════════════════════
#  COMPROBACIONES DE ENTORNO
# ══════════════════════════════════════════════════════════════════════════════
def _apply_main_icon(window):
    try:
        _ico = os.path.join(tempfile.gettempdir(), "alsoplaying_main.ico")
        if not os.path.exists(_ico):
            with open(_ico, "wb") as _f:
                _f.write(base64.b64decode(MAIN_ICON_B64))
        window.iconbitmap(_ico)
    except Exception:
        pass

def check_environment():
    import subprocess, winreg, glob, webbrowser

    def find_python():
        # Primero intentar sys.executable si es un python.exe real
        if sys.executable.lower().endswith("python.exe") and "venv" not in sys.executable:
             return sys.executable, "detected"

        for _root in (winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CURRENT_USER):
            try:
                k  = winreg.OpenKey(_root, r"SOFTWARE\Python\PythonCore")
                ver = winreg.EnumKey(k, 0)
                pk = winreg.OpenKey(k, ver + r"\InstallPath")
                path = winreg.QueryValueEx(pk, "ExecutablePath")[0]
                if os.path.exists(path) and "WindowsApps" not in path:
                    return path, ver
            except Exception:
                pass
        for pat in [
            r"C:\Python3*\python.exe",
            r"C:\Users\*\AppData\Local\Programs\Python\Python3*\python.exe",
        ]:
            hits = glob.glob(pat)
            if hits:
                p = hits[-1]
                ver = os.path.basename(os.path.dirname(p)).replace("Python", "")
                return p, ver
        return None, None

    python_path, python_ver = find_python()

    def install_python_auto():
        import tkinter as _tk
        from tkinter import messagebox as _mb
        _r = _tk.Tk(); _r.withdraw()
        _apply_main_icon(_r)
        
        resp = _mb.askyesno(_t("python_install_offer_title"), _t("python_install_offer_msg"))
        if resp:
            _r2 = _tk.Tk()
            _r2.title(_t("python_installing_title"))
            _r2.configure(bg="#1a1a2e")
            _r2.geometry("360x100")
            _tk.Label(_r2, text=_t("python_installing_msg"),
                      font=("Segoe UI", 10), fg="#ffffff", bg="#1a1a2e").pack(pady=20)
            _r2.update()
            _apply_main_icon(_r2)
            _r2.update()

            try:
                creation_flags = 0x08000000 if sys.platform == "win32" else 0
                install = subprocess.run(
                    ["winget", "install", "Python.Python.3.13", "--silent", "--accept-package-agreements", "--accept-source-agreements"],
                    capture_output=True, text=True, creationflags=creation_flags
                )
                _r2.destroy()
                if install.returncode == 0:
                    _mb.showinfo(_t("python_install_success_title"), _t("python_install_success_msg"))
                    sys.exit(0)
                else:
                    _mb.showerror(_t("python_install_error_title"), _t("python_install_error_msg", install.stderr[-400:] or install.stdout[-400:]))
            except Exception as e:
                _r2.destroy()
                _mb.showerror(_t("python_install_error_title"), _t("python_install_error_msg", str(e)))
        else:
             _mb.showinfo(_t("instructions_title"), _t("instructions_msg"))
        _r.destroy()
        sys.exit(0)

    if not python_path:
        install_python_auto()

    try:
        result = subprocess.run(
            [python_path, "--version"],
            capture_output=True, text=True
        )
        ver_str = result.stdout.strip() or result.stderr.strip()
        parts = ver_str.replace("Python", "").strip().split(".")
        major, minor = int(parts[0]), int(parts[1])
        if (major, minor) < (3, 11): # Bajamos a 3.11 por compatibilidad si ya tiene uno
            pass 
        elif (major, minor) < (3, 11):
            install_python_auto()
    except Exception:
        pass

    try:
        result = subprocess.run(
            [python_path, "-m", "PyInstaller", "--version"],
            capture_output=True, text=True,
            creationflags=0x08000000
        )
        pyinstaller_ok = result.returncode == 0
    except Exception:
        pyinstaller_ok = False

    if not pyinstaller_ok:
        import tkinter as _tk
        from tkinter import messagebox as _mb
        _r = _tk.Tk(); _r.withdraw()
        _apply_main_icon(_r)
        resp = _mb.askyesno(
            _t("missing_dep_title"),
            _t("missing_dep_msg"),
            icon="question"
        )
        if resp:
            _r2 = _tk.Tk()
            _r2.title(_t("installing_title"))
            _r2.configure(bg="#1a1a2e")
            _r2.geometry("360x100")
            _r2.resizable(False, False)
            _r2.attributes("-topmost", True)
            _tk.Label(_r2, text=_t("installing_msg"),
                      font=("Segoe UI", 10), fg="#ffffff", bg="#1a1a2e").pack(pady=20)
            _r2.update()
            _apply_main_icon(_r2)
            _r2.update()

            install = subprocess.run(
                [python_path, "-m", "pip", "install", "pyinstaller"],
                capture_output=True, text=True,
                creationflags=0x08000000
            )
            _r2.destroy()

            if install.returncode == 0:
                _mb.showinfo(_t("success_title"), _t("install_success_msg"))
            else:
                _mb.showerror(_t("install_error_title"), _t("install_error_msg", install.stderr[-400:]))
                _r.destroy()
                sys.exit(0)
        else:
            _mb.showwarning(_t("warning_title"), _t("warning_msg"))
        _r.destroy()

    return python_path


if __name__ == "__main__":
    python_path = check_environment()
    app = CreatorApp()
    app.python_path = python_path
    app.run()
