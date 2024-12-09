"""main module"""

import json
from tkinter import filedialog
from typing import Any
import customtkinter as ctk
from modules.service import ctk_init, mk_btn, mk_tb


class App(ctk.CTk):
    """Main App"""

    def __init__(self):
        super().__init__()
        ctk_init(self, "Q and A", 400, 600)

        self.load_btn = mk_btn(
            self,
            {
                "text": "Nahrat otazky",
                "command": lambda: self.load_data(self.load_dialog()),
            },
            {"row": 0, "column": 0, "pady": 5, "padx": 5},
        )

        self.load_info = mk_tb(
            self,
            {},
            {
                "row": 1,
                "column": 0,
                "columnspan": 2,
                "pady": 5,
                "padx": 5,
            },
        )

    def load_dialog(self) -> str:
        """Load dialog"""
        self.withdraw()
        adresar: str = "./testy"
        file_path: str = filedialog.askopenfilename(
            title="Vyberte soubor",
            initialdir=adresar,
            filetypes=(
                ("Json soubory", "*.json"),
                ("Všechny soubory", "*.*"),
            ),
        )
        self.deiconify()
        self.update_idletasks()
        return file_path

    def load_data(self, entry_file: str) -> dict:
        """Load data"""
        with open(entry_file, "r", encoding="utf-8") as file:
            data: dict = json.load(file)
        return data

    def exit(self) -> None:
        """Terminate"""
        self.destroy()


if __name__ == "__main__":
    app: App = App()
    app.mainloop()
