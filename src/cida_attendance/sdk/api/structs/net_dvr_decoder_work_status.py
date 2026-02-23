from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_177 import NET_DVR_MATRIX_CHAN_STATUS
from .anon_183 import NET_DVR_DISP_CHAN_STATUS


class struct_tagNET_DVR_DECODER_WORK_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_DECODER_WORK_STATUS, [
    ('dwSize', DWORD),
    ('struDecChanStatus', NET_DVR_MATRIX_CHAN_STATUS * 32),
    ('struDispChanStatus', NET_DVR_DISP_CHAN_STATUS * 24),
    ('byAlarmInStatus', BYTE * 32),
    ('byAlarmOutStatus', BYTE * 32),
    ('byAudioInChanStatus', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_DECODER_WORK_STATUS = struct_tagNET_DVR_DECODER_WORK_STATUS
LPNET_DVR_DECODER_WORK_STATUS = POINTER(struct_tagNET_DVR_DECODER_WORK_STATUS)
tagNET_DVR_DECODER_WORK_STATUS = struct_tagNET_DVR_DECODER_WORK_STATUS
