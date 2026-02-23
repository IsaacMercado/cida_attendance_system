from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CHANS_RECORD_STATUS_CFG(Structure):
    pass

_S(struct_tagNET_DVR_CHANS_RECORD_STATUS_CFG, [
    ('dwSize', DWORD),
    ('byValid', BYTE),
    ('byRecord', BYTE),
    ('dwRelatedHD', DWORD),
    ('byOffLineRecord', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_CHAN_RECORD_STATUS_CFG = struct_tagNET_DVR_CHANS_RECORD_STATUS_CFG
LPNET_DVR_CHAN_RECORD_STATUS_CFG = POINTER(struct_tagNET_DVR_CHANS_RECORD_STATUS_CFG)
tagNET_DVR_CHANS_RECORD_STATUS_CFG = struct_tagNET_DVR_CHANS_RECORD_STATUS_CFG
