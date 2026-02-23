from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_145 import NET_DVR_JPEGPARA
from .net_vca_one_rule import NET_VCA_ONE_RULE


class struct_tagNET_VCA_RULECFG(Structure):
    pass

_S(struct_tagNET_VCA_RULECFG, [
    ('dwSize', DWORD),
    ('byPicProType', BYTE),
    ('byUpLastAlarm', BYTE),
    ('byPicRecordEnable', BYTE),
    ('byRes', BYTE),
    ('struPictureParam', NET_DVR_JPEGPARA),
    ('struRule', NET_VCA_ONE_RULE * 8),
])

NET_VCA_RULECFG = struct_tagNET_VCA_RULECFG
LPNET_VCA_RULECFG = POINTER(struct_tagNET_VCA_RULECFG)
tagNET_VCA_RULECFG = struct_tagNET_VCA_RULECFG
