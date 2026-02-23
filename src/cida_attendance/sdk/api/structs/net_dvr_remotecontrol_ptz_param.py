from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_point import NET_VCA_POINT


class struct_tagNET_DVR_REMOTECONTROL_PTZ_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_REMOTECONTROL_PTZ_PARAM, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('dwPTZCommand', DWORD),
    ('struVcaPoint', NET_VCA_POINT),
    ('dwSpeed', DWORD),
    ('dwStop', DWORD),
    ('byRes', BYTE * 32),
])

NET_DVR_REMOTECONTROL_PTZ_PARAM = struct_tagNET_DVR_REMOTECONTROL_PTZ_PARAM
LPNET_DVR_REMOTECONTROL_PTZ_PARAM = POINTER(struct_tagNET_DVR_REMOTECONTROL_PTZ_PARAM)
tagNET_DVR_REMOTECONTROL_PTZ_PARAM = struct_tagNET_DVR_REMOTECONTROL_PTZ_PARAM
