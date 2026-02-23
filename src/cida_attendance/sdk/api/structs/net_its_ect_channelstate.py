from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_ITS_ECT_CHANNELSTATE(Structure):
    pass

_S(struct_tagNET_ITS_ECT_CHANNELSTATE, [
    ('dwSize', DWORD),
    ('byRecordStatic', BYTE),
    ('bySignalStatic', BYTE),
    ('byHardwareStatic', BYTE),
    ('byChannelArmState', BYTE),
    ('dwChannel', DWORD),
    ('dwBitRate', DWORD),
    ('dwLinkNum', DWORD),
    ('struClientIP', NET_DVR_IPADDR * 6),
    ('dwIPLinkNum', DWORD),
    ('byExceedMaxLink', BYTE),
    ('byRes', BYTE * 139),
])

NET_ITS_ECT_CHANNELSTATE = struct_tagNET_ITS_ECT_CHANNELSTATE
LPNET_ITS_ECT_CHANNELSTATE = POINTER(struct_tagNET_ITS_ECT_CHANNELSTATE)
tagNET_ITS_ECT_CHANNELSTATE = struct_tagNET_ITS_ECT_CHANNELSTATE
