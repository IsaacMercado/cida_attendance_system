from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_IPDEVINFO_V31(Structure):
    pass

_S(struct_tagNET_DVR_IPDEVINFO_V31, [
    ('byEnable', BYTE),
    ('byProType', BYTE),
    ('byEnableQuickAdd', BYTE),
    ('byCameraType', BYTE),
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('byDomain', BYTE * 64),
    ('struIP', NET_DVR_IPADDR),
    ('wDVRPort', WORD),
    ('szDeviceID', BYTE * 32),
    ('byEnableTiming', BYTE),
    ('byCertificateValidation', BYTE),
])

NET_DVR_IPDEVINFO_V31 = struct_tagNET_DVR_IPDEVINFO_V31
LPNET_DVR_IPDEVINFO_V31 = POINTER(struct_tagNET_DVR_IPDEVINFO_V31)
tagNET_DVR_IPDEVINFO_V31 = struct_tagNET_DVR_IPDEVINFO_V31
