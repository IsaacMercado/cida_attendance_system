from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_REMOTE_CTRL_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_REMOTE_CTRL_PARAM, [
    ('byRemoteCtrlCmd', BYTE),
    ('byRes1', BYTE * 3),
    ('dwCtrlParam', DWORD),
    ('byRes2', BYTE * 8),
])

NET_DVR_REMOTE_CTRL_PARAM = struct_tagNET_DVR_REMOTE_CTRL_PARAM
LPNET_DVR_REMOTE_CTRL_PARAM = POINTER(struct_tagNET_DVR_REMOTE_CTRL_PARAM)
tagNET_DVR_REMOTE_CTRL_PARAM = struct_tagNET_DVR_REMOTE_CTRL_PARAM
