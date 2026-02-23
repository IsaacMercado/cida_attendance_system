from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FORCESTOP_FORENSICS_CFG(Structure):
    pass

_S(struct_tagNET_DVR_FORCESTOP_FORENSICS_CFG, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byRes', BYTE * 64),
])

NET_DVR_FORCESTOP_FORENSICS_CFG = struct_tagNET_DVR_FORCESTOP_FORENSICS_CFG
LPNET_DVR_FORCESTOP_FORENSICS_CFG = POINTER(struct_tagNET_DVR_FORCESTOP_FORENSICS_CFG)
tagNET_DVR_FORCESTOP_FORENSICS_CFG = struct_tagNET_DVR_FORCESTOP_FORENSICS_CFG
