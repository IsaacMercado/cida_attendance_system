from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_pu_stream_cfg import NET_DVR_PU_STREAM_CFG
from .net_dvr_videoeffect import NET_DVR_VIDEOEFFECT


class struct_tagNET_DVR_INPUTSTREAMCFG_V40(Structure):
    pass

_S(struct_tagNET_DVR_INPUTSTREAMCFG_V40, [
    ('dwSize', DWORD),
    ('byValid', BYTE),
    ('byCamMode', BYTE),
    ('wInputNo', WORD),
    ('sCamName', BYTE * 32),
    ('struVideoEffect', NET_DVR_VIDEOEFFECT),
    ('struPuStream', NET_DVR_PU_STREAM_CFG),
    ('wBoardNum', WORD),
    ('wInputIdxOnBoard', WORD),
    ('dwResolution', DWORD),
    ('byVideoFormat', BYTE),
    ('byStatus', BYTE),
    ('sGroupName', BYTE * 32),
    ('byJointMatrix', BYTE),
    ('byJointNo', BYTE),
    ('byColorMode', BYTE),
    ('byScreenServer', BYTE),
    ('byDevNo', BYTE),
    ('byRes1', BYTE),
    ('dwInputSignalNo', DWORD),
    ('byVideoEnctype', BYTE),
    ('byAudioEnctype', BYTE),
    ('byWallStatus', BYTE),
    ('byRes', BYTE * 117),
])

NET_DVR_INPUTSTREAMCFG_V40 = struct_tagNET_DVR_INPUTSTREAMCFG_V40
LPNET_DVR_INPUTSTREAMCFG_V40 = POINTER(struct_tagNET_DVR_INPUTSTREAMCFG_V40)
tagNET_DVR_INPUTSTREAMCFG_V40 = struct_tagNET_DVR_INPUTSTREAMCFG_V40
