from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_singlesubsystemjoininfo import NET_DVR_SINGLESUBSYSTEMJOININFO


class struct_tagNET_DVR_ALLDECSUBSYSTEMJOININFO(Structure):
    pass

_S(struct_tagNET_DVR_ALLDECSUBSYSTEMJOININFO, [
    ('dwSize', DWORD),
    ('struSingleSubSystemJoinInfo', NET_DVR_SINGLESUBSYSTEMJOININFO * 80),
    ('byRes', BYTE * 8),
])

NET_DVR_ALLDECSUBSYSTEMJOININFO = struct_tagNET_DVR_ALLDECSUBSYSTEMJOININFO
LPNET_DVR_ALLDECSUBSYSTEMJOININFO = POINTER(struct_tagNET_DVR_ALLDECSUBSYSTEMJOININFO)
tagNET_DVR_ALLDECSUBSYSTEMJOININFO = struct_tagNET_DVR_ALLDECSUBSYSTEMJOININFO
