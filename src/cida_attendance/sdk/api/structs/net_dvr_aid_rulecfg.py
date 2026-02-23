from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_145 import NET_DVR_JPEGPARA
from .net_dvr_one_aid_rule import NET_DVR_ONE_AID_RULE


class struct_tagNET_DVR_AID_RULECFG(Structure):
    pass

_S(struct_tagNET_DVR_AID_RULECFG, [
    ('dwSize', DWORD),
    ('byPicProType', BYTE),
    ('byRes1', BYTE * 3),
    ('struPictureParam', NET_DVR_JPEGPARA),
    ('struOneAIDRule', NET_DVR_ONE_AID_RULE * 8),
    ('byRes2', BYTE * 32),
])

NET_DVR_AID_RULECFG = struct_tagNET_DVR_AID_RULECFG
LPNET_DVR_AID_RULECFG = POINTER(struct_tagNET_DVR_AID_RULECFG)
tagNET_DVR_AID_RULECFG = struct_tagNET_DVR_AID_RULECFG
