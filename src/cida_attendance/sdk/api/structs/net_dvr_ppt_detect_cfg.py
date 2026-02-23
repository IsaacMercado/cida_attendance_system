from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct__NET_DVR_PPT_DETECT_CFG_(Structure):
    pass

_S(struct__NET_DVR_PPT_DETECT_CFG_, [
    ('dwSize', DWORD),
    ('byEnablePPTDetect', BYTE),
    ('byPptDetLevel', BYTE),
    ('byEnablePartScreen', BYTE),
    ('byRes1', BYTE),
    ('wX', WORD),
    ('wY', WORD),
    ('wWidth', WORD),
    ('wHeight', WORD),
    ('dwChangePixelNum', DWORD),
    ('byRes', BYTE * 28),
])

NET_DVR_PPT_DETECT_CFG = struct__NET_DVR_PPT_DETECT_CFG_
LPNET_DVR_PPT_DETECT_CFG = POINTER(struct__NET_DVR_PPT_DETECT_CFG_)
_NET_DVR_PPT_DETECT_CFG_ = struct__NET_DVR_PPT_DETECT_CFG_
