from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME


class struct_tagNET_ITC_ICRTIMECFG(Structure):
    pass

_S(struct_tagNET_ITC_ICRTIMECFG, [
    ('struTime', NET_DVR_SCHEDTIME),
    ('byAssociateRresetNo', BYTE),
    ('bySubSwitchMode', BYTE),
    ('byRes', BYTE * 10),
])

NET_ITC_ICRTIMECFG = struct_tagNET_ITC_ICRTIMECFG
LPNET_ITC_ICRTIMECFG = POINTER(struct_tagNET_ITC_ICRTIMECFG)
tagNET_ITC_ICRTIMECFG = struct_tagNET_ITC_ICRTIMECFG
