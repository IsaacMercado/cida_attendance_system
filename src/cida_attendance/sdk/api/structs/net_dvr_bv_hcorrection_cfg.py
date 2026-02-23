from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_BV_HCORRECTION_CFG(Structure):
    pass

_S(struct_tagNET_DVR_BV_HCORRECTION_CFG, [
    ('dwSize', DWORD),
    ('dwHumanHeight', DWORD),
    ('byRes', BYTE * 300),
])

NET_DVR_BV_HCORRECTION_CFG = struct_tagNET_DVR_BV_HCORRECTION_CFG
LPNET_DVR_BV_HCORRECTION_CFG = POINTER(struct_tagNET_DVR_BV_HCORRECTION_CFG)
tagNET_DVR_BV_HCORRECTION_CFG = struct_tagNET_DVR_BV_HCORRECTION_CFG
