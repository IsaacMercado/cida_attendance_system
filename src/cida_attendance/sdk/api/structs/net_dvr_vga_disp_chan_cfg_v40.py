from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_318 import union_anon_318


class struct_tagNET_DVR_VGA_DISP_CHAN_CFG_V40(Structure):
    pass

_S(struct_tagNET_DVR_VGA_DISP_CHAN_CFG_V40, [
    ('dwSize', DWORD),
    ('byAudio', BYTE),
    ('byAudioWindowIdx', BYTE),
    ('byVgaResolution', BYTE),
    ('byVedioFormat', BYTE),
    ('dwWindowMode', DWORD),
    ('byJoinDecChan', BYTE * 16),
    ('byEnlargeStatus', BYTE),
    ('byEnlargeSubWindowIndex', BYTE),
    ('byScale', BYTE),
    ('byUnionType', BYTE),
    ('struDiff', union_anon_318),
    ('byRes', BYTE * 120),
])

NET_DVR_VGA_DISP_CHAN_CFG_V40 = struct_tagNET_DVR_VGA_DISP_CHAN_CFG_V40
LPNET_DVR_VGA_DISP_CHAN_CFG_V40 = POINTER(struct_tagNET_DVR_VGA_DISP_CHAN_CFG_V40)
tagNET_DVR_VGA_DISP_CHAN_CFG_V40 = struct_tagNET_DVR_VGA_DISP_CHAN_CFG_V40
