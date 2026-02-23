from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_XML_CONFIG_OUTPUT(Structure):
    pass

_S(struct_tagNET_DVR_XML_CONFIG_OUTPUT, [
    ('dwSize', DWORD),
    ('lpOutBuffer', POINTER(None)),
    ('dwOutBufferSize', DWORD),
    ('dwReturnedXMLSize', DWORD),
    ('lpStatusBuffer', POINTER(None)),
    ('dwStatusSize', DWORD),
    ('lpDataBuffer', POINTER(None)),
    ('byNumOfMultiPart', BYTE),
    ('byRes', BYTE * 23),
])

NET_DVR_XML_CONFIG_OUTPUT = struct_tagNET_DVR_XML_CONFIG_OUTPUT
LPNET_DVR_XML_CONFIG_OUTPUT = POINTER(struct_tagNET_DVR_XML_CONFIG_OUTPUT)
tagNET_DVR_XML_CONFIG_OUTPUT = struct_tagNET_DVR_XML_CONFIG_OUTPUT
