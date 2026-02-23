from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_QUERY_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_QUERY_STATUS, [
    ('dwSize', DWORD),
    ('byCpuLoad', BYTE),
    ('byMemLoad', BYTE),
    ('wAbility', WORD),
    ('wRemainAbility', WORD),
    ('wTotalPlanNum', WORD),
    ('wCurPlanNum', WORD),
    ('byRes', BYTE * 62),
])

NET_DVR_QUERY_STATUS = struct_tagNET_DVR_QUERY_STATUS
LPNET_DVR_QUERY_STATUS = POINTER(struct_tagNET_DVR_QUERY_STATUS)
tagNET_DVR_QUERY_STATUS = struct_tagNET_DVR_QUERY_STATUS
