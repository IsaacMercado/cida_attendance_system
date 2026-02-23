from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SINGLE_SECURITY_QUESTION_CFG(Structure):
    pass

_S(struct_tagNET_DVR_SINGLE_SECURITY_QUESTION_CFG, [
    ('dwSize', DWORD),
    ('dwId', DWORD),
    ('sAnswer', c_char * 256),
    ('byMark', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_SINGLE_SECURITY_QUESTION_CFG = struct_tagNET_DVR_SINGLE_SECURITY_QUESTION_CFG
LPNET_DVR_SINGLE_SECURITY_QUESTION_CFG = POINTER(struct_tagNET_DVR_SINGLE_SECURITY_QUESTION_CFG)
tagNET_DVR_SINGLE_SECURITY_QUESTION_CFG = struct_tagNET_DVR_SINGLE_SECURITY_QUESTION_CFG
