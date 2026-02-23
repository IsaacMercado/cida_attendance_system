from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PHONECENTERDIALCFG(Structure):
    pass

_S(struct_tagNET_DVR_PHONECENTERDIALCFG, [
    ('sCenterName', BYTE * 32),
    ('byPhoneNum', BYTE * 32),
    ('byRepeatCall', BYTE),
    ('byPstnProtocol', BYTE),
    ('byDialDelay', BYTE),
    ('byPstnTransMode', BYTE),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 5),
    ('byReceiverId', BYTE * 6),
    ('byRes2', BYTE * 32),
])

NET_DVR_PHONECENTERDIALCFG = struct_tagNET_DVR_PHONECENTERDIALCFG
LPNET_DVR_PHONECENTERDIALCFG = POINTER(struct_tagNET_DVR_PHONECENTERDIALCFG)
tagNET_DVR_PHONECENTERDIALCFG = struct_tagNET_DVR_PHONECENTERDIALCFG
