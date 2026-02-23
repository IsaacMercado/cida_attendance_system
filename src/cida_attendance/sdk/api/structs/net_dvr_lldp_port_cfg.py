from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LLDP_PORT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_LLDP_PORT_CFG, [
    ('byCardNo', BYTE),
    ('byPortNo', BYTE),
    ('byEnabledTx', BYTE),
    ('byEnabledRx', BYTE),
    ('byRes', BYTE * 12),
])

NET_DVR_LLDP_PORT_CFG = struct_tagNET_DVR_LLDP_PORT_CFG
LPNET_DVR_LLDP_PORT_CFG = POINTER(struct_tagNET_DVR_LLDP_PORT_CFG)
tagNET_DVR_LLDP_PORT_CFG = struct_tagNET_DVR_LLDP_PORT_CFG
