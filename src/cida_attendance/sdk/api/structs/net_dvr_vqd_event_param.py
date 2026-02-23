from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VQD_EVENT_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_VQD_EVENT_PARAM, [
    ('byThreshold', BYTE),
    ('byTriggerMode', BYTE),
    ('byUploadPic', BYTE),
    ('byRes1', BYTE),
    ('dwTimeInterval', DWORD),
    ('byRes2', BYTE * 64),
])

NET_DVR_VQD_EVENT_PARAM = struct_tagNET_DVR_VQD_EVENT_PARAM
LPNET_DVR_VQD_EVENT_PARAM = POINTER(struct_tagNET_DVR_VQD_EVENT_PARAM)
tagNET_DVR_VQD_EVENT_PARAM = struct_tagNET_DVR_VQD_EVENT_PARAM
