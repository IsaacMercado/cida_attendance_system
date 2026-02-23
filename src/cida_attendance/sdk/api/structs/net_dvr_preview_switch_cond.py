from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PREVIEW_SWITCH_COND(Structure):
    pass

_S(struct_tagNET_DVR_PREVIEW_SWITCH_COND, [
    ('dwSize', DWORD),
    ('byGroup', BYTE),
    ('byVideoOutType', BYTE),
    ('byGetDefaultPreviewSet', BYTE),
    ('byPreviewNumber', BYTE),
])

NET_DVR_PREVIEW_SWITCH_COND = struct_tagNET_DVR_PREVIEW_SWITCH_COND
LPNET_DVR_PREVIEW_SWITCH_COND = POINTER(struct_tagNET_DVR_PREVIEW_SWITCH_COND)
tagNET_DVR_PREVIEW_SWITCH_COND = struct_tagNET_DVR_PREVIEW_SWITCH_COND
