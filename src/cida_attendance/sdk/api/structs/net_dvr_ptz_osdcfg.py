from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PTZ_OSDCFG(Structure):
    pass

_S(struct_tagNET_DVR_PTZ_OSDCFG, [
    ('dwSize', DWORD),
    ('byZoomStatus', BYTE),
    ('byPtStatus', BYTE),
    ('byPresetStatus', BYTE),
    ('byPositionDisplayFormat', BYTE),
    ('byRes', BYTE * 124),
])

NET_DVR_PTZ_OSDCFG = struct_tagNET_DVR_PTZ_OSDCFG
LPNET_DVR_PTZ_OSDCFG = POINTER(struct_tagNET_DVR_PTZ_OSDCFG)
tagNET_DVR_PTZ_OSDCFG = struct_tagNET_DVR_PTZ_OSDCFG
