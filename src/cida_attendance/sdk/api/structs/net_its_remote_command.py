from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_ITS_REMOTE_COMMAND(Structure):
    pass

_S(struct_tagNET_ITS_REMOTE_COMMAND, [
    ('wLaneid', WORD),
    ('byCamLaneId', BYTE),
    ('byRes', BYTE),
    ('dwCode', DWORD),
    ('byRes1', BYTE * 128),
])

NET_ITS_REMOTE_COMMAND = struct_tagNET_ITS_REMOTE_COMMAND
LPNET_ITS_REMOTE_COMMAND = POINTER(struct_tagNET_ITS_REMOTE_COMMAND)
tagNET_ITS_REMOTE_COMMAND = struct_tagNET_ITS_REMOTE_COMMAND
