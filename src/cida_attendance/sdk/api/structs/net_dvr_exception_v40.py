from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_handleexception_v41 import NET_DVR_HANDLEEXCEPTION_V41


class struct_tagNET_DVR_EXCEPTION_V40(Structure):
    pass

_S(struct_tagNET_DVR_EXCEPTION_V40, [
    ('dwSize', DWORD),
    ('dwMaxGroupNum', DWORD),
    ('struExceptionHandle', NET_DVR_HANDLEEXCEPTION_V41 * 32),
    ('byRes', BYTE * 128),
])

NET_DVR_EXCEPTION_V40 = struct_tagNET_DVR_EXCEPTION_V40
LPNET_DVR_EXCEPTION_V40 = POINTER(struct_tagNET_DVR_EXCEPTION_V40)
tagNET_DVR_EXCEPTION_V40 = struct_tagNET_DVR_EXCEPTION_V40
