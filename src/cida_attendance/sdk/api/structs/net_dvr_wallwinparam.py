from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_WALLWINPARAM(Structure):
    pass

_S(struct_tagNET_DVR_WALLWINPARAM, [
    ('dwSize', DWORD),
    ('byTransparency', BYTE),
    ('byWinMode', BYTE),
    ('byEnableSpartan', BYTE),
    ('byDecResource', BYTE),
    ('byWndShowMode', BYTE),
    ('byEnabledFeature', BYTE),
    ('byFeatureMode', BYTE),
    ('byRes1', BYTE),
    ('dwAmplifyingSubWndNo', DWORD),
    ('byWndTopKeep', BYTE),
    ('byWndOpenKeep', BYTE),
    ('byRes', BYTE * 22),
])

NET_DVR_WALLWINPARAM = struct_tagNET_DVR_WALLWINPARAM
LPNET_DVR_WALLWINPARAM = POINTER(struct_tagNET_DVR_WALLWINPARAM)
tagNET_DVR_WALLWINPARAM = struct_tagNET_DVR_WALLWINPARAM
