from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagVEDIOPLATLOG(Structure):
    pass

_S(struct_tagVEDIOPLATLOG, [
    ('bySearchCondition', BYTE),
    ('byDevSequence', BYTE),
    ('sSerialNumber', BYTE * 48),
    ('byMacAddr', BYTE * 6),
])

NET_DVR_VEDIOPLATLOG = struct_tagVEDIOPLATLOG
LPNET_DVR_VEDIOPLATLOG = POINTER(struct_tagVEDIOPLATLOG)
tagVEDIOPLATLOG = struct_tagVEDIOPLATLOG
