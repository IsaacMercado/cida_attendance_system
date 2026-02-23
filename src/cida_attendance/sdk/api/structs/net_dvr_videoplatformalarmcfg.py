from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_7 import NET_DVR_HANDLEEXCEPTION_V30
from .net_dvr_boardalarmcfg import NET_DVR_BOARDALARMCFG
from .net_dvr_temperaturealarmcfg import NET_DVR_TEMPERATUREALARMCFG


class struct_tagNET_DVR_VIDEOPLATFORMALARMCFG(Structure):
    pass

_S(struct_tagNET_DVR_VIDEOPLATFORMALARMCFG, [
    ('dwSize', DWORD),
    ('struTempAlarmCfg', NET_DVR_TEMPERATUREALARMCFG),
    ('struBoardAlarmCfg', NET_DVR_BOARDALARMCFG),
    ('struHandleException', NET_DVR_HANDLEEXCEPTION_V30 * 16),
    ('byRes', BYTE * 32),
])

NET_DVR_VIDEOPLATFORMALARMCFG = struct_tagNET_DVR_VIDEOPLATFORMALARMCFG
LPNET_DVR_VIDEOPLATFORMALARMCFG = POINTER(struct_tagNET_DVR_VIDEOPLATFORMALARMCFG)
tagNET_DVR_VIDEOPLATFORMALARMCFG = struct_tagNET_DVR_VIDEOPLATFORMALARMCFG
