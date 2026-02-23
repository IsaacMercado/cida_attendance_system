from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_27 import NET_DVR_RGB_COLOR


class struct_tagNET_DVR_INPUT_SOURCE_TEXT(Structure):
    pass

_S(struct_tagNET_DVR_INPUT_SOURCE_TEXT, [
    ('dwSize', DWORD),
    ('dwTextNo', DWORD),
    ('byEnable', BYTE),
    ('byFontSize', BYTE),
    ('byBkGroudMode', BYTE),
    ('byRes', BYTE * 1),
    ('dwXPosition', DWORD),
    ('dwYPosition', DWORD),
    ('struForegroudColor', NET_DVR_RGB_COLOR),
    ('struBackgroudColor', NET_DVR_RGB_COLOR),
    ('byTextContent', BYTE * 128),
    ('byRes1', BYTE * 64),
])

NET_DVR_INPUT_SOURCE_TEXT = struct_tagNET_DVR_INPUT_SOURCE_TEXT
LPNET_DVR_INPUT_SOURCE_TEXT = POINTER(struct_tagNET_DVR_INPUT_SOURCE_TEXT)
tagNET_DVR_INPUT_SOURCE_TEXT = struct_tagNET_DVR_INPUT_SOURCE_TEXT
