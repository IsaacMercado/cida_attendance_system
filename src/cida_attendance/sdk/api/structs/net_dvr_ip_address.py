from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNet_DVR_IP_ADDRESS(Structure):
    pass

_S(struct_tagNet_DVR_IP_ADDRESS, [
    ('byDevAddress', BYTE * 64),
    ('wDevPort', WORD),
    ('byres', BYTE * 134),
])

NET_DVR_IP_ADDRESS = struct_tagNet_DVR_IP_ADDRESS
LPNET_DVR_IP_ADDRESS = POINTER(struct_tagNet_DVR_IP_ADDRESS)
tagNet_DVR_IP_ADDRESS = struct_tagNet_DVR_IP_ADDRESS
