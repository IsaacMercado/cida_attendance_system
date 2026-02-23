from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER, String


class struct_tagNET_DVR_PASSIVETRANSINFO(Structure):
    pass

_S(struct_tagNET_DVR_PASSIVETRANSINFO, [
    ('dwSize', DWORD),
    ('byStreamType', BYTE),
    ('byLinkMode', BYTE),
    ('byPassiveTransMode', BYTE),
    ('byRes1', BYTE * 5),
    ('byDataType', BYTE),
    ('byRes2', BYTE),
    ('wDataLength', WORD),
    ('pBuffer', String),
    ('byRes3', BYTE * 32),
])

NET_DVR_PASSIVETRANSINFO = struct_tagNET_DVR_PASSIVETRANSINFO
LPNET_DVR_PASSIVETRANSINFO = POINTER(struct_tagNET_DVR_PASSIVETRANSINFO)
tagNET_DVR_PASSIVETRANSINFO = struct_tagNET_DVR_PASSIVETRANSINFO
