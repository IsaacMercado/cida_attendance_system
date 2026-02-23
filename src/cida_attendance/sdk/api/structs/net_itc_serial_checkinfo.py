from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_ITC_SERIAL_CHECKINFO(Structure):
    pass

_S(struct_tagNET_ITC_SERIAL_CHECKINFO, [
    ('bySerialIndex', BYTE * 8),
    ('byRes', BYTE * 40),
])

NET_ITC_SERIAL_CHECKINFO = struct_tagNET_ITC_SERIAL_CHECKINFO
LPNET_ITC_SERIAL_CHECKINFO = POINTER(struct_tagNET_ITC_SERIAL_CHECKINFO)
tagNET_ITC_SERIAL_CHECKINFO = struct_tagNET_ITC_SERIAL_CHECKINFO
