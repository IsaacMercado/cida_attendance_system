from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_145 import NET_DVR_JPEGPARA
from .net_dvr_ptz_position import NET_DVR_PTZ_POSITION
from .net_vca_one_rule_v42 import NET_VCA_ONE_RULE_V42


class struct_tagNET_VCA_RULECFG_V42(Structure):
    pass

_S(struct_tagNET_VCA_RULECFG_V42, [
    ('dwSize', DWORD),
    ('byPicProType', BYTE),
    ('byUpLastAlarm', BYTE),
    ('byPicRecordEnable', BYTE),
    ('byRes1', BYTE),
    ('struPicParam', NET_DVR_JPEGPARA),
    ('struRule', NET_VCA_ONE_RULE_V42 * 16),
    ('wRelSnapChan', WORD * 3),
    ('byTrackEnable', BYTE),
    ('byRes2', BYTE),
    ('struPTZPosition', NET_DVR_PTZ_POSITION),
    ('wTrackDuration', WORD),
    ('wIntervalTime', WORD),
    ('wHeightLimit', WORD),
    ('byRes', BYTE * 58),
])

NET_VCA_RULECFG_V42 = struct_tagNET_VCA_RULECFG_V42
LPNET_VCA_RULECFG_V42 = POINTER(struct_tagNET_VCA_RULECFG_V42)
tagNET_VCA_RULECFG_V42 = struct_tagNET_VCA_RULECFG_V42
