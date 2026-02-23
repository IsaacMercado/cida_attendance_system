from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR
from .net_dvr_alarmhost_netparam import NET_DVR_ALARMHOST_NETPARAM


class struct_tagNET_DVR_ALARMHOST_WIRELESS_NETWORK_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_WIRELESS_NETWORK_CFG, [
    ('dwSize', DWORD),
    ('struNetCenter', NET_DVR_ALARMHOST_NETPARAM * 4),
    ('byAPNName', BYTE * 32),
    ('byAPNUserName', BYTE * 24),
    ('byAPNPassWord', BYTE * 16),
    ('byReconnTime', BYTE),
    ('byOverTime', BYTE),
    ('byDetectLinkTime', BYTE),
    ('byRes1', BYTE),
    ('bySIMNum', BYTE * 32),
    ('struSIMIP', NET_DVR_IPADDR),
    ('byRes2', BYTE * 64),
])

NET_DVR_ALARMHOST_WIRELESS_NETWORK_CFG = struct_tagNET_DVR_ALARMHOST_WIRELESS_NETWORK_CFG
LPNET_DVR_ALARMHOST_WIRELESS_NETWORK_CFG = POINTER(struct_tagNET_DVR_ALARMHOST_WIRELESS_NETWORK_CFG)
tagNET_DVR_ALARMHOST_WIRELESS_NETWORK_CFG = struct_tagNET_DVR_ALARMHOST_WIRELESS_NETWORK_CFG
