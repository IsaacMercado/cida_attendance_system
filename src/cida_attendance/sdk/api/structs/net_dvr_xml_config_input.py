from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_XML_CONFIG_INPUT(Structure):
    pass

_S(struct_tagNET_DVR_XML_CONFIG_INPUT, [
    ('dwSize', DWORD),
    ('lpRequestUrl', POINTER(None)),
    ('dwRequestUrlLen', DWORD),
    ('lpInBuffer', POINTER(None)),
    ('dwInBufferSize', DWORD),
    ('dwRecvTimeOut', DWORD),
    ('byForceEncrpt', BYTE),
    ('byNumOfMultiPart', BYTE),
    ('byMIMEType', BYTE),
    ('byRes', BYTE * 29),
])

NET_DVR_XML_CONFIG_INPUT = struct_tagNET_DVR_XML_CONFIG_INPUT
LPNET_DVR_XML_CONFIG_INPUT = POINTER(struct_tagNET_DVR_XML_CONFIG_INPUT)
tagNET_DVR_XML_CONFIG_INPUT = struct_tagNET_DVR_XML_CONFIG_INPUT
