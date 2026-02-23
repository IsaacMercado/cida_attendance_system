from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PTZ_BASICPARAMCFG(Structure):
    pass

_S(struct_tagNET_DVR_PTZ_BASICPARAMCFG, [
    ('dwSize', DWORD),
    ('byProportionalPan', BYTE),
    ('byPresetFreezing', BYTE),
    ('byPresetSpeed', BYTE),
    ('byKeyboardCtrlSpeed', BYTE),
    ('byAutoScanSpeed', BYTE),
    ('byZoomingSpeed', BYTE),
    ('byManualControlSpeed', BYTE),
    ('byPTZMotionTrack', BYTE),
    ('byRes', BYTE * 124),
])

NET_DVR_PTZ_BASICPARAMCFG = struct_tagNET_DVR_PTZ_BASICPARAMCFG
LPNET_DVR_PTZ_BASICPARAMCFG = POINTER(struct_tagNET_DVR_PTZ_BASICPARAMCFG)
tagNET_DVR_PTZ_BASICPARAMCFG = struct_tagNET_DVR_PTZ_BASICPARAMCFG
