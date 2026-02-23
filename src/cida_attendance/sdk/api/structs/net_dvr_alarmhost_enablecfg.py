from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMHOST_ENABLECFG(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_ENABLECFG, [
    ('dwSize', DWORD),
    ('byAudioOutEnable', BYTE * 32),
    ('byElectroLockEnable', BYTE * 32),
    ('byMobileGateEnable', BYTE * 32),
    ('bySirenEnable', BYTE * 8),
    ('bySerialPurpose', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_ALARMHOST_ENABLECFG = struct_tagNET_DVR_ALARMHOST_ENABLECFG
LPNET_DVR_ALARMHOST_ENABLECFG = POINTER(struct_tagNET_DVR_ALARMHOST_ENABLECFG)
tagNET_DVR_ALARMHOST_ENABLECFG = struct_tagNET_DVR_ALARMHOST_ENABLECFG
