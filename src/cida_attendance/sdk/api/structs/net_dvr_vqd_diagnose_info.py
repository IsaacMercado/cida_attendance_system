from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_vqd_diagnose_exception_info import NET_DVR_VQD_DIAGNOSE_EXCEPTION_INFO


class struct_tagNET_DVR_VQD_DIAGNOSE_INFO(Structure):
    pass

_S(struct_tagNET_DVR_VQD_DIAGNOSE_INFO, [
    ('dwSize', DWORD),
    ('struVQDDiagnoseExceptionInfo', NET_DVR_VQD_DIAGNOSE_EXCEPTION_INFO),
])

NET_DVR_VQD_DIAGNOSE_INFO = struct_tagNET_DVR_VQD_DIAGNOSE_INFO
LPNET_DVR_VQD_DIAGNOSE_INFO = POINTER(struct_tagNET_DVR_VQD_DIAGNOSE_INFO)
tagNET_DVR_VQD_DIAGNOSE_INFO = struct_tagNET_DVR_VQD_DIAGNOSE_INFO
