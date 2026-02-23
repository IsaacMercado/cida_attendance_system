from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LOGIN_DEVICE_PARAM_(Structure):
    pass

_S(struct_tagNET_DVR_LOGIN_DEVICE_PARAM_, [
    ('dwSize', DWORD),
    ('byMobileDev', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_LOGIN_DEVICE_PARAM = struct_tagNET_DVR_LOGIN_DEVICE_PARAM_
LPNET_DVR_LOGIN_DEVICE_PARAM = POINTER(struct_tagNET_DVR_LOGIN_DEVICE_PARAM_)
tagNET_DVR_LOGIN_DEVICE_PARAM_ = struct_tagNET_DVR_LOGIN_DEVICE_PARAM_
