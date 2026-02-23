from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_POSINFO_OVERLAY(Structure):
    pass

_S(struct_tagNET_DVR_POSINFO_OVERLAY, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byBackpackEnanble', BYTE),
    ('bySexEnanble', BYTE),
    ('byCarryEnanble', BYTE),
    ('byRideEnanble', BYTE),
    ('byMaskEnanble', BYTE),
    ('byHatEnanble', BYTE),
    ('bySleeveEnanble', BYTE),
    ('byPantsTypeEnanble', BYTE),
    ('byHairEnanble', BYTE),
    ('byGlassesEnanble', BYTE),
    ('byAgeEnanble', BYTE),
    ('byHeightEnanble', BYTE),
    ('byRes', BYTE * 511),
])

NET_DVR_POSINFO_OVERLAY = struct_tagNET_DVR_POSINFO_OVERLAY
LPNET_DVR_POSINFO_OVERLAY = POINTER(struct_tagNET_DVR_POSINFO_OVERLAY)
tagNET_DVR_POSINFO_OVERLAY = struct_tagNET_DVR_POSINFO_OVERLAY
