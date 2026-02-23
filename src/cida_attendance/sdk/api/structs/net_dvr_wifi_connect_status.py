from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_WIFI_CONNECT_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_WIFI_CONNECT_STATUS, [
    ('dwSize', DWORD),
    ('byCurStatus', BYTE),
    ('byRes1', BYTE * 3),
    ('dwErrorCode', DWORD),
    ('byRes', BYTE * 244),
])

NET_DVR_WIFI_CONNECT_STATUS = struct_tagNET_DVR_WIFI_CONNECT_STATUS
LPNET_DVR_WIFI_CONNECT_STATUS = POINTER(struct_tagNET_DVR_WIFI_CONNECT_STATUS)
tagNET_DVR_WIFI_CONNECT_STATUS = struct_tagNET_DVR_WIFI_CONNECT_STATUS
