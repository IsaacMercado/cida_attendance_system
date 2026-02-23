from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_UPLOAD_ID_BLOCKLIST_COND(Structure):
    pass

_S(struct_tagNET_DVR_UPLOAD_ID_BLOCKLIST_COND, [
    ('dwSize', DWORD),
    ('dwBlockListNum', DWORD),
    ('byRes', BYTE * 128),
])

NET_DVR_UPLOAD_ID_BLOCKLIST_COND = struct_tagNET_DVR_UPLOAD_ID_BLOCKLIST_COND
LPNET_DVR_UPLOAD_ID_BLOCKLIST_COND = POINTER(struct_tagNET_DVR_UPLOAD_ID_BLOCKLIST_COND)
tagNET_DVR_UPLOAD_ID_BLOCKLIST_COND = struct_tagNET_DVR_UPLOAD_ID_BLOCKLIST_COND
