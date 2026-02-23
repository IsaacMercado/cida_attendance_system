from ctypes import Union

from ..base_classes import _S, BYTE
from .anon_243 import struct_anon_243
from .anon_244 import struct_anon_244
from .anon_245 import struct_anon_245
from .anon_246 import struct_anon_246
from .anon_247 import struct_anon_247
from .anon_248 import struct_anon_248
from .anon_249 import struct_anon_249
from .anon_250 import struct_anon_250
from .anon_251 import struct_anon_251


class union_anon_252(Union):
    pass

_S(union_anon_252, [
    ('byLen', BYTE * 800),
    ('struAlarmParam', struct_anon_243),
    ('struMotionParam', struct_anon_244),
    ('struVcaParam', struct_anon_245),
    ('struInquestParam', struct_anon_246),
    ('struVCADetect', struct_anon_247),
    ('struStreamIDParam', struct_anon_248),
    ('struPosAlarm', struct_anon_249),
    ('struTrialParam', struct_anon_250),
    ('struACSAlarm', struct_anon_251),
])

