from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CURTRIGGERMODE(Structure):
    pass

_S(struct_tagNET_DVR_CURTRIGGERMODE, [
    ('dwSize', DWORD),
    ('dwTriggerType', DWORD),
    ('byRes', BYTE * 24),
])

NET_DVR_CURTRIGGERMODE = struct_tagNET_DVR_CURTRIGGERMODE
LPNET_DVR_CURTRIGGERMODE = POINTER(struct_tagNET_DVR_CURTRIGGERMODE)
tagNET_DVR_CURTRIGGERMODE = struct_tagNET_DVR_CURTRIGGERMODE
