from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_multi_stream_compressioncfg_cond import (
    NET_DVR_MULTI_STREAM_COMPRESSIONCFG_COND,
)


class struct_tagNET_DVR_ROI_DETECT_COND(Structure):
    pass

_S(struct_tagNET_DVR_ROI_DETECT_COND, [
    ('dwSize', DWORD),
    ('dwRoiID', DWORD),
    ('struMultiStreamCfg', NET_DVR_MULTI_STREAM_COMPRESSIONCFG_COND),
    ('byRoiDetectType', BYTE),
    ('byRoiDetectTrackType', BYTE),
    ('byRes', BYTE * 30),
])

NET_DVR_ROI_DETECT_COND = struct_tagNET_DVR_ROI_DETECT_COND
LPNET_DVR_ROI_DETECT_COND = POINTER(struct_tagNET_DVR_ROI_DETECT_COND)
tagNET_DVR_ROI_DETECT_COND = struct_tagNET_DVR_ROI_DETECT_COND
