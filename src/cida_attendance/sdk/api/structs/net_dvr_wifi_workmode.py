from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_WIFI_WORKMODE(Structure):
    pass

_S(struct_tagNET_DVR_WIFI_WORKMODE, [
    ('dwSize', DWORD),
    ('dwNetworkInterfaceMode', DWORD),
])

NET_DVR_WIFI_WORKMODE = struct_tagNET_DVR_WIFI_WORKMODE
LPNET_DVR_WIFI_WORKMODE = POINTER(struct_tagNET_DVR_WIFI_WORKMODE)
tagNET_DVR_WIFI_WORKMODE = struct_tagNET_DVR_WIFI_WORKMODE
