from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_REL_CAPTURE_CHAN(Structure):
    pass

_S(struct_tagNET_DVR_REL_CAPTURE_CHAN, [
    ('byChan', BYTE * 16),
    ('byRes', BYTE * 20),
])

NET_DVR_REL_CAPTURE_CHAN = struct_tagNET_DVR_REL_CAPTURE_CHAN
LPNET_DVR_REL_CAPTURE_CHAN = POINTER(struct_tagNET_DVR_REL_CAPTURE_CHAN)
tagNET_DVR_REL_CAPTURE_CHAN = struct_tagNET_DVR_REL_CAPTURE_CHAN
