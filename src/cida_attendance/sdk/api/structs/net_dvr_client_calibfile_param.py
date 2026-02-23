from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CLIENT_CALIBFILE_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_CLIENT_CALIBFILE_PARAM, [
    ('dwSize', DWORD),
    ('dwFileLen', DWORD),
    ('byChannel', BYTE),
    ('byFileType', BYTE),
    ('byRes', BYTE * 22),
])

NET_DVR_CLIENT_CALIBFILE_PARAM = struct_tagNET_DVR_CLIENT_CALIBFILE_PARAM
LPNET_DVR_CLIENT_CALIBFILE_PARAM = POINTER(struct_tagNET_DVR_CLIENT_CALIBFILE_PARAM)
tagNET_DVR_CLIENT_CALIBFILE_PARAM = struct_tagNET_DVR_CLIENT_CALIBFILE_PARAM
