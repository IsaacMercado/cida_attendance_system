from ctypes import Structure

from ..base_classes import _S, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_AREAINFOCFG(Structure):
    pass

_S(struct_tagNET_DVR_AREAINFOCFG, [
    ('wNationalityID', WORD),
    ('wProvinceID', WORD),
    ('wCityID', WORD),
    ('wCountyID', WORD),
    ('dwCode', DWORD),
])

NET_DVR_AREAINFOCFG = struct_tagNET_DVR_AREAINFOCFG
LPNET_DVR_AREAINFOCFG = POINTER(struct_tagNET_DVR_AREAINFOCFG)
tagNET_DVR_AREAINFOCFG = struct_tagNET_DVR_AREAINFOCFG
