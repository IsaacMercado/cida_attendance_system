from ctypes import Union

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .net_matrix_analogmatrix import NET_MATRIX_ANALOGMATRIX
from .net_matrix_digitalmatrix import NET_MATRIX_DIGITALMATRIX


class union_tagNET_MATRIX_UNION(Union):
    pass

_S(union_tagNET_MATRIX_UNION, [
    ('struDigitalMatrix', NET_MATRIX_DIGITALMATRIX),
    ('struAnalogMatrix', NET_MATRIX_ANALOGMATRIX),
])

NET_MATRIX_UNION = union_tagNET_MATRIX_UNION
LPNET_MATRIX_UNION = POINTER(union_tagNET_MATRIX_UNION)
tagNET_MATRIX_UNION = union_tagNET_MATRIX_UNION
