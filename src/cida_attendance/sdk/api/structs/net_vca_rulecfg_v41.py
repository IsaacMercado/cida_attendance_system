from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_145 import NET_DVR_JPEGPARA
from .net_vca_one_rule_v41 import NET_VCA_ONE_RULE_V41


class struct_tagNET_VCA_RULECFG_V41(Structure):
    pass

_S(struct_tagNET_VCA_RULECFG_V41, [
    ('dwSize', DWORD),
    ('byPicProType', BYTE),
    ('byUpLastAlarm', BYTE),
    ('byPicRecordEnable', BYTE),
    ('byRes1', BYTE),
    ('struPictureParam', NET_DVR_JPEGPARA),
    ('struRule', NET_VCA_ONE_RULE_V41 * 8),
    ('wRelSnapChan', WORD * 3),
    ('byRes', BYTE * 26),
])

NET_VCA_RULECFG_V41 = struct_tagNET_VCA_RULECFG_V41
LPNET_VCA_RULECFG_V41 = POINTER(struct_tagNET_VCA_RULECFG_V41)
tagNET_VCA_RULECFG_V41 = struct_tagNET_VCA_RULECFG_V41
