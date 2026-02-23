from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_pdc_enter_direction import NET_DVR_PDC_ENTER_DIRECTION
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_DVR_PDC_RULE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_PDC_RULE_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 23),
    ('struPolygon', NET_VCA_POLYGON),
    ('struEnterDirection', NET_DVR_PDC_ENTER_DIRECTION),
])

NET_DVR_PDC_RULE_CFG = struct_tagNET_DVR_PDC_RULE_CFG
LPNET_DVR_PDC_RULE_CFG = POINTER(struct_tagNET_DVR_PDC_RULE_CFG)
tagNET_DVR_PDC_RULE_CFG = struct_tagNET_DVR_PDC_RULE_CFG
