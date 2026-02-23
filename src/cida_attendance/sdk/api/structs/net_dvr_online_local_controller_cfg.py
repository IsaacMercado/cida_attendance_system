from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_ONLINE_LOCAL_CONTROLLER_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ONLINE_LOCAL_CONTROLLER_CFG, [
    ('dwSize', DWORD),
    ('byLocalControllerName', BYTE * 32),
    ('wLocalControllerID', WORD),
    ('wDevPort', WORD),
    ('struDevIP', NET_DVR_IPADDR),
    ('struSubnetMask', NET_DVR_IPADDR),
    ('struGateway', NET_DVR_IPADDR),
    ('bySearchProgress', BYTE),
    ('byEffectData', BYTE),
    ('byRes', BYTE * 302),
])

NET_DVR_ONLINE_LOCAL_CONTROLLER_CFG = struct_tagNET_DVR_ONLINE_LOCAL_CONTROLLER_CFG
LPNET_DVR_ONLINE_LOCAL_CONTROLLER_CFG = POINTER(struct_tagNET_DVR_ONLINE_LOCAL_CONTROLLER_CFG)
tagNET_DVR_ONLINE_LOCAL_CONTROLLER_CFG = struct_tagNET_DVR_ONLINE_LOCAL_CONTROLLER_CFG
