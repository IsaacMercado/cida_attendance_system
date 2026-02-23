from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_GAIN(Structure):
    pass

_S(struct_tagNET_DVR_GAIN, [
    ('byGainLevel', BYTE),
    ('byGainUserSet', BYTE),
    ('byRes', BYTE * 2),
    ('dwMaxGainValue', DWORD),
])

NET_DVR_GAIN = struct_tagNET_DVR_GAIN
LPNET_DVR_GAIN = POINTER(struct_tagNET_DVR_GAIN)
tagNET_DVR_GAIN = struct_tagNET_DVR_GAIN
