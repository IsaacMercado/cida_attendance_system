from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_SIP_CFG_V50(Structure):
    pass

_S(struct_tagNET_DVR_SIP_CFG_V50, [
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
    ('byRes3', BYTE),
    ('bySIPServerDomain', BYTE * 64),
    ('stuSTUNServerIP', NET_DVR_IPADDR),
    ('bySTUNServerDomain', BYTE * 64),
    ('wSTUNServerPort', WORD),
    ('byRes4', BYTE * 2),
    ('stuProxyServerIP', NET_DVR_IPADDR),
    ('byProxyServerDomain', BYTE * 64),
    ('wProxyServerPort', WORD),
    ('byNetWork', BYTE),
    ('byRes5', BYTE),
    ('byCalledTargetName', BYTE * 32),
    ('byRes', BYTE * 224),
])

NET_DVR_SIP_CFG_V50 = struct_tagNET_DVR_SIP_CFG_V50
LPNET_DVR_SIP_CFG_V50 = POINTER(struct_tagNET_DVR_SIP_CFG_V50)
tagNET_DVR_SIP_CFG_V50 = struct_tagNET_DVR_SIP_CFG_V50
