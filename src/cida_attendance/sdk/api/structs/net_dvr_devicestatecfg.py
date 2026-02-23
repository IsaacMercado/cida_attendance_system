from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_DEVICESTATECFG(Structure):
    pass

_S(struct_tagNET_DVR_DEVICESTATECFG, [
    ('dwSize', DWORD),
    ('wPreviewNum', WORD),
    ('wFortifyLinkNum', WORD),
    ('struPreviewIP', NET_DVR_IPADDR * 6),
    ('struFortifyIP', NET_DVR_IPADDR * 10),
    ('dwVideoFrameRate', DWORD),
    ('byResolution', BYTE),
    ('bySnapResolution', BYTE),
    ('byStreamType', BYTE),
    ('byTriggerType', BYTE),
    ('dwSDVolume', DWORD),
    ('dwSDFreeSpace', DWORD),
    ('byDetectorState', (BYTE * 3) * 16),
    ('byDetectorLinkState', BYTE),
    ('bySDStatus', BYTE),
    ('byFortifyLevel', BYTE * 10),
    ('byRes2', BYTE * 116),
])

NET_DVR_DEVICESTATECFG = struct_tagNET_DVR_DEVICESTATECFG
LPNET_DVR_DEVICESTATECFG = POINTER(struct_tagNET_DVR_DEVICESTATECFG)
tagNET_DVR_DEVICESTATECFG = struct_tagNET_DVR_DEVICESTATECFG
