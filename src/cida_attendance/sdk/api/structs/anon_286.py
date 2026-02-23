from ctypes import Union

from ..base_classes import _S, BYTE
from .anon_278 import struct_anon_278
from .anon_279 import struct_anon_279
from .anon_280 import struct_anon_280
from .anon_281 import struct_anon_281
from .anon_282 import struct_anon_282
from .anon_283 import struct_anon_283
from .anon_284 import struct_anon_284
from .anon_285 import struct_anon_285


class union_anon_286(Union):
    pass

_S(union_anon_286, [
    ('byLen', BYTE * 800),
    ('struAlarmRet', struct_anon_278),
    ('struMotionRet', struct_anon_279),
    ('struVcaRet', struct_anon_280),
    ('struInquestRet', struct_anon_281),
    ('struStreamIDRet', struct_anon_282),
    ('struPosRet', struct_anon_283),
    ('struTrialRet', struct_anon_284),
    ('struIOTRet', struct_anon_285),
])

