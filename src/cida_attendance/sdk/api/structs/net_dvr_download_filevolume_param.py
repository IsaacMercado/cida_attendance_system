from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from ..functions import DOWNLOAD_DATA_CB


class struct_tagNET_DVR_DOWNLOAD_FILEVOLUME_PARAM_(Structure):
    pass

_S(struct_tagNET_DVR_DOWNLOAD_FILEVOLUME_PARAM_, [
    ('dwSize', DWORD),
    ('sUrl', BYTE * 240),
    ('byRes', BYTE * 248),
    ('fnDownloadDataCB', DOWNLOAD_DATA_CB),
    ('pUserData', POINTER(None)),
])

NET_DVR_DOWNLOAD_FILEVOLUME_PARAM = struct_tagNET_DVR_DOWNLOAD_FILEVOLUME_PARAM_
LPNET_DVR_DOWNLOAD_FILEVOLUME_PARAM = POINTER(struct_tagNET_DVR_DOWNLOAD_FILEVOLUME_PARAM_)
tagNET_DVR_DOWNLOAD_FILEVOLUME_PARAM_ = struct_tagNET_DVR_DOWNLOAD_FILEVOLUME_PARAM_
