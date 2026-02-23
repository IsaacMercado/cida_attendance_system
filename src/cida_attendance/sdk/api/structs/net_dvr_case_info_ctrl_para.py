from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CASE_INFO_CTRL_PARA(Structure):
    pass

_S(struct_tagNET_DVR_CASE_INFO_CTRL_PARA, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byShowCaseInfoTime', BYTE),
    ('byRes', BYTE * 131),
])

NET_DVR_CASE_INFO_CTRL_PARAM = struct_tagNET_DVR_CASE_INFO_CTRL_PARA
LPNET_DVR_CASE_INFO_CTRL_PARA = POINTER(struct_tagNET_DVR_CASE_INFO_CTRL_PARA)
tagNET_DVR_CASE_INFO_CTRL_PARA = struct_tagNET_DVR_CASE_INFO_CTRL_PARA
