"""Service module"""

from typing import TypeAlias
import customtkinter as ctk

Label: TypeAlias = ctk.CTkLabel
Entry: TypeAlias = ctk.CTkEntry
Btn: TypeAlias = ctk.CTkButton
Frame: TypeAlias = ctk.CTkFrame
Txtbx: TypeAlias = ctk.CTkTextbox
Radio: TypeAlias = ctk.CTkRadioButton
Optmnu: TypeAlias = ctk.CTkOptionMenu
Dnn: TypeAlias = dict | None

font_lbl: tuple = ("Helvetica", 20)
font_btn: tuple = ("Helvetica", 18)
font_entr: tuple = ("Segoe UI", 18)
font_txtbx: tuple = ("Consolas", 18)
font_radio: tuple = ("Helvetica", 18)


def ctk_init(self, name: str, app_width: int, app_height: int):
    """App init"""
    ctk.set_appearance_mode("dark")
    ctk.set_widget_scaling(1)  # widget dimensions and text size
    ctk.set_window_scaling(1)
    self.update_idletasks()
    self.title(f"{name}")
    self.minsize(app_width, app_height)
    self.resizable(False, False)
    width: int = app_width
    height: int = app_height
    screen_width: int = self.winfo_screenwidth()
    screen_height: int = self.winfo_screenheight()
    x: int = screen_width // 2 - width // 2
    y: int = screen_height // 2 - height // 2
    self.geometry(f"{width}x{height}+{x}+{y}")


def mk_frm(
    parent,
    frame_args: Dnn = None,
    grid_args: Dnn = None,
    sticky: str = "nsew",
) -> Frame:
    """Make Frame"""
    frame_args = frame_args or {}
    grid_args = grid_args or {}
    frame: Frame = Frame(parent, corner_radius=4, **frame_args)
    frame.grid(sticky=sticky, **grid_args)
    return frame


def mk_lbl(
    parent,
    label_args: Dnn = None,
    grid_args: Dnn = None,
    sticky: str = "nsew",
) -> Label:
    """Make Label"""
    label_args = label_args or {}
    grid_args = grid_args or {}
    label: Label = Label(
        parent, font=font_lbl, corner_radius=4, **label_args
    )
    label.grid(sticky=sticky, **grid_args)
    return label


def mk_entr(
    parent,
    entry_args: Dnn = None,
    grid_args: Dnn = None,
    sticky: str = "nsew",
) -> Entry:
    """Make Entry"""
    entry_args = entry_args or {}
    grid_args = grid_args or {}
    entry: Entry = Entry(parent, font=font_entr, **entry_args)
    entry.grid(sticky=sticky, **grid_args)
    return entry


def mk_btn(
    parent,
    btn_args: Dnn = None,
    grid_args: Dnn = None,
    sticky: str = "nsew",
) -> Btn:
    """make btn"""
    btn_args = btn_args or {}
    grid_args = grid_args or {}
    btn: Btn = Btn(parent, font=font_btn, **btn_args)
    btn.grid(sticky=sticky, **grid_args)
    return btn


def mk_txtbx(
    parent,
    txtbx_args: Dnn = None,
    grid_args: Dnn = None,
    sticky: str = "nsew",
) -> Txtbx:
    """make btn"""
    txtbx_args = txtbx_args or {}
    grid_args = grid_args or {}
    txtbx: Txtbx = Txtbx(parent, font=font_txtbx, **txtbx_args)
    txtbx.grid(sticky=sticky, **grid_args)
    return txtbx


def mk_radio(
    parent, radio_args: Dnn, grid_args: Dnn, sticky: str = "nsew"
) -> Radio:
    """Make radio button"""
    radio_args = radio_args or {}
    grid_args = grid_args or {}
    radio: Radio = Radio(parent, font=font_radio, **radio_args)
    radio.grid(sticky=sticky, **grid_args)
    return radio


def mk_optmnu(
    parent, optmnu_args: Dnn, grid_args: Dnn, sticky: str = "nsew"
) -> Optmnu:
    """Make option menu"""
    optmnu_args = optmnu_args or {}
    grid_args = grid_args or {}
    optmnu: Optmnu = Optmnu(parent, font=font_lbl, **optmnu_args)
    optmnu.grid(sticky=sticky, **grid_args)
    return optmnu


if __name__ == "__main__":
    pass
