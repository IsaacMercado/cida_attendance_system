from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ESATA_MINISAS_USAGE(Structure):
    pass

_S(struct_tagNET_DVR_ESATA_MINISAS_USAGE, [
    ('dwSize', DWORD),
    ('byESATAUsage', BYTE * 16),
    ('byMiniSASUsage', BYTE * 96),
    ('byRes', BYTE * 32),
])

NET_DVR_ESATA_MINISAS_USAGE = struct_tagNET_DVR_ESATA_MINISAS_USAGE
LPNET_DVR_ESATA_MINISAS_USAGE = POINTER(struct_tagNET_DVR_ESATA_MINISAS_USAGE)
tagNET_DVR_ESATA_MINISAS_USAGE = struct_tagNET_DVR_ESATA_MINISAS_USAGE
