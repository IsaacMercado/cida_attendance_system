from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_channel import NET_DVR_CHANNEL
from .net_dvr_track_calibration_param_v41 import NET_DVR_TRACK_CALIBRATION_PARAM_V41


class struct_tagNET_DVR_TRACK_DEV_PARAM_(Structure):
    pass

_S(struct_tagNET_DVR_TRACK_DEV_PARAM_, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byTransMode', BYTE),
    ('byRes1', BYTE * 2),
    ('struTrackDevChan', NET_DVR_CHANNEL),
    ('struCalParam', NET_DVR_TRACK_CALIBRATION_PARAM_V41),
    ('byRes2', BYTE * 256),
])

NET_DVR_TRACK_DEV_PARAM = struct_tagNET_DVR_TRACK_DEV_PARAM_
LPNET_DVR_TRACK_DEV_PARAM = POINTER(struct_tagNET_DVR_TRACK_DEV_PARAM_)
tagNET_DVR_TRACK_DEV_PARAM_ = struct_tagNET_DVR_TRACK_DEV_PARAM_
