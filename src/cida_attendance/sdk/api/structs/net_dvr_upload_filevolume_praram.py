from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_UPLOAD_FILEVOLUME_PRARAM_(Structure):
    pass

_S(struct_tagNET_DVR_UPLOAD_FILEVOLUME_PRARAM_, [
    ('dwSize', DWORD),
    ('byFileType', BYTE),
    ('byFileVolnumeID', BYTE),
    ('byArchive', BYTE),
    ('byRes1', BYTE),
    ('dwFileSize', DWORD),
    ('szFileName', c_char * 100),
    ('byRes', BYTE * 300),
])

NET_DVR_UPLOAD_FILEVOLUME_PRARAM = struct_tagNET_DVR_UPLOAD_FILEVOLUME_PRARAM_
LPNET_DVR_UPLOAD_FILEVOLUME_PRARAM = POINTER(struct_tagNET_DVR_UPLOAD_FILEVOLUME_PRARAM_)
tagNET_DVR_UPLOAD_FILEVOLUME_PRARAM_ = struct_tagNET_DVR_UPLOAD_FILEVOLUME_PRARAM_
