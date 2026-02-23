from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_STREAMENCRYPTION_CFG(Structure):
    pass

_S(struct_tagNET_DVR_STREAMENCRYPTION_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes', BYTE * 255),
])

NET_DVR_STREAMENCRYPTION_CFG = struct_tagNET_DVR_STREAMENCRYPTION_CFG
LPNET_DVR_STREAMENCRYPTION_CFG = POINTER(struct_tagNET_DVR_STREAMENCRYPTION_CFG)
tagNET_DVR_STREAMENCRYPTION_CFG = struct_tagNET_DVR_STREAMENCRYPTION_CFG
