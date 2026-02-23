from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TRACK_PARAMCFG(Structure):
    pass

_S(struct_tagNET_DVR_TRACK_PARAMCFG, [
    ('dwSize', DWORD),
    ('wAlarmDelayTime', WORD),
    ('wTrackHoldTime', WORD),
    ('byTrackMode', BYTE),
    ('byPreDirection', BYTE),
    ('byTrackSmooth', BYTE),
    ('byZoomAdjust', BYTE),
    ('byMaxTrackZoom', BYTE),
    ('byStopTrackWhenFindFace', BYTE),
    ('byStopTrackThreshold', BYTE),
    ('byRes', BYTE * 9),
])

NET_DVR_TRACK_PARAMCFG = struct_tagNET_DVR_TRACK_PARAMCFG
LPNET_DVR_TRACK_PARAMCFG = POINTER(struct_tagNET_DVR_TRACK_PARAMCFG)
tagNET_DVR_TRACK_PARAMCFG = struct_tagNET_DVR_TRACK_PARAMCFG
