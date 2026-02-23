from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PRIVACY_MASKS_COND(Structure):
    pass

_S(struct_tagNET_DVR_PRIVACY_MASKS_COND, [
    ('dwSize', DWORD),
    ('dwChan', DWORD),
    ('byRegionalID', BYTE),
    ('byDelPrivacyMaskCfg', BYTE),
    ('byRes', BYTE * 62),
])

NET_DVR_PRIVACY_MASKS_COND = struct_tagNET_DVR_PRIVACY_MASKS_COND
LPNET_DVR_PRIVACY_MASKS_COND = POINTER(struct_tagNET_DVR_PRIVACY_MASKS_COND)
tagNET_DVR_PRIVACY_MASKS_COND = struct_tagNET_DVR_PRIVACY_MASKS_COND
