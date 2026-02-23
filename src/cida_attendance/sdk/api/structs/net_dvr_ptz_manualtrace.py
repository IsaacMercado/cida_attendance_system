from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_v30 import NET_DVR_TIME_V30
from .net_vca_point import NET_VCA_POINT


class struct_tagNET_DVR_PTZ_MANUALTRACE(Structure):
    pass

_S(struct_tagNET_DVR_PTZ_MANUALTRACE, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('struPoint', NET_VCA_POINT),
    ('byTrackType', BYTE),
    ('byLinkageType', BYTE),
    ('byRes', BYTE * 2),
    ('struPointEnd', NET_VCA_POINT),
    ('struTime', NET_DVR_TIME_V30),
    ('dwSerialNo', DWORD),
    ('byRes1', BYTE * 36),
])

NET_DVR_PTZ_MANUALTRACE = struct_tagNET_DVR_PTZ_MANUALTRACE
LPNET_DVR_PTZ_MANUALTRACE = POINTER(struct_tagNET_DVR_PTZ_MANUALTRACE)
tagNET_DVR_PTZ_MANUALTRACE = struct_tagNET_DVR_PTZ_MANUALTRACE
