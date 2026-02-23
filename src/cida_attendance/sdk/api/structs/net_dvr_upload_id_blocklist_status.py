from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_UPLOAD_ID_BLOCKLIST_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_UPLOAD_ID_BLOCKLIST_STATUS, [
    ('dwSize', DWORD),
    ('byIDNum', BYTE * 32),
    ('byStatus', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_UPLOAD_ID_BLOCKLIST_STATUS = struct_tagNET_DVR_UPLOAD_ID_BLOCKLIST_STATUS
LPNET_DVR_UPLOAD_ID_BLOCKLIST_STATUS = POINTER(struct_tagNET_DVR_UPLOAD_ID_BLOCKLIST_STATUS)
tagNET_DVR_UPLOAD_ID_BLOCKLIST_STATUS = struct_tagNET_DVR_UPLOAD_ID_BLOCKLIST_STATUS
