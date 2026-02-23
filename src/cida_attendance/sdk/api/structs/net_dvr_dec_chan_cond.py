from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DEC_CHAN_COND(Structure):
    pass

_S(struct_tagNET_DVR_DEC_CHAN_COND, [
    ('dwSize', DWORD),
    ('dwSlotNum', DWORD),
    ('dwDecChan', DWORD),
    ('byRes', BYTE * 16),
])

NET_DVR_DEC_CHAN_COND = struct_tagNET_DVR_DEC_CHAN_COND
LPNET_DVR_DEC_CHAN_COND = POINTER(struct_tagNET_DVR_DEC_CHAN_COND)
tagNET_DVR_DEC_CHAN_COND = struct_tagNET_DVR_DEC_CHAN_COND
