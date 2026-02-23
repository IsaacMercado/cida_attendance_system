from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CHANS_RECORD_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_CHANS_RECORD_STATUS, [
    ('byValid', BYTE),
    ('byRecord', BYTE),
    ('wChannelNO', WORD),
    ('dwRelatedHD', DWORD),
    ('byOffLineRecord', BYTE),
    ('byRes', BYTE * 7),
])

NET_DVR_CHANS_RECORD_STATUS = struct_tagNET_DVR_CHANS_RECORD_STATUS
LPNET_DVR_CHANS_RECORD_STATUS = POINTER(struct_tagNET_DVR_CHANS_RECORD_STATUS)
tagNET_DVR_CHANS_RECORD_STATUS = struct_tagNET_DVR_CHANS_RECORD_STATUS
