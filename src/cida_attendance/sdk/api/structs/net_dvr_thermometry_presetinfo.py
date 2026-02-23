from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_thermometry_presetinfo_param import NET_DVR_THERMOMETRY_PRESETINFO_PARAM


class struct_tagNET_DVR_THERMOMETRY_PRESETINFO(Structure):
    pass

_S(struct_tagNET_DVR_THERMOMETRY_PRESETINFO, [
    ('dwSize', DWORD),
    ('wPresetNo', WORD),
    ('byRes', BYTE * 2),
    ('struPresetInfo', NET_DVR_THERMOMETRY_PRESETINFO_PARAM * 40),
])

NET_DVR_THERMOMETRY_PRESETINFO = struct_tagNET_DVR_THERMOMETRY_PRESETINFO
LPNET_DVR_THERMOMETRY_PRESETINFO = POINTER(struct_tagNET_DVR_THERMOMETRY_PRESETINFO)
tagNET_DVR_THERMOMETRY_PRESETINFO = struct_tagNET_DVR_THERMOMETRY_PRESETINFO
