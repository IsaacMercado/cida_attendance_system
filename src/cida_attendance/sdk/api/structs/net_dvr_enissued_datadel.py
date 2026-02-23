from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ENISSUED_DATADEL(Structure):
    pass

_S(struct_tagNET_DVR_ENISSUED_DATADEL, [
    ('dwSize', DWORD),
    ('byDevCtrlCode', BYTE),
    ('byRes', BYTE * 27),
])

NET_DVR_ENISSUED_DATADEL = struct_tagNET_DVR_ENISSUED_DATADEL
LPNET_DVR_ENISSUED_DATADEL = POINTER(struct_tagNET_DVR_ENISSUED_DATADEL)
tagNET_DVR_ENISSUED_DATADEL = struct_tagNET_DVR_ENISSUED_DATADEL
