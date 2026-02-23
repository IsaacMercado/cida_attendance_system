from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from ..functions import fnCertVerifyResultCallBack


class struct_tagNET_DVR_LOCAL_CERTIFICATION(Structure):
    pass

_S(struct_tagNET_DVR_LOCAL_CERTIFICATION, [
    ('szLoadPath', c_char * 256),
    ('fnCB', fnCertVerifyResultCallBack),
    ('pUserData', POINTER(None)),
    ('byRes', BYTE * 64),
])

NET_DVR_LOCAL_CERTIFICATION = struct_tagNET_DVR_LOCAL_CERTIFICATION
LPNET_DVR_LOCAL_CERTIFICATION = POINTER(struct_tagNET_DVR_LOCAL_CERTIFICATION)
tagNET_DVR_LOCAL_CERTIFICATION = struct_tagNET_DVR_LOCAL_CERTIFICATION
