from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_IMAGEOVERLAYCFG(Structure):
    pass

_S(struct_tagNET_DVR_IMAGEOVERLAYCFG, [
    ('dwSize', DWORD),
    ('byOverlayInfo', BYTE),
    ('byOverlayMonitorInfo', BYTE),
    ('byOverlayTime', BYTE),
    ('byOverlaySpeed', BYTE),
    ('byOverlaySpeeding', BYTE),
    ('byOverlayLimitFlag', BYTE),
    ('byOverlayPlate', BYTE),
    ('byOverlayColor', BYTE),
    ('byOverlayLength', BYTE),
    ('byOverlayType', BYTE),
    ('byOverlayColorDepth', BYTE),
    ('byOverlayDriveChan', BYTE),
    ('byOverlayMilliSec', BYTE),
    ('byOverlayIllegalInfo', BYTE),
    ('byOverlayRedOnTime', BYTE),
    ('byFarAddPlateJpeg', BYTE),
    ('byNearAddPlateJpeg', BYTE),
    ('byRes1', BYTE * 3),
    ('byMonitorInfo1', BYTE * 32),
    ('byMonitorInfo2', BYTE * 44),
    ('byRes2', BYTE * 52),
])

NET_DVR_IMAGEOVERLAYCFG = struct_tagNET_DVR_IMAGEOVERLAYCFG
LPNET_DVR_IMAGEOVERLAYCFG = POINTER(struct_tagNET_DVR_IMAGEOVERLAYCFG)
tagNET_DVR_IMAGEOVERLAYCFG = struct_tagNET_DVR_IMAGEOVERLAYCFG
