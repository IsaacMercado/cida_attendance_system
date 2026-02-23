from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_T1TEST_SEND_DATA_BUZZER(Structure):
    pass

_S(struct_tagNET_DVR_T1TEST_SEND_DATA_BUZZER, [
    ('byHearSound', BYTE),
    ('byRes', BYTE * 31),
])

NET_DVR_T1TEST_SEND_DATA_BUZZER = struct_tagNET_DVR_T1TEST_SEND_DATA_BUZZER
LPNET_DVR_T1TEST_SEND_DATA_BUZZER = POINTER(struct_tagNET_DVR_T1TEST_SEND_DATA_BUZZER)
tagNET_DVR_T1TEST_SEND_DATA_BUZZER = struct_tagNET_DVR_T1TEST_SEND_DATA_BUZZER
