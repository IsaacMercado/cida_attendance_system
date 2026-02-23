from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_lamp_param import NET_DVR_LAMP_PARAM


class struct_tagNET_DVR_EXTERNAL_PARKLAMP(Structure):
    pass

_S(struct_tagNET_DVR_EXTERNAL_PARKLAMP, [
    ('struLampParam', NET_DVR_LAMP_PARAM * 8),
    ('byLampType', BYTE),
    ('byRes', BYTE * 7),
])

NET_DVR_EXTERNAL_PARKLAMP = struct_tagNET_DVR_EXTERNAL_PARKLAMP
LPNET_DVR_EXTERNAL_PARKLAMP = POINTER(struct_tagNET_DVR_EXTERNAL_PARKLAMP)
tagNET_DVR_EXTERNAL_PARKLAMP = struct_tagNET_DVR_EXTERNAL_PARKLAMP
