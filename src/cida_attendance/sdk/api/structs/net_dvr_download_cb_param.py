from ctypes import Structure

from ..base_classes import _S, BYTE, INT64
from ..ctypes_preamble import POINTER
from ..functions import DOWNLOAD_DATA_CB


class struct_tagNET_DVR_DOWNLOAD_CB_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_DOWNLOAD_CB_PARAM, [
    ('fnDownloadDataCB', DOWNLOAD_DATA_CB),
    ('pUserData', POINTER(None)),
    ('i64Offset', INT64),
    ('byRes', BYTE * 256),
])

NET_DVR_DOWNLOAD_CB_PARAM = struct_tagNET_DVR_DOWNLOAD_CB_PARAM
LPNET_DVR_DOWNLOAD_CB_PARAM = POINTER(struct_tagNET_DVR_DOWNLOAD_CB_PARAM)
tagNET_DVR_DOWNLOAD_CB_PARAM = struct_tagNET_DVR_DOWNLOAD_CB_PARAM
