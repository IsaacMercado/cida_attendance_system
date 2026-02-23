from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DATE_FORMAT(Structure):
    pass

_S(struct_tagNET_DVR_DATE_FORMAT, [
    ('byMonth', BYTE),
    ('byDay', BYTE),
    ('byYear', BYTE),
    ('byDateForm', BYTE),
    ('byRes', BYTE * 20),
    ('chSeprator', c_char * 4),
    ('chDisplaySeprator', c_char * 4),
    ('byDisplayForm', BYTE),
    ('res', BYTE * 27),
])

NET_DVR_DATE_FORMAT = struct_tagNET_DVR_DATE_FORMAT
LPNET_DVR_DATE_FORMAT = POINTER(struct_tagNET_DVR_DATE_FORMAT)
tagNET_DVR_DATE_FORMAT = struct_tagNET_DVR_DATE_FORMAT
