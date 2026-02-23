from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_REC_PASSBACK_BASIC_CFG(Structure):
    pass

_S(struct_tagNET_DVR_REC_PASSBACK_BASIC_CFG, [
    ('dwSize', DWORD),
    ('dwStartTime', DWORD),
    ('dwStopTime', DWORD),
    ('wMaxTotalConcurrenceNum', WORD),
    ('wMaxDvrConcurrenceNum', WORD),
    ('dwSyncSpeed', DWORD),
    ('dwRecordType', DWORD),
    ('byRes', BYTE * 248),
])

NET_DVR_REC_PASSBACK_BASIC_CFG = struct_tagNET_DVR_REC_PASSBACK_BASIC_CFG
LPNET_DVR_REC_PASSBACK_BASIC_CFG = POINTER(struct_tagNET_DVR_REC_PASSBACK_BASIC_CFG)
tagNET_DVR_REC_PASSBACK_BASIC_CFG = struct_tagNET_DVR_REC_PASSBACK_BASIC_CFG
