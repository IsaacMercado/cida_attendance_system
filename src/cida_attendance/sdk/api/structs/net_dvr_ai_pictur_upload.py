from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_AI_PICTUR_UPLOAD(Structure):
    pass

_S(struct_tagNET_DVR_AI_PICTUR_UPLOAD, [
    ('dwSize', DWORD),
    ('szTaskID', c_char * 64),
    ('szPID', c_char * 64),
    ('byRes', BYTE * 128),
])

NET_DVR_AI_PICTUR_UPLOAD = struct_tagNET_DVR_AI_PICTUR_UPLOAD
LPNET_DVR_AI_PICTUR_UPLOAD = POINTER(struct_tagNET_DVR_AI_PICTUR_UPLOAD)
tagNET_DVR_AI_PICTUR_UPLOAD = struct_tagNET_DVR_AI_PICTUR_UPLOAD
