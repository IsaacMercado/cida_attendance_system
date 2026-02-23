from ctypes import Structure, c_int

from ..base_classes import _S
from ..ctypes_preamble import POINTER


class struct__tagNET_DVR_LINE_VOLTAGE(Structure):
    pass

_S(struct__tagNET_DVR_LINE_VOLTAGE, [
    ('iLineVolAB', c_int),
    ('iLineVolBC', c_int),
    ('iLineVolCA', c_int),
    ('iAverageLineVol', c_int),
])

NET_DVR_LINE_VOLTAGE = struct__tagNET_DVR_LINE_VOLTAGE
LPNET_DVR_LINE_VOLTAGE = POINTER(struct__tagNET_DVR_LINE_VOLTAGE)
_tagNET_DVR_LINE_VOLTAGE = struct__tagNET_DVR_LINE_VOLTAGE
