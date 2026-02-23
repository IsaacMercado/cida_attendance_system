from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_431(Structure):
    pass

_S(struct_anon_431, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byDeviceStatus', BYTE),
    ('byAllowRedirect', BYTE),
    ('byDomainName', BYTE * 64),
    ('byRes1', BYTE),
    ('byVerificationCode', BYTE * 32),
    ('byNetMode', BYTE),
    ('byOfflineStatus', BYTE),
    ('byEnableTiming', BYTE),
    ('byRes2', BYTE),
    ('byOperateCode', BYTE * 64),
    ('byRes', BYTE * 344),
])

NET_DVR_EZVIZ_ACCESS_CFG = struct_anon_431
LPNET_DVR_EZVIZ_ACCESS_CFG = POINTER(struct_anon_431)
