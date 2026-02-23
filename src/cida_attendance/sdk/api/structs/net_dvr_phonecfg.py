from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PHONECFG(Structure):
    pass

_S(struct_tagNET_DVR_PHONECFG, [
    ('byAllowList', BYTE * 32),
    ('byPhonePerssion', BYTE * 32),
    ('byAlarmHandler', BYTE * 32),
    ('byRes', BYTE * 128),
])

NET_DVR_PHONECFG = struct_tagNET_DVR_PHONECFG
LPNET_DVR_PHONECFG = POINTER(struct_tagNET_DVR_PHONECFG)
tagNET_DVR_PHONECFG = struct_tagNET_DVR_PHONECFG
