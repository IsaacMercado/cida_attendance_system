from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .anon_54 import NET_DVR_PRESETCHAN_INFO
from .anon_55 import NET_DVR_CRUISECHAN_INFO
from .anon_56 import NET_DVR_PTZTRACKCHAN_INFO


class struct_tagNET_DVR_ALARMINCFG_V40(Structure):
    pass

_S(struct_tagNET_DVR_ALARMINCFG_V40, [
    ('dwSize', DWORD),
    ('sAlarmInName', BYTE * 32),
    ('byAlarmType', BYTE),
    ('byAlarmInHandle', BYTE),
    ('byChannel', BYTE),
    ('byInputType', BYTE),
    ('dwHandleType', DWORD),
    ('dwMaxRelAlarmOutChanNum', DWORD),
    ('dwRelAlarmOutChanNum', DWORD),
    ('dwRelAlarmOut', DWORD * int((4096 + 32))),
    ('struAlarmTime', (NET_DVR_SCHEDTIME * 8) * 7),
    ('dwMaxRecordChanNum', DWORD),
    ('dwCurRecordChanNum', DWORD),
    ('dwRelRecordChan', DWORD * 512),
    ('dwMaxEnablePtzCtrlNun', DWORD),
    ('dwEnablePresetChanNum', DWORD),
    ('struPresetChanInfo', NET_DVR_PRESETCHAN_INFO * 512),
    ('byPresetDurationTime', BYTE * 512),
    ('byRes2', BYTE * 4),
    ('dwEnableCruiseChanNum', DWORD),
    ('struCruiseChanInfo', NET_DVR_CRUISECHAN_INFO * 512),
    ('dwEnablePtzTrackChanNum', DWORD),
    ('struPtzTrackInfo', NET_DVR_PTZTRACKCHAN_INFO * 512),
    ('wEventType', WORD * 64),
    ('byRes', BYTE * 128),
])

NET_DVR_ALARMINCFG_V40 = struct_tagNET_DVR_ALARMINCFG_V40
LPNET_DVR_ALARMINCFG_V40 = POINTER(struct_tagNET_DVR_ALARMINCFG_V40)
tagNET_DVR_ALARMINCFG_V40 = struct_tagNET_DVR_ALARMINCFG_V40
