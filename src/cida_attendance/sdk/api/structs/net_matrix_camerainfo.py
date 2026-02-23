from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_tagNET_MATRIX_CAMERAINFO(Structure):
    pass

_S(struct_tagNET_MATRIX_CAMERAINFO, [
    ('dwGlobalCamId', DWORD),
    ('sCamName', BYTE * 32),
    ('dwMatrixId', DWORD),
    ('dwLocCamId', DWORD),
    ('byValid', BYTE),
    ('byPtzCtrl', BYTE),
    ('byUseType', BYTE),
    ('byUsedByTrunk', BYTE),
    ('byTrunkReq', BYTE),
    ('byRes1', BYTE * 3),
    ('struInstallTime', NET_DVR_TIME),
    ('sPurpose', BYTE * 32),
    ('byRes2', BYTE * 20),
])

NET_MATRIX_CAMERAINFO = struct_tagNET_MATRIX_CAMERAINFO
LPNET_MATRIX_CAMERAINFO = POINTER(struct_tagNET_MATRIX_CAMERAINFO)
tagNET_MATRIX_CAMERAINFO = struct_tagNET_MATRIX_CAMERAINFO
