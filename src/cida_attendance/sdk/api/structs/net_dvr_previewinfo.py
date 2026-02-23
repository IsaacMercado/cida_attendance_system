from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, HWND, LONG
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PREVIEWINFO(Structure):
    pass

_S(struct_tagNET_DVR_PREVIEWINFO, [
    ('lChannel', LONG),
    ('dwStreamType', DWORD),
    ('dwLinkMode', DWORD),
    ('hPlayWnd', HWND),
    ('bBlocked', DWORD),
    ('bPassbackRecord', DWORD),
    ('byPreviewMode', BYTE),
    ('byStreamID', BYTE * 32),
    ('byProtoType', BYTE),
    ('byRes1', BYTE),
    ('byVideoCodingType', BYTE),
    ('dwDisplayBufNum', DWORD),
    ('byNPQMode', BYTE),
    ('byRecvMetaData', BYTE),
    ('byDataType', BYTE),
    ('byRes', BYTE * 213),
])

NET_DVR_PREVIEWINFO = struct_tagNET_DVR_PREVIEWINFO
LPNET_DVR_PREVIEWINFO = POINTER(struct_tagNET_DVR_PREVIEWINFO)
tagNET_DVR_PREVIEWINFO = struct_tagNET_DVR_PREVIEWINFO
