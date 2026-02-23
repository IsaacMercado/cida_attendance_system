from ctypes import Structure, c_int

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MIX_AUDIOOUT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_MIX_AUDIOOUT_CFG, [
    ('dwSize', DWORD),
    ('byModulatorEnbale', BYTE),
    ('byPostFilter', BYTE),
    ('byLimitPressure', BYTE),
    ('byRes1', BYTE),
    ('wModulatorValue', WORD),
    ('wTriggerTime', WORD),
    ('wFreeTime', WORD),
    ('byCompressThreshold', BYTE),
    ('byCompressMode', BYTE),
    ('byCompressRate', BYTE),
    ('byRecoveryGain', BYTE),
    ('byOutputGain', BYTE),
    ('byOutputMute', BYTE),
    ('iOutputGainEx', c_int),
    ('bySoundQualityHanding', BYTE),
    ('byRes', BYTE * 55),
])

NET_DVR_MIX_AUDIOOUT_CFG = struct_tagNET_DVR_MIX_AUDIOOUT_CFG
LPNET_DVR_MIX_AUDIOOUT_CFG = POINTER(struct_tagNET_DVR_MIX_AUDIOOUT_CFG)
tagNET_DVR_MIX_AUDIOOUT_CFG = struct_tagNET_DVR_MIX_AUDIOOUT_CFG
