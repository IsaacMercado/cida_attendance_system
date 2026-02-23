from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_SIGNALLAMP_DETCFG(Structure):
    pass

_S(struct_tagNET_DVR_SIGNALLAMP_DETCFG, [
    ('dwSize', DWORD),
    ('byAbsTime', BYTE * 32),
    ('struAlarmCamIP', NET_DVR_IPADDR),
    ('dwPic1Len', DWORD),
    ('dwPic2Len', DWORD),
    ('pPic1Buffer', String),
    ('pPic2Buffer', String),
    ('byRes', BYTE * 128),
])

NET_DVR_SIGNALLAMP_DETCFG = struct_tagNET_DVR_SIGNALLAMP_DETCFG
LPNET_DVR_SIGNALLAMP_DETCFG = POINTER(struct_tagNET_DVR_SIGNALLAMP_DETCFG)
tagNET_DVR_SIGNALLAMP_DETCFG = struct_tagNET_DVR_SIGNALLAMP_DETCFG
