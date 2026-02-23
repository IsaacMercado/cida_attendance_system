from ctypes import Union

from ..base_classes import _S, BYTE
from .anon_231 import struct_anon_231
from .anon_232 import struct_anon_232
from .anon_233 import struct_anon_233
from .anon_234 import struct_anon_234
from .anon_235 import struct_anon_235
from .anon_236 import struct_anon_236
from .anon_237 import struct_anon_237
from .anon_238 import struct_anon_238
from .anon_239 import struct_anon_239
from .anon_240 import struct_anon_240
from .anon_241 import struct_anon_241


class union_anon_242(Union):
    pass

_S(union_anon_242, [
    ('byLen', BYTE * 300),
    ('struAlarmParam', struct_anon_231),
    ('struAlarmParamByValue', struct_anon_232),
    ('struMotionParam', struct_anon_233),
    ('struMotionParamByValue', struct_anon_234),
    ('struVcaParam', struct_anon_235),
    ('struVcaParamByValue', struct_anon_236),
    ('struInquestParam', struct_anon_237),
    ('struVCADetectByBit', struct_anon_238),
    ('struVCADetectByValue', struct_anon_239),
    ('struStreamIDParam', struct_anon_240),
    ('struTrialParam', struct_anon_241),
])

