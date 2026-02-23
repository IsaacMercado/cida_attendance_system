from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_itc_icr_param_union import NET_ITC_ICR_PARAM_UNION


class struct_tagNET_ITC_ICRCFG(Structure):
    pass

_S(struct_tagNET_ITC_ICRCFG, [
    ('dwSize', DWORD),
    ('bySwitchType', BYTE),
    ('byRes', BYTE * 3),
    ('uICRParam', NET_ITC_ICR_PARAM_UNION),
])

NET_ITC_ICRCFG = struct_tagNET_ITC_ICRCFG
LPNET_ITC_ICRCFG = POINTER(struct_tagNET_ITC_ICRCFG)
tagNET_ITC_ICRCFG = struct_tagNET_ITC_ICRCFG
