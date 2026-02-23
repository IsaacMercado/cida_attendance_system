from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_label_identify import NET_DVR_LABEL_IDENTIFY


class struct_tagNET_DVR_DEL_LABEL_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_DEL_LABEL_PARAM, [
    ('dwSize', DWORD),
    ('byMode', BYTE),
    ('byRes1', BYTE),
    ('wLabelNum', WORD),
    ('struIndentify', NET_DVR_LABEL_IDENTIFY * 20),
    ('byRes2', BYTE * 160),
])

NET_DVR_DEL_LABEL_PARAM = struct_tagNET_DVR_DEL_LABEL_PARAM
LPNET_DVR_DEL_LABEL_PARAM = POINTER(struct_tagNET_DVR_DEL_LABEL_PARAM)
tagNET_DVR_DEL_LABEL_PARAM = struct_tagNET_DVR_DEL_LABEL_PARAM
