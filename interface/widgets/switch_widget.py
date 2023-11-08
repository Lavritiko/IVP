import tkinter
from typing import Callable, Optional, Tuple, Union, Any
from  customtkinter import *
from customtkinter.windows.widgets.font import CTkFont

class MySwitch(CTkSwitch):
    def __init__(self, master: any,
                 width: int = 150, height: int = 30,
                 switch_width: int = 36, switch_height: int = 18,
                 corner_radius: int | None = None,
                 border_width: int | None = None, button_length: int | None = None,
                 bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None,
                 border_color: str | Tuple[str, str] = "transparent", progress_color: str | Tuple[str, str] | None = None,
                 button_color: str | Tuple[str, str] | None = None, button_hover_color: str | Tuple[str, str] | None = None, 
                 text_color: str | Tuple[str, str] | None = None, text_color_disabled: str | Tuple[str, str] | None = None,
                 text: str = "CTkSwitch",
                 font: tuple | CTkFont | None = None,
                 textvariable: Variable | None = None,
                 onvalue: int | str = 1, offvalue: int | str = 0,
                 variable: Variable | None = None,
                 hover: bool = True, command: Callable[..., Any] | None = None,
                 state: str = tkinter.NORMAL, **kwargs):
        super().__init__(master,
                         width,
                         height,
                         switch_width,
                         switch_height,
                         corner_radius,
                         border_width,
                         button_length,
                         bg_color,
                         fg_color,
                         border_color,
                         progress_color,
                         button_color,
                         button_hover_color,
                         text_color,
                         text_color_disabled,
                         text, font, textvariable,
                         onvalue, offvalue, variable,
                         hover, command, state, **kwargs)