from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct__NET_DVR_PTZ_TRACK_PARAM_(Structure):
    pass

_S(struct__NET_DVR_PTZ_TRACK_PARAM_, [
    ('dwSize', DWORD),
    ('byTrackMode', BYTE),
    ('byLinkageTarget', BYTE),
    ('byAutoTrackEnable', BYTE),
    ('byRes1', BYTE),
    ('dwTrackTime', DWORD),
    ('byRes2', BYTE * 256),
])

NET_DVR_PTZ_TRACK_PARAM = struct__NET_DVR_PTZ_TRACK_PARAM_
LPNET_DVR_PTZ_TRACK_PARAM = POINTER(struct__NET_DVR_PTZ_TRACK_PARAM_)
_NET_DVR_PTZ_TRACK_PARAM_ = struct__NET_DVR_PTZ_TRACK_PARAM_
