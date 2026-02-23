from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_dev_info import NET_VCA_DEV_INFO


class struct_tagNET_VCA_FACESNAP_INFO_ALARM(Structure):
    pass

_S(struct_tagNET_VCA_FACESNAP_INFO_ALARM, [
    ('dwRelativeTime', DWORD),
    ('dwAbsTime', DWORD),
    ('dwSnapFacePicID', DWORD),
    ('dwSnapFacePicLen', DWORD),
    ('struDevInfo', NET_VCA_DEV_INFO),
    ('byFaceScore', BYTE),
    ('bySex', BYTE),
    ('byGlasses', BYTE),
    ('byAge', BYTE),
    ('byAgeDeviation', BYTE),
    ('byAgeGroup', BYTE),
    ('byFacePicQuality', BYTE),
    ('byRes', BYTE),
    ('dwUIDLen', DWORD),
    ('pUIDBuffer', POINTER(BYTE)),
    ('fStayDuration', c_float),
    ('pBuffer1', POINTER(BYTE)),
])

NET_VCA_FACESNAP_INFO_ALARM = struct_tagNET_VCA_FACESNAP_INFO_ALARM
LPNET_VCA_FACESNAP_INFO_ALARM = POINTER(struct_tagNET_VCA_FACESNAP_INFO_ALARM)
tagNET_VCA_FACESNAP_INFO_ALARM = struct_tagNET_VCA_FACESNAP_INFO_ALARM
