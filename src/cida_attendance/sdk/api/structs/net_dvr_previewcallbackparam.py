from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, LONG
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PREVIEWCALLBACKPARAM(Structure):
    pass

_S(struct_tagNET_DVR_PREVIEWCALLBACKPARAM, [
    ('lChannel', LONG),
    ('nLinkProtocol', BYTE),
    ('nTransMode', BYTE),
    ('byPreviewType', BYTE),
    ('byRes', BYTE * 5),
    ('nSessionID', DWORD),
])

NET_DVR_PREVIEWCALLBACKPARAM = struct_tagNET_DVR_PREVIEWCALLBACKPARAM
LPNET_DVR_PREVIEWCALLBACKPARAM = POINTER(struct_tagNET_DVR_PREVIEWCALLBACKPARAM)
tagNET_DVR_PREVIEWCALLBACKPARAM = struct_tagNET_DVR_PREVIEWCALLBACKPARAM
