from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER, String
from .net_vca_rect import NET_VCA_RECT


class struct_tagNET_DVR_PLATE_INFO(Structure):
    pass

_S(struct_tagNET_DVR_PLATE_INFO, [
    ('byPlateType', BYTE),
    ('byColor', BYTE),
    ('byBright', BYTE),
    ('byLicenseLen', BYTE),
    ('byEntireBelieve', BYTE),
    ('byRegion', BYTE),
    ('byCountry', BYTE),
    ('byArea', BYTE),
    ('byPlateSize', BYTE),
    ('byAddInfoFlag', BYTE),
    ('wCRIndex', WORD),
    ('byRes', BYTE * 4),
    ('pAddInfoBuffer', POINTER(BYTE)),
    ('sPlateCategory', c_char * 8),
    ('dwXmlLen', DWORD),
    ('pXmlBuf', String),
    ('struPlateRect', NET_VCA_RECT),
    ('sLicense', c_char * 16),
    ('byBelieve', BYTE * 16),
])

NET_DVR_PLATE_INFO = struct_tagNET_DVR_PLATE_INFO
LPNET_DVR_PLATE_INFO = POINTER(struct_tagNET_DVR_PLATE_INFO)
tagNET_DVR_PLATE_INFO = struct_tagNET_DVR_PLATE_INFO
