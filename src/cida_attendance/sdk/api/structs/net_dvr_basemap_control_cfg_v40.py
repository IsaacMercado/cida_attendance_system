from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_gis_server_info import NET_DVR_GIS_SERVER_INFO


class struct_tagNET_DVR_BASEMAP_CONTROL_CFG_V40(Structure):
    pass

_S(struct_tagNET_DVR_BASEMAP_CONTROL_CFG_V40, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byBaseMapType', BYTE),
    ('byRes1', BYTE * 2),
    ('dwBaseMapNo', DWORD),
    ('struGisServer', NET_DVR_GIS_SERVER_INFO),
    ('byRes2', BYTE * 64),
])

NET_DVR_BASEMAP_CONTROL_CFG_V40 = struct_tagNET_DVR_BASEMAP_CONTROL_CFG_V40
LPNET_DVR_BASEMAP_CONTROL_CFG_V40 = POINTER(struct_tagNET_DVR_BASEMAP_CONTROL_CFG_V40)
tagNET_DVR_BASEMAP_CONTROL_CFG_V40 = struct_tagNET_DVR_BASEMAP_CONTROL_CFG_V40
