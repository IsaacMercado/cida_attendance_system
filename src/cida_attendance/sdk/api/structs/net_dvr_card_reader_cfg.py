from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CARD_READER_CFG(Structure):
    pass

_S(struct_tagNET_DVR_CARD_READER_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byCardReaderType', BYTE),
    ('byOkLedPolarity', BYTE),
    ('byErrorLedPolarity', BYTE),
    ('byBuzzerPolarity', BYTE),
    ('bySwipeInterval', BYTE),
    ('byPressTimeout', BYTE),
    ('byEnableFailAlarm', BYTE),
    ('byMaxReadCardFailNum', BYTE),
    ('byEnableTamperCheck', BYTE),
    ('byOfflineCheckTime', BYTE),
    ('byFingerPrintCheckLevel', BYTE),
    ('byUseLocalController', BYTE),
    ('byRes1', BYTE),
    ('wLocalControllerID', WORD),
    ('wLocalControllerReaderID', WORD),
    ('wCardReaderChannel', WORD),
    ('byRes', BYTE * 16),
])

NET_DVR_CARD_READER_CFG = struct_tagNET_DVR_CARD_READER_CFG
LPNET_DVR_CARD_READER_CFG = POINTER(struct_tagNET_DVR_CARD_READER_CFG)
tagNET_DVR_CARD_READER_CFG = struct_tagNET_DVR_CARD_READER_CFG
