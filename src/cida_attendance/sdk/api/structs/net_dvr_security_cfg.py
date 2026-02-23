from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SECURITY_CFG(Structure):
    pass

_S(struct_tagNET_DVR_SECURITY_CFG, [
    ('dwSize', DWORD),
    ('byCommuMode', BYTE),
    ('byRes1', BYTE * 2),
    ('byWebAuthentication', BYTE),
    ('byRtspAuthentication', BYTE),
    ('byTelnetServer', BYTE),
    ('bySSHServer', BYTE),
    ('byIllegalLoginLock', BYTE),
    ('byStreamEncryption', BYTE),
    ('byAntiAttack', BYTE),
    ('byRes', BYTE * 26),
])

NET_DVR_SECURITY_CFG = struct_tagNET_DVR_SECURITY_CFG
LPNET_DVR_SECURITY_CFG = POINTER(struct_tagNET_DVR_SECURITY_CFG)
tagNET_DVR_SECURITY_CFG = struct_tagNET_DVR_SECURITY_CFG
