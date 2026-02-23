from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PRIVACY_MASKS_ENABLECFG(Structure):
    pass

_S(struct_tagNET_DVR_PRIVACY_MASKS_ENABLECFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_PRIVACY_MASKS_ENABLECFG = struct_tagNET_DVR_PRIVACY_MASKS_ENABLECFG
LPNET_DVR_PRIVACY_MASKS_ENABLECFG = POINTER(struct_tagNET_DVR_PRIVACY_MASKS_ENABLECFG)
tagNET_DVR_PRIVACY_MASKS_ENABLECFG = struct_tagNET_DVR_PRIVACY_MASKS_ENABLECFG
