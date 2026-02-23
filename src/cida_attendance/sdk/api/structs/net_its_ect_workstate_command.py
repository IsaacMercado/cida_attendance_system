from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_ITS_ECT_WORKSTATE_COMMAND(Structure):
    pass

_S(struct_tagNET_ITS_ECT_WORKSTATE_COMMAND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byRes', BYTE * 256),
])

NET_ITS_ECT_WORKSTATE_COMMAND = struct_tagNET_ITS_ECT_WORKSTATE_COMMAND
LPNET_ITS_ECT_WORKSTATE_COMMAND = POINTER(struct_tagNET_ITS_ECT_WORKSTATE_COMMAND)
tagNET_ITS_ECT_WORKSTATE_COMMAND = struct_tagNET_ITS_ECT_WORKSTATE_COMMAND
