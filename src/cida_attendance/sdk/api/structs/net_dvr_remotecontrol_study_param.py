from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_REMOTECONTROL_STUDY_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_REMOTECONTROL_STUDY_PARAM, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byRes', BYTE * 16),
])

NET_DVR_REMOTECONTROL_STUDY_PARAM = struct_tagNET_DVR_REMOTECONTROL_STUDY_PARAM
LPNET_DVR_REMOTECONTROL_STUDY_PARAM = POINTER(struct_tagNET_DVR_REMOTECONTROL_STUDY_PARAM)
tagNET_DVR_REMOTECONTROL_STUDY_PARAM = struct_tagNET_DVR_REMOTECONTROL_STUDY_PARAM
