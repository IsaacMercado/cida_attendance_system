from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_DISP_CHAN_INFO(Structure):
    pass

_S(struct_tagNET_DVR_DISP_CHAN_INFO, [
    ('struIP', NET_DVR_IPADDR),
    ('wDVRPort', WORD),
    ('byDispChannel', BYTE),
    ('byUsedSlotNum', BYTE),
    ('bySlotNum', BYTE),
    ('byRes', BYTE * 7),
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
])

NET_DVR_DISP_CHAN_INFO = struct_tagNET_DVR_DISP_CHAN_INFO
LPNET_DVR_DISP_CHAN_INFO = POINTER(struct_tagNET_DVR_DISP_CHAN_INFO)
tagNET_DVR_DISP_CHAN_INFO = struct_tagNET_DVR_DISP_CHAN_INFO
