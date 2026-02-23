from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_POSTRADARSPEED_CFG(Structure):
    pass

_S(struct_tagNET_DVR_POSTRADARSPEED_CFG, [
    ('dwSize', DWORD),
    ('byLaneType', BYTE),
    ('byRes1', BYTE * 3),
    ('dwInterval', DWORD),
    ('dwSignSpeed', DWORD),
    ('dwSpeedLimit', DWORD),
    ('dwBigCarSignSpeed', DWORD),
    ('dwBigCarSpeedLimit', DWORD),
    ('dwLowSpeedLimit', DWORD),
    ('dwBigCarLowSpeedLimit', DWORD),
    ('byCheckPostEnabled', BYTE),
    ('byOverSpeedEnabled', BYTE),
    ('byRes', BYTE * 246),
])

NET_DVR_POSTRADARSPEED_CFG = struct_tagNET_DVR_POSTRADARSPEED_CFG
LPNET_DVR_POSTRADARSPEED_CFG = POINTER(struct_tagNET_DVR_POSTRADARSPEED_CFG)
tagNET_DVR_POSTRADARSPEED_CFG = struct_tagNET_DVR_POSTRADARSPEED_CFG
