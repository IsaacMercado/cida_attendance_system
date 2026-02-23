from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DEC_VCA_ALARM_PIC(Structure):
    pass

_S(struct_tagNET_DVR_DEC_VCA_ALARM_PIC, [
    ('byUploadPic', BYTE),
    ('byOverlayTargetInfo', BYTE),
    ('byOverlayRuleInfo', BYTE),
    ('byPicQuality', BYTE),
    ('byPicSize', BYTE),
    ('byRes', BYTE * 27),
])

NET_DVR_DEC_VCA_ALARM_PIC = struct_tagNET_DVR_DEC_VCA_ALARM_PIC
LPNET_DVR_DEC_VCA_ALARM_PIC = POINTER(struct_tagNET_DVR_DEC_VCA_ALARM_PIC)
tagNET_DVR_DEC_VCA_ALARM_PIC = struct_tagNET_DVR_DEC_VCA_ALARM_PIC
