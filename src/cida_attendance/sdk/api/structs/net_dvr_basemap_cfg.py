from ctypes import Structure

from ..base_classes import _S, BYTE, WORD


class struct_tagNET_DVR_BASEMAP_CFG(Structure):
    pass

_S(struct_tagNET_DVR_BASEMAP_CFG, [
    ('byScreenIndex', BYTE),
    ('byMapNum', BYTE),
    ('res', BYTE * 2),
    ('wSourWidth', WORD),
    ('wSourHeight', WORD),
])

NET_DVR_BASEMAP_CFG = struct_tagNET_DVR_BASEMAP_CFG
LPNET_DVR_BASEMAP_CFG = struct_tagNET_DVR_BASEMAP_CFG
tagNET_DVR_BASEMAP_CFG = struct_tagNET_DVR_BASEMAP_CFG
