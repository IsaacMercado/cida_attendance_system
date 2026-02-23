from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SAFETYCABIN_PERSON_SIGNAL_CFG(Structure):
    pass

_S(struct_tagNET_DVR_SAFETYCABIN_PERSON_SIGNAL_CFG, [
    ('dwSize', DWORD),
    ('bySensorType', BYTE),
    ('bySensitivity', BYTE),
    ('byDevUseTimeout', BYTE),
    ('byRes1', BYTE),
    ('wCurtainDelayTime', WORD),
    ('wCurtainResponseTime', WORD),
    ('wFaintToEmergencyTime', WORD),
    ('byFollowDetectorSensitivity', BYTE),
    ('byManyPersonSensitivity', BYTE),
    ('byRes2', BYTE * 28),
])

NET_DVR_SAFETYCABIN_PERSON_SIGNAL_CFG = struct_tagNET_DVR_SAFETYCABIN_PERSON_SIGNAL_CFG
LPNET_DVR_SAFETYCABIN_PERSON_SIGNAL_CFG = POINTER(struct_tagNET_DVR_SAFETYCABIN_PERSON_SIGNAL_CFG)
tagNET_DVR_SAFETYCABIN_PERSON_SIGNAL_CFG = struct_tagNET_DVR_SAFETYCABIN_PERSON_SIGNAL_CFG
