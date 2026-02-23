from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_REL_CAPTURE_CHAN_V40(Structure):
    pass

_S(struct_tagNET_DVR_REL_CAPTURE_CHAN_V40, [
    ('dwMaxRelCaptureChanNum', DWORD),
    ('dwChanNo', DWORD * 512),
    ('byRes', BYTE * 32),
])

NET_DVR_REL_CAPTURE_CHAN_V40 = struct_tagNET_DVR_REL_CAPTURE_CHAN_V40
LPNET_DVR_REL_CAPTURE_CHAN_V40 = POINTER(struct_tagNET_DVR_REL_CAPTURE_CHAN_V40)
tagNET_DVR_REL_CAPTURE_CHAN_V40 = struct_tagNET_DVR_REL_CAPTURE_CHAN_V40
