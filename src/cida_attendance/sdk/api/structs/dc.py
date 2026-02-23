from ctypes import Structure

from ..base_classes import _S, HWND
from ..ctypes_preamble import POINTER


class struct___DC(Structure):
    pass

_S(struct___DC, [
    ('surface', POINTER(None)),
    ('hWnd', HWND),
])

DC = struct___DC
HDC = POINTER(DC)
__DC = struct___DC
