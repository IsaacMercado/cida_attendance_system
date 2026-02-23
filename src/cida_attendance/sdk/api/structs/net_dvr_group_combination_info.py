from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_GROUP_COMBINATION_INFO(Structure):
    pass

_S(struct_tagNET_DVR_GROUP_COMBINATION_INFO, [
    ('byEnable', BYTE),
    ('byMemberNum', BYTE),
    ('bySequenceNo', BYTE),
    ('byRes', BYTE),
    ('dwGroupNo', DWORD),
])

NET_DVR_GROUP_COMBINATION_INFO = struct_tagNET_DVR_GROUP_COMBINATION_INFO
LPNET_DVR_GROUP_COMBINATION_INFO = POINTER(struct_tagNET_DVR_GROUP_COMBINATION_INFO)
tagNET_DVR_GROUP_COMBINATION_INFO = struct_tagNET_DVR_GROUP_COMBINATION_INFO
