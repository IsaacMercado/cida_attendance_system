from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_ITC_SERIAL_INFO(Structure):
    pass

_S(struct_tagNET_ITC_SERIAL_INFO, [
    ('bySerialProtocol', BYTE),
    ('byIntervalType', BYTE),
    ('wInterval', WORD),
    ('byNormalPassProtocol', BYTE),
    ('byInverseProtocol', BYTE),
    ('bySpeedProtocol', BYTE),
    ('byRes', BYTE * 9),
])

NET_ITC_SERIAL_INFO = struct_tagNET_ITC_SERIAL_INFO
LPNET_ITC_SERIAL_INFO = POINTER(struct_tagNET_ITC_SERIAL_INFO)
tagNET_ITC_SERIAL_INFO = struct_tagNET_ITC_SERIAL_INFO
