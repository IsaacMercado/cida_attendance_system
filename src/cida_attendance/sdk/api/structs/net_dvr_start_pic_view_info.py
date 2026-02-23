from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_START_PIC_VIEW_INFO(Structure):
    pass

_S(struct_tagNET_DVR_START_PIC_VIEW_INFO, [
    ('dwSize', DWORD),
    ('dwSignalIndex', DWORD),
    ('dwDeviceIndex', DWORD),
    ('byRes1', BYTE * 12),
    ('byChanIndex', BYTE),
    ('byRes2', BYTE * 3),
    ('dwScreenNum', DWORD),
    ('dwLayer', DWORD),
    ('dwResolution', DWORD),
    ('byFrame', BYTE),
    ('bySupportStreamView', BYTE),
    ('byRes3', BYTE * 14),
])

NET_DVR_START_PIC_VIEW_INFO = struct_tagNET_DVR_START_PIC_VIEW_INFO
LPNET_DVR_START_PIC_VIEW_INFO = POINTER(struct_tagNET_DVR_START_PIC_VIEW_INFO)
tagNET_DVR_START_PIC_VIEW_INFO = struct_tagNET_DVR_START_PIC_VIEW_INFO
