from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SOFTWARE_SERVICE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_SOFTWARE_SERVICE_CFG, [
    ('dwSize', DWORD),
    ('byThirdStreamEnabled', BYTE),
    ('bySubStreamEnabled', BYTE),
    ('byRes', BYTE * 254),
])

NET_DVR_SOFTWARE_SERVICE_CFG = struct_tagNET_DVR_SOFTWARE_SERVICE_CFG
LPNET_DVR_SOFTWARE_SERVICE_CFG = POINTER(struct_tagNET_DVR_SOFTWARE_SERVICE_CFG)
tagNET_DVR_SOFTWARE_SERVICE_CFG = struct_tagNET_DVR_SOFTWARE_SERVICE_CFG
