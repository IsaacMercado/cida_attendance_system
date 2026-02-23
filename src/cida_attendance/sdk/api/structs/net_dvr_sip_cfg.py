from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_SIP_CFG(Structure):
    pass

_S(struct_tagNET_DVR_SIP_CFG, [
    ('dwSize', DWORD),
    ('byEnableAutoLogin', BYTE),
    ('byLoginStatus', BYTE),
    ('byRes1', BYTE * 2),
    ('stuServerIP', NET_DVR_IPADDR),
    ('wServerPort', WORD),
    ('byRes2', BYTE * 2),
    ('byUserName', BYTE * 32),
    ('byPassWord', BYTE * 16),
    ('byLocalNo', BYTE * 32),
    ('byDispalyName', BYTE * 128),
    ('wLocalPort', WORD),
    ('byLoginCycle', BYTE),
    ('byType', BYTE),
    ('byDomainName', BYTE * 64),
    ('byRes', BYTE * 64),
])

NET_DVR_SIP_CFG = struct_tagNET_DVR_SIP_CFG
LPNET_DVR_SIP_CFG = POINTER(struct_tagNET_DVR_SIP_CFG)
tagNET_DVR_SIP_CFG = struct_tagNET_DVR_SIP_CFG
