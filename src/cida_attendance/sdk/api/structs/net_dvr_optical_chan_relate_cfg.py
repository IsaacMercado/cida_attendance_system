from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_OPTICAL_CHAN_RELATE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_OPTICAL_CHAN_RELATE_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('dwDevNo', DWORD),
    ('dwOpticalPort', DWORD),
    ('byDevID', BYTE * 48),
    ('dwInputChanNo', DWORD),
    ('byRes2', BYTE * 64),
])

NET_DVR_OPTICAL_CHAN_RELATE_CFG = struct_tagNET_DVR_OPTICAL_CHAN_RELATE_CFG
LPNET_DVR_OPTICAL_CHAN_RELATE_CFG = POINTER(struct_tagNET_DVR_OPTICAL_CHAN_RELATE_CFG)
tagNET_DVR_OPTICAL_CHAN_RELATE_CFG = struct_tagNET_DVR_OPTICAL_CHAN_RELATE_CFG
