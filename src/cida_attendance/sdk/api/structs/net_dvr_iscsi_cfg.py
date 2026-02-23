from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_ISCSI_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ISCSI_CFG, [
    ('dwSize', DWORD),
    ('wVrmPort', WORD),
    ('byEnable', BYTE),
    ('byRes', BYTE * 69),
    ('struVrmAddr', NET_DVR_IPADDR),
    ('chNvtIndexCode', c_char * 64),
])

NET_DVR_ISCSI_CFG = struct_tagNET_DVR_ISCSI_CFG
LPNET_DVR_ISCSI_CFG = POINTER(struct_tagNET_DVR_ISCSI_CFG)
tagNET_DVR_ISCSI_CFG = struct_tagNET_DVR_ISCSI_CFG
