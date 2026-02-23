from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MONITOR_VQDCFG(Structure):
    pass

_S(struct_tagNET_DVR_MONITOR_VQDCFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byDevType', BYTE),
    ('bySignalPoint', BYTE),
    ('byBlurPoint', BYTE),
    ('byLumaPoint', BYTE),
    ('byChromaPoint', BYTE),
    ('bySnowPoint', BYTE),
    ('byStreakPoint', BYTE),
    ('byFreezePoint', BYTE),
    ('byPTZPoint', BYTE),
    ('byMonitorDel', BYTE),
    ('byContrastThreshold', BYTE),
    ('byMonoThreshold', BYTE),
    ('byShakeThreshold', BYTE),
    ('byFlashThreshold', BYTE),
    ('byCoverThreshold', BYTE),
    ('bySceneThreshold', BYTE),
    ('byDarkThreshold', BYTE),
    ('byRes', BYTE * 46),
])

NET_DVR_MONITOR_VQDCFG = struct_tagNET_DVR_MONITOR_VQDCFG
LPNET_DVR_MONITOR_VQDCFG = POINTER(struct_tagNET_DVR_MONITOR_VQDCFG)
tagNET_DVR_MONITOR_VQDCFG = struct_tagNET_DVR_MONITOR_VQDCFG
