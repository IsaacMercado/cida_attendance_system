from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SMARTTRACKCFG(Structure):
    pass

_S(struct_tagNET_DVR_SMARTTRACKCFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes', BYTE * 3),
    ('dwDuration', DWORD),
    ('byRes1', BYTE * 124),
])

NET_DVR_SMARTTRACKCFG = struct_tagNET_DVR_SMARTTRACKCFG
LPNET_DVR_SMARTTRACKCFG = POINTER(struct_tagNET_DVR_SMARTTRACKCFG)
tagNET_DVR_SMARTTRACKCFG = struct_tagNET_DVR_SMARTTRACKCFG
