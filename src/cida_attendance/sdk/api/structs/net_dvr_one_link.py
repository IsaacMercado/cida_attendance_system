from ctypes import Structure

from ..base_classes import _S, BYTE, LONG
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_ONE_LINK(Structure):
    pass

_S(struct_tagNET_DVR_ONE_LINK, [
    ('struIP', NET_DVR_IPADDR),
    ('lChannel', LONG),
    ('byRes', BYTE * 32),
])

NET_DVR_ONE_LINK = struct_tagNET_DVR_ONE_LINK
LPNET_DVR_ONE_LINK = POINTER(struct_tagNET_DVR_ONE_LINK)
tagNET_DVR_ONE_LINK = struct_tagNET_DVR_ONE_LINK
