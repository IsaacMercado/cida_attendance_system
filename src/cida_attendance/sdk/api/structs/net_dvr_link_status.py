from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_one_link import NET_DVR_ONE_LINK


class struct_tagNET_DVR_LINK_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_LINK_STATUS, [
    ('dwSize', DWORD),
    ('wLinkNum', WORD),
    ('byRes1', BYTE * 2),
    ('struOneLink', NET_DVR_ONE_LINK * 128),
    ('byRes', BYTE * 32),
])

NET_DVR_LINK_STATUS = struct_tagNET_DVR_LINK_STATUS
LPNET_DVR_LINK_STATUS = POINTER(struct_tagNET_DVR_LINK_STATUS)
tagNET_DVR_LINK_STATUS = struct_tagNET_DVR_LINK_STATUS
