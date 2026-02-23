from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_lli_param import NET_DVR_LLI_PARAM


class struct_tagNET_DVR_REVISE_GPS_CFG(Structure):
    pass

_S(struct_tagNET_DVR_REVISE_GPS_CFG, [
    ('dwSize', DWORD),
    ('byLatitudeType', BYTE),
    ('byLongitudeType', BYTE),
    ('byMode', BYTE),
    ('byRes', BYTE),
    ('struLatitude', NET_DVR_LLI_PARAM),
    ('struLongitude', NET_DVR_LLI_PARAM),
    ('byRes1', BYTE * 300),
])

NET_DVR_REVISE_GPS_CFG = struct_tagNET_DVR_REVISE_GPS_CFG
LPNET_DVR_REVISE_GPS_CFG = POINTER(struct_tagNET_DVR_REVISE_GPS_CFG)
tagNET_DVR_REVISE_GPS_CFG = struct_tagNET_DVR_REVISE_GPS_CFG
