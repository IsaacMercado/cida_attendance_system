from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .anon_54 import NET_DVR_PRESETCHAN_INFO
from .anon_55 import NET_DVR_CRUISECHAN_INFO
from .anon_56 import NET_DVR_PTZTRACKCHAN_INFO


class struct_tagNET_DVR_VCA_DETECTION_CFG_V40(Structure):
    pass

_S(struct_tagNET_DVR_VCA_DETECTION_CFG_V40, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('struAlarmSched', (NET_DVR_SCHEDTIME * 8) * 7),
    ('dwHandleType', DWORD),
    ('dwMaxRelAlarmOutChanNum', DWORD),
    ('dwRelAlarmOut', DWORD * int((4096 + 32))),
    ('dwMaxRecordChanNum', DWORD),
    ('dwRelRecordChan', DWORD * 512),
    ('dwEnablePresetChanNum', DWORD),
    ('struPresetChanInfo', NET_DVR_PRESETCHAN_INFO * 512),
    ('byRes2', BYTE * 516),
    ('dwEnableCruiseChanNum', DWORD),
    ('struCruiseChanInfo', NET_DVR_CRUISECHAN_INFO * 512),
    ('dwEnablePtzTrackChanNum', DWORD),
    ('struPtzTrackInfo', NET_DVR_PTZTRACKCHAN_INFO * 512),
    ('struHolidayTime', NET_DVR_SCHEDTIME * 8),
    ('byRes', BYTE * 224),
])

NET_DVR_VCA_DETECTION_CFG_V40 = struct_tagNET_DVR_VCA_DETECTION_CFG_V40
LPNET_DVR_VCA_DETECTION_CFG_V40 = POINTER(struct_tagNET_DVR_VCA_DETECTION_CFG_V40)
tagNET_DVR_VCA_DETECTION_CFG_V40 = struct_tagNET_DVR_VCA_DETECTION_CFG_V40
