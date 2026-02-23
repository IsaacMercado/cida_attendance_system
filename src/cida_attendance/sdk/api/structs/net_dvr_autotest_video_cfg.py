from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_AUTOTEST_VIDEO_CFG(Structure):
    pass

_S(struct_tagNET_DVR_AUTOTEST_VIDEO_CFG, [
    ('dwSplitScreenNums', DWORD),
    ('dwVoCh', DWORD),
    ('dwInterface', DWORD),
])

NET_DVR_AUTOTEST_VIDEO_CFG = struct_tagNET_DVR_AUTOTEST_VIDEO_CFG
LPNET_DVR_AUTOTEST_VIDEO_CFG = POINTER(struct_tagNET_DVR_AUTOTEST_VIDEO_CFG)
tagNET_DVR_AUTOTEST_VIDEO_CFG = struct_tagNET_DVR_AUTOTEST_VIDEO_CFG
