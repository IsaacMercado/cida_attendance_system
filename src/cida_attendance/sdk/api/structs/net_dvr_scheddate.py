from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SCHEDDATE(Structure):
    pass

_S(struct_tagNET_DVR_SCHEDDATE, [
    ('byStartMonth', BYTE),
    ('byStartDay', BYTE),
    ('byStopMonth', BYTE),
    ('byStopDay', BYTE),
])

NET_DVR_SCHEDDATE = struct_tagNET_DVR_SCHEDDATE
LPNET_DVR_SCHEDDATE = POINTER(struct_tagNET_DVR_SCHEDDATE)
tagNET_DVR_SCHEDDATE = struct_tagNET_DVR_SCHEDDATE
