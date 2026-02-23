from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PHONECFG_V50(Structure):
    pass

_S(struct_tagNET_DVR_PHONECFG_V50, [
    ('byAllowList', BYTE * 32),
    ('byPhonePerssion', BYTE * 32),
    ('byAlarmHandler', BYTE * 32),
    ('byAcsPassword', BYTE * 16),
    ('byName', BYTE * 32),
    ('byRes', BYTE * 80),
])

NET_DVR_PHONECFG_V50 = struct_tagNET_DVR_PHONECFG_V50
LPNET_DVR_PHONECFG_V50 = POINTER(struct_tagNET_DVR_PHONECFG_V50)
tagNET_DVR_PHONECFG_V50 = struct_tagNET_DVR_PHONECFG_V50
