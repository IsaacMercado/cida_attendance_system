from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VIDEOWALL_MATERIAL_COND(Structure):
    pass

_S(struct_tagNET_DVR_VIDEOWALL_MATERIAL_COND, [
    ('dwSize', DWORD),
    ('byWallNo', BYTE),
    ('byWindowType', BYTE),
    ('byFileType', BYTE),
    ('byRes1', BYTE),
    ('dwWindowNo', DWORD),
    ('dwMaterialNo', DWORD),
    ('byRes', BYTE * 32),
])

NET_DVR_VIDEOWALL_MATERIAL_COND = struct_tagNET_DVR_VIDEOWALL_MATERIAL_COND
LPNET_DVR_VIDEOWALL_MATERIAL_COND = POINTER(struct_tagNET_DVR_VIDEOWALL_MATERIAL_COND)
tagNET_DVR_VIDEOWALL_MATERIAL_COND = struct_tagNET_DVR_VIDEOWALL_MATERIAL_COND
