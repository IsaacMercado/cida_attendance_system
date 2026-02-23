from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LOCAL_SECURITY(Structure):
    pass

_S(struct_tagNET_DVR_LOCAL_SECURITY, [
    ('bySecurityLevel', BYTE),
    ('byRes', BYTE * 255),
])

NET_DVR_LOCAL_SECURITY = struct_tagNET_DVR_LOCAL_SECURITY
LPNET_DVR_LOCAL_SECURITY = POINTER(struct_tagNET_DVR_LOCAL_SECURITY)
tagNET_DVR_LOCAL_SECURITY = struct_tagNET_DVR_LOCAL_SECURITY
