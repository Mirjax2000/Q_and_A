"""main module"""

import json
from typing import TypeAlias
from tkinter import filedialog
import customtkinter as ctk
from icecream import ic
from modules.service import (
    ctk_init,
    mk_btn,
    mk_lbl,
    mk_txtbx,
    mk_frm,
    mk_radio,
    mk_optmnu,
)
from fronta import Fronta

Label: TypeAlias = ctk.CTkLabel
Entry: TypeAlias = ctk.CTkEntry
Btn: TypeAlias = ctk.CTkButton
Frame: TypeAlias = ctk.CTkFrame
Txtbx: TypeAlias = ctk.CTkTextbox
Radio: TypeAlias = ctk.CTkRadioButton
Optmnu: TypeAlias = ctk.CTkOptionMenu


class App(ctk.CTk):
    """Main App"""

    def __init__(self):
        super().__init__()
        ctk_init(self, "Q and A", 600, 600)
        self.columnconfigure((0, 1), weight=1, uniform="a")
        self.rowconfigure(4, weight=1, uniform="a")
        self.raw_data: dict = {}
        #
        self.load_info: Txtbx = mk_txtbx(
            self,
            {
                "border_color": "black",
                "border_spacing": 5,
                "height": 100,
            },
            {
                "row": 0,
                "column": 0,
                "columnspan": 3,
                "pady": (10, 0),
                "padx": 25,
            },
        )
        self.info_printer("Nahraj otazky!")
        #
        self.option_menu: Optmnu = mk_optmnu(
            self,
            {"state": "disabled"},
            {
                "row": 1,
                "column": 0,
                "columnspan": 2,
                "pady": 10,
                "padx": 25,
            },
        )
        # btns
        self.load_btn: Btn = mk_btn(
            self,
            {
                "text": "Nahrat otazky",
                "command": lambda: self.load_data(self.load_dialog()),
            },
            {"row": 2, "column": 0, "pady": 10, "padx": (25, 0)},
        )

        self.delete_btn: Btn = mk_btn(
            self,
            {
                "text": "smazat otazky",
                "state": "disabled",
                "command": self.clear_data,
            },
            {"row": 2, "column": 1, "pady": 10, "padx": 25},
        )
        self.exit_btn: Btn = mk_btn(
            self,
            {"text": "exit", "command": self.exit},
            {"row": 10, "column": 2, "pady": 10, "padx": 25},
        )
        self.run_btn: Btn = mk_btn(
            self,
            {
                "text": "spustit test",
                "state": "disabled",
                "command": lambda: self.activate_widgets(
                    self.widget_list
                ),
            },
            {
                "row": 2,
                "column": 2,
                "pady": 10,
                "padx": (0, 25),
            },
        )
        #
        self.test_frm: Frame = mk_frm(
            self, {}, {"row": 4, "column": 0, "columnspan": 3}
        )
        self.test_frm.columnconfigure(0, weight=1, uniform="a")

        self.title_lbl: Label = mk_lbl(
            self.test_frm,
            {"text": "Otazka: ", "anchor": "w", "justify": "left"},
            {"row": 0, "column": 0, "pady": 20, "padx": 20},
        )
        self.title_lbl.configure(font=("Helvetica", 30))

        self.radio_var = ctk.StringVar(value="")

        self.radio_1: Radio = mk_radio(
            self.test_frm,
            {
                "text": "moznost 1",
                "value": False,
                "variable": self.radio_var,
                "command": self.vyhodnot,
            },
            {"row": 1, "column": 0, "pady": 20, "padx": 25},
        )
        self.radio_2: Radio = mk_radio(
            self.test_frm,
            {
                "text": "moznost 2",
                "value": True,
                "variable": self.radio_var,
                "command": self.vyhodnot,
            },
            {"row": 2, "column": 0, "pady": 20, "padx": 25},
        )
        self.radio_3: Radio = mk_radio(
            self.test_frm,
            {
                "text": "moznost 3",
                "value": False,
                "variable": self.radio_var,
                "command": self.vyhodnot,
            },
            {"row": 3, "column": 0, "pady": 20, "padx": 25},
        )
        self.radio_4: Radio = mk_radio(
            self.test_frm,
            {
                "text": "moznost 4",
                "value": False,
                "variable": self.radio_var,
                "command": self.vyhodnot,
            },
            {"row": 4, "column": 0, "pady": 20, "padx": 25},
        )

        self.next_btn: Btn = mk_btn(
            self.test_frm,
            {
                "text": "dalsi",
                "state": "disabled",
                "command": self.next,
            },
            {
                "row": 5,
                "column": 0,
                "pady": 20,
                "padx": 25,
            },
            sticky="e",
        )
        self.widget_list: list = [
            self.next_btn,
            self.radio_1,
            self.radio_2,
            self.radio_3,
            self.radio_4,
            self.title_lbl,
        ]
        self.deactivate_widgets(self.widget_list)
        self.update_idletasks()

    # methods
    def next(self) -> None:
        """Next btn"""
        # fronta deque.
        self.deactivate_widgets(self.widget_list)

    def right_answer(self) -> bool:
        """spravna odpoved"""
        if self.radio_var.get() == "1":
            return True
        return False

    def vyhodnot(self) -> None:
        """vyhodnot"""
        if self.right_answer():
            self.next_btn.configure(state="normal")
        ic(self.radio_var.get())

    def deactivate_widgets(self, widgets_list: list) -> None:
        """Deactivuje widgety"""
        for item in widgets_list:
            item.grid_remove()

    def activate_widgets(self, widgets_list: list) -> None:
        """Activuj widgety"""
        for item in widgets_list:
            item.grid()

    def info_printer(self, text: str, color: str = "#00ff33") -> None:
        """Texto do load_info widgetu"""
        self.load_info.configure(state="normal", text_color=color)
        self.load_info.delete("0.0", "end")
        self.load_info.insert("0.0", text)
        self.load_info.configure(state="disabled")

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
            self.raw_data = data
        if self.raw_data:
            self.info_printer("Data nahrana, jeeeej!")
            self.delete_btn.configure(state="normal")
            self.run_btn.configure(state="normal")
            self.load_btn.configure(state="disabled")

    def clear_data(self) -> None:
        """Clear data and load_info Txtbx"""
        self.raw_data.clear()
        self.info_printer("Nahraj otazky!")
        self.delete_btn.configure(state="disabled")
        self.run_btn.configure(state="disabled")
        self.deactivate_widgets(self.widget_list)
        self.load_btn.configure(state="normal")

    def exit(self) -> None:
        """Terminate"""
        self.destroy()


if __name__ == "__main__":
    app: App = App()
    app.mainloop()
