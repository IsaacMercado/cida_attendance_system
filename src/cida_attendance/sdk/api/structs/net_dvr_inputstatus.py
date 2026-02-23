from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_inputstatus_union import NET_DVR_INPUTSTATUS_UNION


class struct_tagNET_DVR_INPUTSTATUS(Structure):
    pass

_S(struct_tagNET_DVR_INPUTSTATUS, [
    ('wInputNo', WORD),
    ('byInputType', BYTE),
    ('byRes1', BYTE * 9),
    ('struStatusUnion', NET_DVR_INPUTSTATUS_UNION),
    ('byRes2', BYTE * 16),
])

NET_DVR_INPUTSTATUS = struct_tagNET_DVR_INPUTSTATUS
LPNET_DVR_INPUTSTATUS = POINTER(struct_tagNET_DVR_INPUTSTATUS)
tagNET_DVR_INPUTSTATUS = struct_tagNET_DVR_INPUTSTATUS
