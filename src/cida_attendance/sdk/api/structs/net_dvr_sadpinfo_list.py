from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_sadpinfo import NET_DVR_SADPINFO


class struct_tagNET_DVR_SADPINFO_LIST(Structure):
    pass

_S(struct_tagNET_DVR_SADPINFO_LIST, [
    ('dwSize', DWORD),
    ('wSadpNum', WORD),
    ('byRes', BYTE * 6),
    ('struSadpInfo', NET_DVR_SADPINFO * 256),
])

NET_DVR_SADPINFO_LIST = struct_tagNET_DVR_SADPINFO_LIST
LPNET_DVR_SADPINFO_LIST = POINTER(struct_tagNET_DVR_SADPINFO_LIST)
tagNET_DVR_SADPINFO_LIST = struct_tagNET_DVR_SADPINFO_LIST
