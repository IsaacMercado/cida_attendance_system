from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_PLATECHECK_PARA(Structure):
    pass

_S(struct_tagNET_DVR_PLATECHECK_PARA, [
    ('bAlarmWhenChecked', BYTE),
    ('bInformWhenChecked', BYTE),
    ('byRes', BYTE * 6),
    ('struBlockFtpServer', NET_DVR_IPADDR),
])

NET_DVR_PLATECHECK_PARA = struct_tagNET_DVR_PLATECHECK_PARA
LPNET_DVR_PLATECHECK_PARA = POINTER(struct_tagNET_DVR_PLATECHECK_PARA)
tagNET_DVR_PLATECHECK_PARA = struct_tagNET_DVR_PLATECHECK_PARA
