from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PARKINGSAPCE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_PARKINGSAPCE_CFG, [
    ('dwSize', DWORD),
    ('dwTotalParkingLot', DWORD),
    ('dwCurrParkingLot', DWORD),
    ('byRes', BYTE * 128),
])

NET_DVR_PARKINGSAPCE_CFG = struct_tagNET_DVR_PARKINGSAPCE_CFG
LPNET_DVR_PARKINGSAPCE_CFG = POINTER(struct_tagNET_DVR_PARKINGSAPCE_CFG)
tagNET_DVR_PARKINGSAPCE_CFG = struct_tagNET_DVR_PARKINGSAPCE_CFG
