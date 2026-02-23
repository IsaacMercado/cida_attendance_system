from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_matrixsubsysteminfo import NET_DVR_MATRIXSUBSYSTEMINFO


class struct_tagNET_DVR_MATRIXGATEWAYNOTE(Structure):
    pass

_S(struct_tagNET_DVR_MATRIXGATEWAYNOTE, [
    ('wTrunkInToOutAbility', WORD),
    ('wTrunkOutToInAbility', WORD),
    ('byRes', BYTE * 4),
    ('struInputNote', NET_DVR_MATRIXSUBSYSTEMINFO),
    ('struOutputNote', NET_DVR_MATRIXSUBSYSTEMINFO),
])

NET_DVR_MATRIXGATEWAYNOTE = struct_tagNET_DVR_MATRIXGATEWAYNOTE
LPNET_DVR_MATRIXGATEWAYNOTE = POINTER(struct_tagNET_DVR_MATRIXGATEWAYNOTE)
tagNET_DVR_MATRIXGATEWAYNOTE = struct_tagNET_DVR_MATRIXGATEWAYNOTE
