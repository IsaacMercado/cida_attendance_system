from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_177 import NET_DVR_MATRIX_CHAN_STATUS
from .net_dvr_disp_chan_status_v41 import NET_DVR_DISP_CHAN_STATUS_V41


class struct_tagNET_DVR_DECODER_WORK_STATUS_V41(Structure):
    pass

_S(struct_tagNET_DVR_DECODER_WORK_STATUS_V41, [
    ('dwSize', DWORD),
    ('struDecChanStatus', NET_DVR_MATRIX_CHAN_STATUS * 32),
    ('struDispChanStatus', NET_DVR_DISP_CHAN_STATUS_V41 * 32),
    ('byAlarmInStatus', BYTE * 32),
    ('byAlarmOutStatus', BYTE * 32),
    ('byAudioInChanStatus', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_DECODER_WORK_STATUS_V41 = struct_tagNET_DVR_DECODER_WORK_STATUS_V41
LPNET_DVR_DECODER_WORK_STATUS_V41 = POINTER(struct_tagNET_DVR_DECODER_WORK_STATUS_V41)
tagNET_DVR_DECODER_WORK_STATUS_V41 = struct_tagNET_DVR_DECODER_WORK_STATUS_V41
