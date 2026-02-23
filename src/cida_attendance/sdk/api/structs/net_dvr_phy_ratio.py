from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PHY_RATIO(Structure):
    pass

_S(struct_tagNET_DVR_PHY_RATIO, [
    ('dwSize', DWORD),
    ('dwPhysicsRatio', DWORD),
    ('byRes', BYTE * 60),
])

NET_DVR_PHY_RATIO = struct_tagNET_DVR_PHY_RATIO
LPNET_DVR_PHY_RATIO = POINTER(struct_tagNET_DVR_PHY_RATIO)
tagNET_DVR_PHY_RATIO = struct_tagNET_DVR_PHY_RATIO
