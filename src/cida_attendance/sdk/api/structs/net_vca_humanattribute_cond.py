from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_areainfocfg import NET_DVR_AREAINFOCFG


class struct_tagNET_VCA_HUMANATTRIBUTE_COND(Structure):
    pass

_S(struct_tagNET_VCA_HUMANATTRIBUTE_COND, [
    ('bySex', BYTE),
    ('byCertificateType', BYTE),
    ('byStartBirthDate', BYTE * 10),
    ('byEndBirthDate', BYTE * 10),
    ('byName', BYTE * 32),
    ('struNativePlace', NET_DVR_AREAINFOCFG),
    ('byCertificateNumber', BYTE * 32),
    ('byRes', BYTE * 20),
])

NET_VCA_HUMANATTRIBUTE_COND = struct_tagNET_VCA_HUMANATTRIBUTE_COND
LPNET_VCA_HUMANATTRIBUTE_COND = POINTER(struct_tagNET_VCA_HUMANATTRIBUTE_COND)
tagNET_VCA_HUMANATTRIBUTE_COND = struct_tagNET_VCA_HUMANATTRIBUTE_COND
