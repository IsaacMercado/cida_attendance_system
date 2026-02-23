from ctypes import Structure, c_int

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_GEOGLOCATION(Structure):
    pass

_S(struct_tagNET_DVR_GEOGLOCATION, [
    ('iRes', c_int * 2),
    ('dwCity', DWORD),
])

NET_DVR_GEOGLOCATION = struct_tagNET_DVR_GEOGLOCATION
LPNET_DVR_GEOGLOCATION = POINTER(struct_tagNET_DVR_GEOGLOCATION)
tagNET_DVR_GEOGLOCATION = struct_tagNET_DVR_GEOGLOCATION
