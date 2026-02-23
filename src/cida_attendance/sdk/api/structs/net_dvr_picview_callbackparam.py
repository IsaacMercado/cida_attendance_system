from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, LONG, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PICVIEW_CALLBACKPARAM(Structure):
    pass

_S(struct_tagNET_DVR_PICVIEW_CALLBACKPARAM, [
    ('dwUserID', DWORD),
    ('sDeviceID', BYTE * 16),
    ('nPicViewHandle', LONG),
    ('wSignalIndex', WORD),
    ('wHeadLen', WORD),
    ('byHeadBuf', BYTE * 100),
    ('byRes2', BYTE * 32),
])

NET_DVR_PICVIEW_CALLBACKPARAM = struct_tagNET_DVR_PICVIEW_CALLBACKPARAM
LPNET_DVR_PICVIEW_CALLBACKPARAM = POINTER(struct_tagNET_DVR_PICVIEW_CALLBACKPARAM)
tagNET_DVR_PICVIEW_CALLBACKPARAM = struct_tagNET_DVR_PICVIEW_CALLBACKPARAM
