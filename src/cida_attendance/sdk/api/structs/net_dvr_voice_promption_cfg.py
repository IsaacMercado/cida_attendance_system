from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VOICE_PROMPTION_CFG(Structure):
    pass

_S(struct_tagNET_DVR_VOICE_PROMPTION_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('byCenterBusyFile', BYTE * 32),
    ('byRefusedFile', BYTE * 32),
    ('byHangUpFile', BYTE * 32),
    ('byCallWaittingFile', BYTE * 32),
    ('byConsultWaittingFile', BYTE * 32),
    ('byWelcomeFile', BYTE * 32),
    ('byFarewellFile', BYTE * 32),
    ('byCalledVoicePromptName', BYTE * 32),
    ('byRes', BYTE * 384),
])

NET_DVR_VOICE_PROMPTION_CFG = struct_tagNET_DVR_VOICE_PROMPTION_CFG
LPNET_DVR_VOICE_PROMPTION_CFG = POINTER(struct_tagNET_DVR_VOICE_PROMPTION_CFG)
tagNET_DVR_VOICE_PROMPTION_CFG = struct_tagNET_DVR_VOICE_PROMPTION_CFG
