from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_VCA_CHAN_WORKSTATUS(Structure):
    pass

_S(struct_tagNET_DVR_VCA_CHAN_WORKSTATUS, [
    ('byJointed', BYTE),
    ('byRes1', BYTE * 3),
    ('struIP', NET_DVR_IPADDR),
    ('wPort', WORD),
    ('wChannel', WORD),
    ('byVcaChanStatus', BYTE),
    ('byRes2', BYTE * 19),
])

NET_DVR_VCA_CHAN_WORKSTATUS = struct_tagNET_DVR_VCA_CHAN_WORKSTATUS
LPNET_DVR_VCA_CHAN_WORKSTATUS = POINTER(struct_tagNET_DVR_VCA_CHAN_WORKSTATUS)
tagNET_DVR_VCA_CHAN_WORKSTATUS = struct_tagNET_DVR_VCA_CHAN_WORKSTATUS
