from ctypes import Union

from ..base_classes import _S, BYTE
from .anon_253 import struct_anon_253
from .anon_254 import struct_anon_254
from .anon_255 import struct_anon_255
from .anon_256 import struct_anon_256
from .anon_257 import struct_anon_257
from .anon_258 import struct_anon_258
from .anon_259 import struct_anon_259
from .anon_260 import struct_anon_260
from .anon_261 import struct_anon_261
from .anon_262 import struct_anon_262


class union_anon_263(Union):
    pass

_S(union_anon_263, [
    ('byLen', BYTE * 800),
    ('struAlarmParam', struct_anon_253),
    ('struMotionParam', struct_anon_254),
    ('struVcaParam', struct_anon_255),
    ('struInquestParam', struct_anon_256),
    ('struVCADetect', struct_anon_257),
    ('struStreamIDParam', struct_anon_258),
    ('struPosAlarm', struct_anon_259),
    ('struTrialParam', struct_anon_260),
    ('struACSAlarm', struct_anon_261),
    ('struIOTAlarm', struct_anon_262),
])

