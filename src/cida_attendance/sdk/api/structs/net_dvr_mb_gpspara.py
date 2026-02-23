from ctypes import Structure, c_int

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_7 import NET_DVR_HANDLEEXCEPTION_V30


class struct_tagNET_DVR_MB_GPSPARA(Structure):
    pass

_S(struct_tagNET_DVR_MB_GPSPARA, [
    ('dwSize', DWORD),
    ('byEnableGPS', BYTE),
    ('byGpsInterface', BYTE),
    ('bySpeedUnit', BYTE),
    ('byEnableRetrieve', BYTE),
    ('iAdjustTime', c_int),
    ('byEnableAdjustTime', BYTE),
    ('byRes1', BYTE * 5),
    ('wGpsUploadInterval', WORD),
    ('byGpsOsdChannel', BYTE * int((32 + 32))),
    ('dwSpeedLimit', DWORD),
    ('struGpsAlarm', NET_DVR_HANDLEEXCEPTION_V30),
    ('byRes2', BYTE * 36),
])

NET_DVR_MB_GPSPARA = struct_tagNET_DVR_MB_GPSPARA
LPNET_DVR_MB_GPSPARA = POINTER(struct_tagNET_DVR_MB_GPSPARA)
tagNET_DVR_MB_GPSPARA = struct_tagNET_DVR_MB_GPSPARA
