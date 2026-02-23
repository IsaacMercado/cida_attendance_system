from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_366 import union_anon_366


class struct_tagNET_DVR_PUSHALARMINFO_V40(Structure):
    pass

_S(struct_tagNET_DVR_PUSHALARMINFO_V40, [
    ('dwAlarmType', DWORD),
    ('uAlarmInfo', union_anon_366),
])

NET_DVR_PUSHALARMINFO_V40 = struct_tagNET_DVR_PUSHALARMINFO_V40
LPNET_DVR_PUSHALARMINFO_V40 = POINTER(struct_tagNET_DVR_PUSHALARMINFO_V40)
tagNET_DVR_PUSHALARMINFO_V40 = struct_tagNET_DVR_PUSHALARMINFO_V40
