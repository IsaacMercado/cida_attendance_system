from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR
from .net_dvr_atm_user_define_protocol import NET_DVR_ATM_USER_DEFINE_PROTOCOL


class struct_tagNET_DVR_ATM_FRAMEFORMAT_V30(Structure):
    pass

_S(struct_tagNET_DVR_ATM_FRAMEFORMAT_V30, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byInputMode', BYTE),
    ('byRes1', BYTE * 34),
    ('struAtmIp', NET_DVR_IPADDR),
    ('wAtmPort', WORD),
    ('byRes2', BYTE * 2),
    ('dwAtmType', DWORD),
    ('struAtmUserDefineProtocol', NET_DVR_ATM_USER_DEFINE_PROTOCOL),
    ('byRes3', BYTE * 8),
])

NET_DVR_ATM_FRAMEFORMAT_V30 = struct_tagNET_DVR_ATM_FRAMEFORMAT_V30
LPNET_DVR_ATM_FRAMEFORMAT_V30 = POINTER(struct_tagNET_DVR_ATM_FRAMEFORMAT_V30)
tagNET_DVR_ATM_FRAMEFORMAT_V30 = struct_tagNET_DVR_ATM_FRAMEFORMAT_V30
