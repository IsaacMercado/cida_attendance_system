from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_single_security_question_cfg import NET_DVR_SINGLE_SECURITY_QUESTION_CFG


class struct_tagNET_DVR_SECURITY_QUESTION_CFG(Structure):
    pass

_S(struct_tagNET_DVR_SECURITY_QUESTION_CFG, [
    ('dwSize', DWORD),
    ('struSecurityQuestion', NET_DVR_SINGLE_SECURITY_QUESTION_CFG * 32),
    ('sLoginPassWord', c_char * 128),
    ('byRes', BYTE * 512),
])

NET_DVR_SECURITY_QUESTION_CFG = struct_tagNET_DVR_SECURITY_QUESTION_CFG
LPNET_DVR_SECURITY_QUESTION_CFG = POINTER(struct_tagNET_DVR_SECURITY_QUESTION_CFG)
tagNET_DVR_SECURITY_QUESTION_CFG = struct_tagNET_DVR_SECURITY_QUESTION_CFG
