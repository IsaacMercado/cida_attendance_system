from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_WPS_CONNECT_PARAM_(Structure):
    pass

_S(struct_tagNET_DVR_WPS_CONNECT_PARAM_, [
    ('dwSize', DWORD),
    ('byConnectType', BYTE),
    ('byRes1', BYTE * 3),
    ('byPIN', BYTE * 8),
    ('byEssid', BYTE * 32),
    ('byRes', BYTE * 32),
])

NET_DVR_WPS_CONNECT_PARAM = struct_tagNET_DVR_WPS_CONNECT_PARAM_
LPNET_DVR_WPS_CONNECT_PARAM = POINTER(struct_tagNET_DVR_WPS_CONNECT_PARAM_)
tagNET_DVR_WPS_CONNECT_PARAM_ = struct_tagNET_DVR_WPS_CONNECT_PARAM_
