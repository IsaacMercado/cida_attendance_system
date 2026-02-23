from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CONTROL_GATEWAY(Structure):
    pass

_S(struct_tagNET_DVR_CONTROL_GATEWAY, [
    ('dwSize', DWORD),
    ('dwGatewayIndex', DWORD),
    ('byCommand', BYTE),
    ('byLockType', BYTE),
    ('wLockID', WORD),
    ('byControlSrc', BYTE * 32),
    ('byControlType', BYTE),
    ('byRes3', BYTE * 3),
    ('byPassword', BYTE * 16),
    ('byRes2', BYTE * 108),
])

NET_DVR_CONTROL_GATEWAY = struct_tagNET_DVR_CONTROL_GATEWAY
LPNET_DVR_CONTROL_GATEWAY = POINTER(struct_tagNET_DVR_CONTROL_GATEWAY)
tagNET_DVR_CONTROL_GATEWAY = struct_tagNET_DVR_CONTROL_GATEWAY
