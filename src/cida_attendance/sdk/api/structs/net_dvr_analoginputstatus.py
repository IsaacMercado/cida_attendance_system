from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ANALOGINPUTSTATUS(Structure):
    pass

_S(struct_tagNET_DVR_ANALOGINPUTSTATUS, [
    ('dwLostFrame', DWORD),
    ('byHaveSignal', BYTE),
    ('byVideoFormat', BYTE),
    ('byRes', BYTE * 46),
])

NET_DVR_ANALOGINPUTSTATUS = struct_tagNET_DVR_ANALOGINPUTSTATUS
LPNET_DVR_ANALOGINPUTSTATUS = POINTER(struct_tagNET_DVR_ANALOGINPUTSTATUS)
tagNET_DVR_ANALOGINPUTSTATUS = struct_tagNET_DVR_ANALOGINPUTSTATUS
