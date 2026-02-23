from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_ONLINEUSER_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ONLINEUSER_CFG, [
    ('dwSize', DWORD),
    ('byID', BYTE),
    ('byUserType', BYTE),
    ('byDataType', BYTE),
    ('byRes', BYTE),
    ('struIpAddr', NET_DVR_IPADDR),
    ('struLoginTime', NET_DVR_TIME_V30),
    ('szUserName', c_char * 32),
    ('byRes1', BYTE * 128),
])

NET_DVR_ONLINEUSER_CFG = struct_tagNET_DVR_ONLINEUSER_CFG
LPNET_DVR_ONLINEUSER_CFG = POINTER(struct_tagNET_DVR_ONLINEUSER_CFG)
tagNET_DVR_ONLINEUSER_CFG = struct_tagNET_DVR_ONLINEUSER_CFG
