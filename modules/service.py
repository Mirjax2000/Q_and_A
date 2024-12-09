"""Service module"""

from pyclbr import Function
from typing import TypeAlias
import customtkinter as ctk

Label: TypeAlias = ctk.CTkLabel
Entry: TypeAlias = ctk.CTkEntry
Btn: TypeAlias = ctk.CTkButton
Frame: TypeAlias = ctk.CTkFrame
Dnn: TypeAlias = dict | None

font_lbl: tuple = ("Helvetica", 20)
font_btn: tuple = ("Helvetica", 18)
font_entr: tuple = ("Segoe UI", 18)


def ctk_init(self, name: str, app_width: int, app_height: int):
    """App init"""
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
    label: Label = Label(parent, font=font_lbl, **label_args)
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


if __name__ == "__main__":
    pass
