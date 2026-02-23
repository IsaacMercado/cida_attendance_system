from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct__NET_DVR_DSP_PARAMETER_CFG(Structure):
    pass

_S(struct__NET_DVR_DSP_PARAMETER_CFG, [
    ('byFBCEnable', BYTE),
    ('byVolume', BYTE),
    ('byRes', BYTE * 22),
])

NET_DVR_DSP_PARAMETER_CFG = struct__NET_DVR_DSP_PARAMETER_CFG
LPNET_DVR_DSP_PARAMETER_CFG = POINTER(struct__NET_DVR_DSP_PARAMETER_CFG)
_NET_DVR_DSP_PARAMETER_CFG = struct__NET_DVR_DSP_PARAMETER_CFG
