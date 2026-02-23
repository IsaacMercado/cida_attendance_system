from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_vca_dev_info import NET_VCA_DEV_INFO


class struct_tagNET_DVR_SCENECHANGE_DETECTION_RESULT(Structure):
    pass

_S(struct_tagNET_DVR_SCENECHANGE_DETECTION_RESULT, [
    ('dwSize', DWORD),
    ('struDevInfo', NET_VCA_DEV_INFO),
    ('wDevInfoIvmsChannelEx', WORD),
    ('byRes', BYTE * 126),
])

NET_DVR_SCENECHANGE_DETECTION_RESULT = struct_tagNET_DVR_SCENECHANGE_DETECTION_RESULT
LPNET_DVR_SCENECHANGE_DETECTION_RESULT = POINTER(struct_tagNET_DVR_SCENECHANGE_DETECTION_RESULT)
tagNET_DVR_SCENECHANGE_DETECTION_RESULT = struct_tagNET_DVR_SCENECHANGE_DETECTION_RESULT
