from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ROI_DETECT_NUM(Structure):
    pass

_S(struct_tagNET_DVR_ROI_DETECT_NUM, [
    ('dwSize', DWORD),
    ('dwGroup', DWORD),
    ('dwStreamType', DWORD),
    ('dwRoiFixNum', DWORD),
    ('dwRoiFixID', DWORD * 8),
    ('szFixRoiName', (BYTE * 32) * 8),
    ('dwRoiTrackNum', DWORD),
    ('dwRoiTrackID', DWORD * 8),
    ('byRes', BYTE * 320),
])

NET_DVR_ROI_DETECT_NUM = struct_tagNET_DVR_ROI_DETECT_NUM
LPNET_DVR_ROI_DETECT_NUM = POINTER(struct_tagNET_DVR_ROI_DETECT_NUM)
tagNET_DVR_ROI_DETECT_NUM = struct_tagNET_DVR_ROI_DETECT_NUM
