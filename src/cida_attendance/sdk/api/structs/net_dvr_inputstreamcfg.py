from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_pu_stream_cfg import NET_DVR_PU_STREAM_CFG
from .net_dvr_videoeffect import NET_DVR_VIDEOEFFECT


class struct_tagNET_DVR_INPUTSTREAMCFG(Structure):
    pass

_S(struct_tagNET_DVR_INPUTSTREAMCFG, [
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
    ('byRes', BYTE),
])

NET_DVR_INPUTSTREAMCFG = struct_tagNET_DVR_INPUTSTREAMCFG
LPNET_DVR_INPUTSTREAMCFG = POINTER(struct_tagNET_DVR_INPUTSTREAMCFG)
tagNET_DVR_INPUTSTREAMCFG = struct_tagNET_DVR_INPUTSTREAMCFG
