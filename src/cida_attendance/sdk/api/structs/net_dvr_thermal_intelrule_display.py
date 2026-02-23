from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_rulesline_cfg import NET_DVR_RULESLINE_CFG


class struct_tagNET_DVR_THERMAL_INTELRULE_DISPLAY(Structure):
    pass

_S(struct_tagNET_DVR_THERMAL_INTELRULE_DISPLAY, [
    ('dwSize', DWORD),
    ('byFontSizeType', BYTE),
    ('byRes1', BYTE * 3),
    ('struNormalRulesLineCfg', NET_DVR_RULESLINE_CFG),
    ('struAlertRulesLineCfg', NET_DVR_RULESLINE_CFG),
    ('struAlarmRulesLineCfg', NET_DVR_RULESLINE_CFG),
    ('byRes', BYTE * 640),
])

NET_DVR_THERMAL_INTELRULE_DISPLAY = struct_tagNET_DVR_THERMAL_INTELRULE_DISPLAY
LPNET_DVR_THERMAL_INTELRULE_DISPLAY = POINTER(struct_tagNET_DVR_THERMAL_INTELRULE_DISPLAY)
tagNET_DVR_THERMAL_INTELRULE_DISPLAY = struct_tagNET_DVR_THERMAL_INTELRULE_DISPLAY
