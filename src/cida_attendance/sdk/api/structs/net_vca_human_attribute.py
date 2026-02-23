from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_areainfocfg import NET_DVR_AREAINFOCFG


class struct_tagNET_VCA_HUMAN_ATTRIBUTE(Structure):
    pass

_S(struct_tagNET_VCA_HUMAN_ATTRIBUTE, [
    ('bySex', BYTE),
    ('byCertificateType', BYTE),
    ('byBirthDate', BYTE * 10),
    ('byName', BYTE * 32),
    ('struNativePlace', NET_DVR_AREAINFOCFG),
    ('byCertificateNumber', BYTE * 32),
    ('dwPersonInfoExtendLen', DWORD),
    ('pPersonInfoExtend', POINTER(BYTE)),
    ('byAgeGroup', BYTE),
    ('byRes2', BYTE * 3),
    ('pThermalData', POINTER(BYTE)),
])

NET_VCA_HUMAN_ATTRIBUTE = struct_tagNET_VCA_HUMAN_ATTRIBUTE
LPNET_VCA_HUMAN_ATTRIBUTE = POINTER(struct_tagNET_VCA_HUMAN_ATTRIBUTE)
tagNET_VCA_HUMAN_ATTRIBUTE = struct_tagNET_VCA_HUMAN_ATTRIBUTE
