from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_EXTERNAL_DEVSTATUS(Structure):
    pass

_S(struct_tagNET_DVR_EXTERNAL_DEVSTATUS, [
    ('dwSize', DWORD),
    ('sDevName', c_char * 32),
    ('byExternalDevTpye', BYTE),
    ('byRelativeIndex', BYTE),
    ('byOnline', BYTE),
    ('byRes', BYTE * 125),
])

NET_DVR_EXTERNAL_DEVSTATUS = struct_tagNET_DVR_EXTERNAL_DEVSTATUS
LPNET_DVR_EXTERNAL_DEVSTATUS = POINTER(struct_tagNET_DVR_EXTERNAL_DEVSTATUS)
tagNET_DVR_EXTERNAL_DEVSTATUS = struct_tagNET_DVR_EXTERNAL_DEVSTATUS
