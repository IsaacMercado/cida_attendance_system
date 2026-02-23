from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_AID_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_AID_PARAM, [
    ('wParkingDuration', WORD),
    ('wPedestrianDuration', WORD),
    ('wDebrisDuration', WORD),
    ('wCongestionLength', WORD),
    ('wCongestionDuration', WORD),
    ('wInverseDuration', WORD),
    ('wInverseDistance', WORD),
    ('wInverseAngleTolerance', WORD),
    ('wIllegalParkingTime', WORD),
    ('wIllegalParkingPicNum', WORD),
    ('byMergePic', BYTE),
    ('byRes1', BYTE * 23),
])

NET_DVR_AID_PARAM = struct_tagNET_DVR_AID_PARAM
LPNET_DVR_AID_PARAM = POINTER(struct_tagNET_DVR_AID_PARAM)
tagNET_DVR_AID_PARAM = struct_tagNET_DVR_AID_PARAM
