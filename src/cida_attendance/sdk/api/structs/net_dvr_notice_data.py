from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_notice_pic import NET_DVR_NOTICE_PIC
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_NOTICE_DATA(Structure):
    pass

_S(struct_tagNET_DVR_NOTICE_DATA, [
    ('dwSize', DWORD),
    ('struTime', NET_DVR_TIME_EX),
    ('byNoticeNumber', BYTE * 32),
    ('byNoticeTheme', BYTE * 64),
    ('byNoticeDetail', BYTE * 1024),
    ('byLevel', BYTE),
    ('byPicNum', BYTE),
    ('byRes1', BYTE * 2),
    ('struNoticePic', NET_DVR_NOTICE_PIC * 6),
    ('byRes2', BYTE * 128),
])

NET_DVR_NOTICE_DATA = struct_tagNET_DVR_NOTICE_DATA
LPNET_DVR_NOTICE_DATA = POINTER(struct_tagNET_DVR_NOTICE_DATA)
tagNET_DVR_NOTICE_DATA = struct_tagNET_DVR_NOTICE_DATA
