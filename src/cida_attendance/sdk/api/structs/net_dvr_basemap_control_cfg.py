from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_BASEMAP_CONTROL_CFG(Structure):
    pass

_S(struct_tagNET_DVR_BASEMAP_CONTROL_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byBaseMapType', BYTE),
    ('byBaseMapCircleNo', BYTE),
    ('byRes1', BYTE),
    ('dwBaseMapNo', DWORD),
    ('byRes2', BYTE * 64),
])

NET_DVR_BASEMAP_CONTROL_CFG = struct_tagNET_DVR_BASEMAP_CONTROL_CFG
LPNET_DVR_BASEMAP_CONTROL_CFG = POINTER(struct_tagNET_DVR_BASEMAP_CONTROL_CFG)
tagNET_DVR_BASEMAP_CONTROL_CFG = struct_tagNET_DVR_BASEMAP_CONTROL_CFG
