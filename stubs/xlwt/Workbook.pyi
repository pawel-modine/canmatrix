# Stubs for xlwt.Workbook (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from .Worksheet import Worksheet

class Workbook:
    encoding: Any = ...
    def __init__(self, encoding: str = ..., style_compression: int = ...) -> None: ...
    def get_style_stats(self): ...
    def set_owner(self, value: Any) -> None: ...
    def get_owner(self): ...
    owner: Any = ...
    def set_country_code(self, value: Any) -> None: ...
    def get_country_code(self): ...
    country_code: Any = ...
    def set_wnd_protect(self, value: Any) -> None: ...
    def get_wnd_protect(self): ...
    wnd_protect: Any = ...
    def set_obj_protect(self, value: Any) -> None: ...
    def get_obj_protect(self): ...
    obj_protect: Any = ...
    def set_protect(self, value: Any) -> None: ...
    def get_protect(self): ...
    protect: Any = ...
    def set_backup_on_save(self, value: Any) -> None: ...
    def get_backup_on_save(self): ...
    backup_on_save: Any = ...
    def set_hpos(self, value: Any) -> None: ...
    def get_hpos(self): ...
    hpos: Any = ...
    def set_vpos(self, value: Any) -> None: ...
    def get_vpos(self): ...
    vpos: Any = ...
    def set_width(self, value: Any) -> None: ...
    def get_width(self): ...
    width: Any = ...
    def set_height(self, value: Any) -> None: ...
    def get_height(self): ...
    height: Any = ...
    def set_active_sheet(self, value: Any) -> None: ...
    def get_active_sheet(self): ...
    active_sheet: Any = ...
    def set_tab_width(self, value: Any) -> None: ...
    def get_tab_width(self): ...
    tab_width: Any = ...
    def set_wnd_visible(self, value: Any) -> None: ...
    def get_wnd_visible(self): ...
    wnd_visible: Any = ...
    def set_wnd_mini(self, value: Any) -> None: ...
    def get_wnd_mini(self): ...
    wnd_mini: Any = ...
    def set_hscroll_visible(self, value: Any) -> None: ...
    def get_hscroll_visible(self): ...
    hscroll_visible: Any = ...
    def set_vscroll_visible(self, value: Any) -> None: ...
    def get_vscroll_visible(self): ...
    vscroll_visible: Any = ...
    def set_tabs_visible(self, value: Any) -> None: ...
    def get_tabs_visible(self): ...
    tabs_visible: Any = ...
    def set_dates_1904(self, value: Any) -> None: ...
    def get_dates_1904(self): ...
    dates_1904: Any = ...
    def set_use_cell_values(self, value: Any) -> None: ...
    def get_use_cell_values(self): ...
    use_cell_values: Any = ...
    def get_default_style(self): ...
    default_style: Any = ...
    def set_colour_RGB(self, colour_index: Any, red: Any, green: Any, blue: Any) -> None: ...
    def add_style(self, style: Any): ...
    def add_font(self, font: Any): ...
    def add_str(self, s: Any): ...
    def del_str(self, sst_idx: Any) -> None: ...
    def str_index(self, s: Any): ...
    def add_rt(self, rt: Any): ...
    def rt_index(self, rt: Any): ...
    def add_sheet(self, sheetname: str, cell_overwrite_ok: bool = ...) -> Worksheet: ...
    def get_sheet(self, sheet: Any): ...
    def sheet_index(self, sheetname: Any): ...
    def raise_bad_sheetname(self, sheetname: Any) -> None: ...
    def convert_sheetindex(self, strg_ref: Any, n_sheets: Any): ...
    def setup_ownbook(self) -> None: ...
    def setup_xcall(self) -> None: ...
    def add_sheet_reference(self, formula: Any) -> None: ...
    def get_biff_data(self): ...
    def save(self, filename_or_stream: Any) -> None: ...