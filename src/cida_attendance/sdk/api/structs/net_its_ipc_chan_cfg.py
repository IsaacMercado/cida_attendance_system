from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_ITS_IPC_CHAN_CFG(Structure):
    pass

_S(struct_tagNET_ITS_IPC_CHAN_CFG, [
    ('dwSize', DWORD),
    ('byCameraType', BYTE),
    ('byRes1', BYTE * 3),
    ('byMonitoringSiteID', BYTE * 48),
    ('byDeviceID', BYTE * 48),
    ('byDirectionNo', BYTE),
    ('byMonitorInfo', BYTE * 48),
    ('byRes2', BYTE * 15),
])

NET_ITS_IPC_CHAN_CFG = struct_tagNET_ITS_IPC_CHAN_CFG
LPNET_ITS_IPC_CHAN_CFG = POINTER(struct_tagNET_ITS_IPC_CHAN_CFG)
tagNET_ITS_IPC_CHAN_CFG = struct_tagNET_ITS_IPC_CHAN_CFG
