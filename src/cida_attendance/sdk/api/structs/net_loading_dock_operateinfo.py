from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct__tagNET_LOADING_DOCK_OPERATEINFO_(Structure):
    pass

_S(struct__tagNET_LOADING_DOCK_OPERATEINFO_, [
    ('dwSize', DWORD),
    ('byAbsTime', BYTE * 32),
    ('byParkingNo', BYTE * 16),
    ('dwIndex', DWORD),
    ('sLicense', c_char * 16),
    ('byCurrentWorkerNumber', BYTE),
    ('byCurrentGoodsLoadingRate', BYTE),
    ('byDoorsStatus', BYTE),
    ('byRes1', BYTE),
    ('dwBackPicDataLength', DWORD),
    ('pBackPicDataBuffer', POINTER(BYTE)),
    ('dwChannel', DWORD),
    ('byRes', BYTE * 508),
])

NET_LOADING_DOCK_OPERATEINFO = struct__tagNET_LOADING_DOCK_OPERATEINFO_
LPNET_LOADING_DOCK_OPERATEINFO = POINTER(struct__tagNET_LOADING_DOCK_OPERATEINFO_)
_tagNET_LOADING_DOCK_OPERATEINFO_ = struct__tagNET_LOADING_DOCK_OPERATEINFO_
