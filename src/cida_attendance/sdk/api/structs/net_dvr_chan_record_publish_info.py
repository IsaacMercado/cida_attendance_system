from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CHAN_RECORD_PUBLISH_INFO(Structure):
    pass

_S(struct_tagNET_DVR_CHAN_RECORD_PUBLISH_INFO, [
    ('byPublish', BYTE),
    ('byRes1', BYTE * 3),
    ('dwStreamType', DWORD),
    ('byRes', BYTE * 12),
])

NET_DVR_RECORD_PUBLISH_INFO = struct_tagNET_DVR_CHAN_RECORD_PUBLISH_INFO
LPNET_DVR_RECORD_PUBLISH_INFO = POINTER(struct_tagNET_DVR_CHAN_RECORD_PUBLISH_INFO)
tagNET_DVR_CHAN_RECORD_PUBLISH_INFO = struct_tagNET_DVR_CHAN_RECORD_PUBLISH_INFO
