from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_tagNET_DVR_VQD_DIAGNOSE_EXCEPTION_INFO(Structure):
    pass

_S(struct_tagNET_DVR_VQD_DIAGNOSE_EXCEPTION_INFO, [
    ('dwChannelNO', DWORD),
    ('dwVQDType', DWORD),
    ('struDiagnoseTime', NET_DVR_TIME),
    ('byScoreValue', BYTE),
    ('byRes', BYTE * 27),
])

NET_DVR_VQD_DIAGNOSE_EXCEPTION_INFO = struct_tagNET_DVR_VQD_DIAGNOSE_EXCEPTION_INFO
LPNET_DVR_VQD_DIAGNOSE_EXCEPTION_INFO = POINTER(struct_tagNET_DVR_VQD_DIAGNOSE_EXCEPTION_INFO)
tagNET_DVR_VQD_DIAGNOSE_EXCEPTION_INFO = struct_tagNET_DVR_VQD_DIAGNOSE_EXCEPTION_INFO
