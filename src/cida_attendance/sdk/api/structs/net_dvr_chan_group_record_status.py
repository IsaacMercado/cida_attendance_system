from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_chans_record_status import NET_DVR_CHANS_RECORD_STATUS


class struct_tagNET_DVR_CHAN_GROUP_RECORD_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_CHAN_GROUP_RECORD_STATUS, [
    ('dwSize', DWORD),
    ('struChanStatus', NET_DVR_CHANS_RECORD_STATUS * int((32 + 32))),
])

NET_DVR_CHAN_GROUP_RECORD_STATUS = struct_tagNET_DVR_CHAN_GROUP_RECORD_STATUS
LPNET_DVR_CHAN_GROUP_RECORD_STATUS = POINTER(struct_tagNET_DVR_CHAN_GROUP_RECORD_STATUS)
tagNET_DVR_CHAN_GROUP_RECORD_STATUS = struct_tagNET_DVR_CHAN_GROUP_RECORD_STATUS
