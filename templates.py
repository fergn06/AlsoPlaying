WIDGET_TEMPLATE = """
import tkinter as tk
import os
import sys
import time
import base64
import tempfile

GAME_NAME = "{{GAME_NAME}}"
PLATFORM = "{{PLATFORM}}"
ICON_B64 = "{{ICON_B64}}"
CLOSE_TEXT = "{{CLOSE_TEXT}}"

def handle_exception(exc_type, exc_value, exc_traceback):
    from tkinter import messagebox
    messagebox.showerror("Error", f"An unexpected error occurred: {exc_value}")

class GameTrackerWidget:
    def __init__(self):
        self.root = tk.Tk()
        # Global exception handler
        self.root.report_callback_exception = handle_exception
        self.root.title(f"{GAME_NAME} - {PLATFORM}")
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.configure(bg="#1a1a2e")
        self.root.resizable(False, False)

        # Apply icon if available
        if ICON_B64:
            try:
                icon_data = base64.b64decode(ICON_B64)
                tmp_icon = os.path.join(tempfile.gettempdir(), "gt_icon.png")
                with open(tmp_icon, "wb") as f:
                    f.write(icon_data)
                img = tk.PhotoImage(file=tmp_icon)
                self.root.iconphoto(True, img)
            except Exception:
                pass

        win_w, win_h = 260, 120
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x  = sw - win_w - 20
        y  = sh - win_h - 60
        self.root.geometry(f"{win_w}x{win_h}+{x}+{y}")

        self.root.bind("<ButtonPress-1>", self._drag_start)
        self.root.bind("<B1-Motion>",     self._drag_move)

        outer = tk.Frame(self.root, bg="#e94560", padx=2, pady=2)
        outer.pack(fill="both", expand=True)
        inner = tk.Frame(outer, bg="#1a1a2e", padx=12, pady=8)
        inner.pack(fill="both", expand=True)

        tk.Label(inner, text=GAME_NAME,
                 font=("Segoe UI", 11, "bold"),
                 fg="#ffffff", bg="#1a1a2e").pack(fill="x")

        tk.Label(inner, text=PLATFORM,
                 font=("Segoe UI", 8),
                 fg="#aaaacc", bg="#1a1a2e").pack(fill="x")

        self.time_lbl = tk.Label(inner, text="00:00:00",
                                  font=("Consolas", 14, "bold"),
                                  fg="#e94560", bg="#1a1a2e")
        self.time_lbl.pack(fill="x", pady=(2, 0))

        tk.Button(inner, text=CLOSE_TEXT,
                  font=("Segoe UI", 8, "bold"),
                  fg="#ffffff", bg="#e94560",
                  activebackground="#c73652", activeforeground="#ffffff",
                  relief="flat", cursor="hand2",
                  pady=5,
                  command=self.root.destroy).pack(fill="x", pady=(8, 0))

        self.start_time = time.time()
        self._tick()

    def _drag_start(self, e):
        self._ox, self._oy = e.x, e.y

    def _drag_move(self, e):
        x = self.root.winfo_x() + e.x - self._ox
        y = self.root.winfo_y() + e.y - self._oy
        self.root.geometry(f"+{x}+{y}")

    def _tick(self):
        elapsed = int(time.time() - self.start_time)
        h, rem  = divmod(elapsed, 3600)
        m, s    = divmod(rem, 60)
        self.time_lbl.config(text=f"{h:02d}:{m:02d}:{s:02d}")
        self.root.after(1000, self._tick)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    GameTrackerWidget().run()
"""
