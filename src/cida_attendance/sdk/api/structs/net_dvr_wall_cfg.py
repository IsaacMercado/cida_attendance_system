from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_substream_switch_cfg import NET_DVR_SUBSTREAM_SWITCH_CFG


class struct_tagNET_DVR_WALL_CFG(Structure):
    pass

_S(struct_tagNET_DVR_WALL_CFG, [
    ('dwSize', DWORD),
    ('byTransparency', BYTE),
    ('byWinStaticMode', BYTE),
    ('byStreamFailedMode', BYTE),
    ('byEnabledOverlayLogo', BYTE),
    ('struSubStreamSwitch', NET_DVR_SUBSTREAM_SWITCH_CFG),
    ('byLEDShowMode', BYTE),
    ('byLowLatencyMode', BYTE),
    ('byRes', BYTE * 50),
])

NET_DVR_WALL_CFG = struct_tagNET_DVR_WALL_CFG
LPNET_DVR_WALL_CFG = POINTER(struct_tagNET_DVR_WALL_CFG)
tagNET_DVR_WALL_CFG = struct_tagNET_DVR_WALL_CFG
