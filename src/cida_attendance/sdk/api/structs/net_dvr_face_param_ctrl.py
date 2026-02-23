from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_del_face_param_mode import NET_DVR_DEL_FACE_PARAM_MODE


class struct_tagNET_DVR_FACE_PARAM_CTRL(Structure):
    pass

_S(struct_tagNET_DVR_FACE_PARAM_CTRL, [
    ('dwSize', DWORD),
    ('byMode', BYTE),
    ('byRes1', BYTE * 3),
    ('struProcessMode', NET_DVR_DEL_FACE_PARAM_MODE),
    ('byRes', BYTE * 64),
])

NET_DVR_FACE_PARAM_CTRL = struct_tagNET_DVR_FACE_PARAM_CTRL
LPNET_DVR_FACE_PARAM_CTRL = POINTER(struct_tagNET_DVR_FACE_PARAM_CTRL)
tagNET_DVR_FACE_PARAM_CTRL = struct_tagNET_DVR_FACE_PARAM_CTRL
