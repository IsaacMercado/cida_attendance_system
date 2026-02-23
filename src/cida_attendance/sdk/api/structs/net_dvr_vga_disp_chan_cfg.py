from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_182 import union_anon_182


class struct_tagNET_DVR_VGA_DISP_CHAN_CFG(Structure):
    pass

_S(struct_tagNET_DVR_VGA_DISP_CHAN_CFG, [
    ('dwSize', DWORD),
    ('byAudio', BYTE),
    ('byAudioWindowIdx', BYTE),
    ('byVgaResolution', BYTE),
    ('byVedioFormat', BYTE),
    ('dwWindowMode', DWORD),
    ('byJoinDecChan', BYTE * 16),
    ('byEnlargeStatus', BYTE),
    ('byEnlargeSubWindowIndex', BYTE),
    ('struDiff', union_anon_182),
    ('byUnionType', BYTE),
    ('byScale', BYTE),
])

NET_DVR_VGA_DISP_CHAN_CFG = struct_tagNET_DVR_VGA_DISP_CHAN_CFG
LPNET_DVR_VGA_DISP_CHAN_CFG = POINTER(struct_tagNET_DVR_VGA_DISP_CHAN_CFG)
tagNET_DVR_VGA_DISP_CHAN_CFG = struct_tagNET_DVR_VGA_DISP_CHAN_CFG
