from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_145 import NET_DVR_JPEGPARA


class struct_tagNET_DVR_SNAPCFG(Structure):
    pass

_S(struct_tagNET_DVR_SNAPCFG, [
    ('dwSize', DWORD),
    ('byRelatedDriveWay', BYTE),
    ('bySnapTimes', BYTE),
    ('wSnapWaitTime', WORD),
    ('wIntervalTime', WORD * 4),
    ('dwSnapVehicleNum', DWORD),
    ('struJpegPara', NET_DVR_JPEGPARA),
    ('byRes2', BYTE * 16),
])

NET_DVR_SNAPCFG = struct_tagNET_DVR_SNAPCFG
LPNET_DVR_SNAPCFG = POINTER(struct_tagNET_DVR_SNAPCFG)
tagNET_DVR_SNAPCFG = struct_tagNET_DVR_SNAPCFG
