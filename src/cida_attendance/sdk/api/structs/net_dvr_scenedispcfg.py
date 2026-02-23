from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_rectcfg import NET_DVR_RECTCFG


class struct_tagNET_DVR_SCENEDISPCFG(Structure):
    pass

_S(struct_tagNET_DVR_SCENEDISPCFG, [
    ('byEnable', BYTE),
    ('bySoltNum', BYTE),
    ('byRes1', BYTE * 2),
    ('byDispChanNum', BYTE),
    ('byAudio', BYTE),
    ('byAudioWindowIdx', BYTE),
    ('byVedioFormat', BYTE),
    ('byWindowMode', BYTE),
    ('byEnlargeStatus', BYTE),
    ('byEnlargeSubWindowIndex', BYTE),
    ('byScale', BYTE),
    ('dwResolution', DWORD),
    ('byJoinDecChan', BYTE * 36),
    ('byJoinDecoderId', BYTE * 36),
    ('byDecResolution', BYTE * 36),
    ('byRow', BYTE),
    ('byColumn', BYTE),
    ('byRes2', BYTE * 5),
    ('struDisp', NET_DVR_RECTCFG),
])

NET_DVR_SCENEDISPCFG = struct_tagNET_DVR_SCENEDISPCFG
LPNET_DVR_SCENEDISPCFG = POINTER(struct_tagNET_DVR_SCENEDISPCFG)
tagNET_DVR_SCENEDISPCFG = struct_tagNET_DVR_SCENEDISPCFG
