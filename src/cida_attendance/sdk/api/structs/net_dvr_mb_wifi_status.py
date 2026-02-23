from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MB_WIFI_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_MB_WIFI_STATUS, [
    ('byEnableWiFi', BYTE),
    ('byWiFiConnectStatus', BYTE),
    ('bySignalStrength', BYTE),
    ('byIPaddress', BYTE * 16),
    ('byEssid', BYTE * 32),
    ('byres', BYTE * 5),
])

NET_DVR_MB_WIFI_STATUS = struct_tagNET_DVR_MB_WIFI_STATUS
LPNET_DVR_MB_WIFI_STATUS = POINTER(struct_tagNET_DVR_MB_WIFI_STATUS)
tagNET_DVR_MB_WIFI_STATUS = struct_tagNET_DVR_MB_WIFI_STATUS
