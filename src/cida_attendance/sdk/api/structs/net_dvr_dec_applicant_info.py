from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_DEC_APPLICANT_INFO(Structure):
    pass

_S(struct_tagNET_DVR_DEC_APPLICANT_INFO, [
    ('dwSize', DWORD),
    ('dwDecResource', DWORD),
    ('dwChannel', DWORD),
    ('struIP', NET_DVR_IPADDR),
    ('wPort', WORD),
    ('byRes', BYTE * 18),
])

NET_DVR_DEC_APPLICANT_INFO = struct_tagNET_DVR_DEC_APPLICANT_INFO
LPNET_DVR_DEC_APPLICANT_INFO = POINTER(struct_tagNET_DVR_DEC_APPLICANT_INFO)
tagNET_DVR_DEC_APPLICANT_INFO = struct_tagNET_DVR_DEC_APPLICANT_INFO
