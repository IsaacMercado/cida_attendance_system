from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DISP_CHAN_STATUS_V41(Structure):
    pass

_S(struct_tagNET_DVR_DISP_CHAN_STATUS_V41, [
    ('byDispStatus', BYTE),
    ('byBVGA', BYTE),
    ('byVideoFormat', BYTE),
    ('byWindowMode', BYTE),
    ('byJoinDecChan', BYTE * 36),
    ('byFpsDisp', BYTE * 36),
    ('byScreenMode', BYTE),
    ('byRes1', BYTE * 3),
    ('dwDispChan', DWORD),
    ('byRes2', BYTE * 24),
])

NET_DVR_DISP_CHAN_STATUS_V41 = struct_tagNET_DVR_DISP_CHAN_STATUS_V41
LPNET_DVR_DISP_CHAN_STATUS_V41 = POINTER(struct_tagNET_DVR_DISP_CHAN_STATUS_V41)
tagNET_DVR_DISP_CHAN_STATUS_V41 = struct_tagNET_DVR_DISP_CHAN_STATUS_V41
