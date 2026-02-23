from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMCTRL_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ALARMCTRL_CFG, [
    ('dwSize', DWORD),
    ('byListenPicUploadEnabled', BYTE),
    ('byRes', BYTE * 259),
])

NET_DVR_ALARMCTRL_CFG = struct_tagNET_DVR_ALARMCTRL_CFG
LPNET_DVR_ALARMCTRL_CFG = POINTER(struct_tagNET_DVR_ALARMCTRL_CFG)
tagNET_DVR_ALARMCTRL_CFG = struct_tagNET_DVR_ALARMCTRL_CFG
