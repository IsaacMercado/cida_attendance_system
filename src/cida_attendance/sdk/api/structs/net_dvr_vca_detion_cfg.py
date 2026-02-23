from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .net_dvr_handleexception_v40 import NET_DVR_HANDLEEXCEPTION_V40


class struct__NET_DVR_VCA_DETION_CFG(Structure):
    pass

_S(struct__NET_DVR_VCA_DETION_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('struAlarmSched', (NET_DVR_SCHEDTIME * 8) * 7),
    ('struHandleException', NET_DVR_HANDLEEXCEPTION_V40),
    ('dwMaxRelRecordChanNum', DWORD),
    ('dwRelRecordChanNum', DWORD),
    ('dwRelRecordChan', DWORD * int((32 + 32))),
    ('byEnablePreset', BYTE * int((32 + 32))),
    ('byPresetNo', BYTE * int((32 + 32))),
    ('byEnableCruise', BYTE * int((32 + 32))),
    ('byCruiseNo', BYTE * int((32 + 32))),
    ('byEnablePtzTrack', BYTE * int((32 + 32))),
    ('byPTZTrack', BYTE * int((32 + 32))),
    ('struHolidayTime', NET_DVR_SCHEDTIME * 8),
    ('byRes', BYTE * 224),
])

NET_DVR_VCA_DETION_CFG = struct__NET_DVR_VCA_DETION_CFG
LPNET_DVR_VCA_DETION_CFG = POINTER(struct__NET_DVR_VCA_DETION_CFG)
_NET_DVR_VCA_DETION_CFG = struct__NET_DVR_VCA_DETION_CFG
