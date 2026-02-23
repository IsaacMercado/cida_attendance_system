from ctypes import Union

from ..base_classes import _S, BYTE
from .anon_271 import struct_anon_271
from .anon_272 import struct_anon_272
from .anon_273 import struct_anon_273
from .anon_274 import struct_anon_274
from .anon_275 import struct_anon_275
from .anon_276 import struct_anon_276


class union_anon_277(Union):
    pass

_S(union_anon_277, [
    ('byLen', BYTE * 800),
    ('struAlarmRet', struct_anon_271),
    ('struMotionRet', struct_anon_272),
    ('struVcaRet', struct_anon_273),
    ('struInquestRet', struct_anon_274),
    ('struStreamIDRet', struct_anon_275),
    ('struPosRet', struct_anon_276),
])

