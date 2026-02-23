from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FOCUSMODE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_FOCUSMODE_CFG, [
    ('dwSize', DWORD),
    ('byFocusMode', BYTE),
    ('byAutoFocusMode', BYTE),
    ('wMinFocusDistance', WORD),
    ('byZoomSpeedLevel', BYTE),
    ('byFocusSpeedLevel', BYTE),
    ('byOpticalZoom', BYTE),
    ('byDigtitalZoom', BYTE),
    ('fOpticalZoomLevel', c_float),
    ('dwFocusPos', DWORD),
    ('byFocusDefinitionDisplay', BYTE),
    ('byFocusSensitivity', BYTE),
    ('byRes1', BYTE * 2),
    ('dwRelativeFocusPos', DWORD),
    ('byRes', BYTE * 48),
])

NET_DVR_FOCUSMODE_CFG = struct_tagNET_DVR_FOCUSMODE_CFG
LPNET_DVR_FOCUSMODE_CFG = POINTER(struct_tagNET_DVR_FOCUSMODE_CFG)
tagNET_DVR_FOCUSMODE_CFG = struct_tagNET_DVR_FOCUSMODE_CFG
