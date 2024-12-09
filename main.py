"""main module"""

import json
from tkinter import filedialog
import customtkinter as ctk
from icecream import ic
from modules.service import ctk_init, mk_btn, mk_tb


class App(ctk.CTk):
    """Main App"""

    def __init__(self):
        super().__init__()
        ctk_init(self, "Q and A", 400, 600)
        self.columnconfigure((0, 1), weight=1, uniform="a")
        self.data: dict = {}
        # btns
        self.load_btn = mk_btn(
            self,
            {
                "text": "Nahrat otazky",
                "command": lambda: self.load_data(self.load_dialog()),
            },
            {"row": 0, "column": 0, "pady": 5, "padx": 5},
        )
        self.exit_btn = mk_btn(
            self,
            {"text": "exit", "command": self.exit},
            {"row": 10, "column": 1, "pady": 5, "padx": 5},
        )

        self.load_info = mk_tb(
            self,
            {
                "text_color": "#00ff33",
                "border_color": "black",
                "border_spacing": 5,
            },
            {
                "row": 1,
                "column": 0,
                "columnspan": 2,
                "pady": 5,
                "padx": 5,
            },
        )
        self.load_info.insert(
            "0.0",
            "Nahraj otazky!",
        )

    # methods
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

    def load_data(self, entry_file: str) -> None:
        """Load data"""
        with open(entry_file, "r", encoding="utf-8") as file:
            data: dict = json.load(file)
            self.data.update(data)

    def exit(self) -> None:
        """Terminate"""
        self.destroy()


if __name__ == "__main__":
    app: App = App()
    app.mainloop()
