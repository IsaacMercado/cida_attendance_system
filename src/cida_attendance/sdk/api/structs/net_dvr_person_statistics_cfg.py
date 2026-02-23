from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PERSON_STATISTICS_CFG(Structure):
    pass

_S(struct_tagNET_DVR_PERSON_STATISTICS_CFG, [
    ('dwSize', DWORD),
    ('byEnableStatistics', BYTE),
    ('byEnableOfflineStatistics', BYTE),
    ('byCountSignalStatisticalStandard', BYTE),
    ('byRes', BYTE * 605),
])

NET_DVR_PERSON_STATISTICS_CFG = struct_tagNET_DVR_PERSON_STATISTICS_CFG
LPNET_DVR_PERSON_STATISTICS_CFG = POINTER(struct_tagNET_DVR_PERSON_STATISTICS_CFG)
tagNET_DVR_PERSON_STATISTICS_CFG = struct_tagNET_DVR_PERSON_STATISTICS_CFG
