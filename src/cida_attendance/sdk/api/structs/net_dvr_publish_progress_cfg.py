from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PUBLISH_PROGRESS_CFG(Structure):
    pass

_S(struct_tagNET_DVR_PUBLISH_PROGRESS_CFG, [
    ('dwSize', DWORD),
    ('byPublishPercent', BYTE),
    ('byPublishStatus', BYTE),
    ('byRes', BYTE * 302),
])

NET_DVR_PUBLISH_PROGRESS_CFG = struct_tagNET_DVR_PUBLISH_PROGRESS_CFG
LPNET_DVR_PUBLISH_PROGRESS_CFG = POINTER(struct_tagNET_DVR_PUBLISH_PROGRESS_CFG)
tagNET_DVR_PUBLISH_PROGRESS_CFG = struct_tagNET_DVR_PUBLISH_PROGRESS_CFG
