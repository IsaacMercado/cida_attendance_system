from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_V6SUBSYSTEMPARAM(Structure):
    pass

_S(struct_tagNET_DVR_V6SUBSYSTEMPARAM, [
    ('bySerialTrans', BYTE),
    ('byRes', BYTE * 35),
])

NET_DVR_V6SUBSYSTEMPARAM = struct_tagNET_DVR_V6SUBSYSTEMPARAM
LPNET_DVR_V6SUBSYSTEMPARAM = POINTER(struct_tagNET_DVR_V6SUBSYSTEMPARAM)
tagNET_DVR_V6SUBSYSTEMPARAM = struct_tagNET_DVR_V6SUBSYSTEMPARAM
