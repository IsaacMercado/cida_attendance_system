from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_IP_VIEW_DEVCFG(Structure):
    pass

_S(struct_tagNET_DVR_IP_VIEW_DEVCFG, [
    ('dwSize', DWORD),
    ('byDefaultRing', BYTE),
    ('byRingVolume', BYTE),
    ('byInputVolume', BYTE),
    ('byOutputVolume', BYTE),
    ('wRtpPort', WORD),
    ('byRes1', BYTE * 2),
    ('dwPreviewDelayTime', DWORD),
    ('byRes2', BYTE * 64),
])

NET_DVR_IP_VIEW_DEVCFG = struct_tagNET_DVR_IP_VIEW_DEVCFG
LPNET_DVR_IP_VIEW_DEVCFG = POINTER(struct_tagNET_DVR_IP_VIEW_DEVCFG)
tagNET_DVR_IP_VIEW_DEVCFG = struct_tagNET_DVR_IP_VIEW_DEVCFG
