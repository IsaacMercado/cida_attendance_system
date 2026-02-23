from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_BEHAVIOUR_COND(Structure):
    pass

_S(struct_tagNET_DVR_BEHAVIOUR_COND, [
    ('dwSearchType', DWORD),
    ('byHumanMisinfo', BYTE),
    ('byRes', BYTE * 251),
])

NET_DVR_BEHAVIOUR_COND = struct_tagNET_DVR_BEHAVIOUR_COND
LPNET_DVR_BEHAVIOUR_COND = POINTER(struct_tagNET_DVR_BEHAVIOUR_COND)
tagNET_DVR_BEHAVIOUR_COND = struct_tagNET_DVR_BEHAVIOUR_COND
