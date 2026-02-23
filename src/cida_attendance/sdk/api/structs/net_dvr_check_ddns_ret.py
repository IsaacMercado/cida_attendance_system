from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_query_ddns_ret import NET_DVR_QUERY_DDNS_RET


class struct_tagNET_DVR_CHECK_DDNS_RET(Structure):
    pass

_S(struct_tagNET_DVR_CHECK_DDNS_RET, [
    ('byDevStatus', BYTE),
    ('byRes1', BYTE),
    ('struQueryRet', NET_DVR_QUERY_DDNS_RET),
    ('wRegionID', WORD),
    ('byRes2', BYTE * 508),
])

NET_DVR_CHECK_DDNS_RET = struct_tagNET_DVR_CHECK_DDNS_RET
LPNET_DVR_CHECK_DDNS_RET = POINTER(struct_tagNET_DVR_CHECK_DDNS_RET)
tagNET_DVR_CHECK_DDNS_RET = struct_tagNET_DVR_CHECK_DDNS_RET
