from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_label_identify import NET_DVR_LABEL_IDENTIFY


class struct_tagNET_DVR_MOD_LABEL_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_MOD_LABEL_PARAM, [
    ('struIndentify', NET_DVR_LABEL_IDENTIFY),
    ('byRes1', BYTE * 24),
    ('sLabelName', BYTE * 40),
    ('byRes2', BYTE * 40),
])

NET_DVR_MOD_LABEL_PARAM = struct_tagNET_DVR_MOD_LABEL_PARAM
LPNET_DVR_MOD_LABEL_PARAM = POINTER(struct_tagNET_DVR_MOD_LABEL_PARAM)
tagNET_DVR_MOD_LABEL_PARAM = struct_tagNET_DVR_MOD_LABEL_PARAM
