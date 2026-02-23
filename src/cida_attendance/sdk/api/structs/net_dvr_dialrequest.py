from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DIALREQUEST(Structure):
    pass

_S(struct_tagNET_DVR_DIALREQUEST, [
    ('byConnNum', BYTE),
    ('byNetType', BYTE),
    ('byRes', BYTE * 6),
])

NET_DVR_DIALREQUEST = struct_tagNET_DVR_DIALREQUEST
LPNET_DVR_DIALREQUEST = POINTER(struct_tagNET_DVR_DIALREQUEST)
tagNET_DVR_DIALREQUEST = struct_tagNET_DVR_DIALREQUEST
