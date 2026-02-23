from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LABEL_IDENTIFY(Structure):
    pass

_S(struct_tagNET_DVR_LABEL_IDENTIFY, [
    ('sLabelIdentify', BYTE * 64),
    ('byRes', BYTE * 8),
])

NET_DVR_LABEL_IDENTIFY = struct_tagNET_DVR_LABEL_IDENTIFY
LPNET_DVR_LABEL_IDENTIFY = POINTER(struct_tagNET_DVR_LABEL_IDENTIFY)
tagNET_DVR_LABEL_IDENTIFY = struct_tagNET_DVR_LABEL_IDENTIFY
