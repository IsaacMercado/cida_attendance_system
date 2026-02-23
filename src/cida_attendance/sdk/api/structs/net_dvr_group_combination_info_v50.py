from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_GROUP_COMBINATION_INFO_V50(Structure):
    pass

_S(struct_tagNET_DVR_GROUP_COMBINATION_INFO_V50, [
    ('byEnable', BYTE),
    ('byMemberNum', BYTE),
    ('bySequenceNo', BYTE),
    ('byRes', BYTE),
    ('dwGroupNo', DWORD),
])

NET_DVR_GROUP_COMBINATION_INFO_V50 = struct_tagNET_DVR_GROUP_COMBINATION_INFO_V50
LPNET_DVR_GROUP_COMBINATION_INFO_V50 = POINTER(struct_tagNET_DVR_GROUP_COMBINATION_INFO_V50)
tagNET_DVR_GROUP_COMBINATION_INFO_V50 = struct_tagNET_DVR_GROUP_COMBINATION_INFO_V50
