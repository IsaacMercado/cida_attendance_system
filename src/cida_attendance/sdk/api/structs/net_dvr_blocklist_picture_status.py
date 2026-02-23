from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_BLOCKLIST_PICTURE_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_BLOCKLIST_PICTURE_STATUS, [
    ('dwSize', DWORD),
    ('byCardNo', BYTE * 32),
    ('byStatus', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_BLOCKLIST_PICTURE_STATUS = struct_tagNET_DVR_BLOCKLIST_PICTURE_STATUS
LPNET_DVR_BLOCKLIST_PICTURE_STATUS = POINTER(struct_tagNET_DVR_BLOCKLIST_PICTURE_STATUS)
tagNET_DVR_BLOCKLIST_PICTURE_STATUS = struct_tagNET_DVR_BLOCKLIST_PICTURE_STATUS
