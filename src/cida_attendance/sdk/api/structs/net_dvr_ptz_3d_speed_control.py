from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PTZ_3D_SPEED_CONTROL(Structure):
    pass

_S(struct_tagNET_DVR_PTZ_3D_SPEED_CONTROL, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byPSpeed', BYTE),
    ('byTSpeed', BYTE),
    ('byZSpeed', BYTE),
    ('byPDirect', BYTE),
    ('byTDirect', BYTE),
    ('byZDirect', BYTE),
    ('byRes', BYTE * 18),
])

NET_DVR_PTZ_3D_SPEED_CONTROL = struct_tagNET_DVR_PTZ_3D_SPEED_CONTROL
LPNET_DVR_PTZ_3D_SPEED_CONTROL = POINTER(struct_tagNET_DVR_PTZ_3D_SPEED_CONTROL)
tagNET_DVR_PTZ_3D_SPEED_CONTROL = struct_tagNET_DVR_PTZ_3D_SPEED_CONTROL
