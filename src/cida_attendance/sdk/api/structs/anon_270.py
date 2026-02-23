from ctypes import Union

from ..base_classes import _S
from .anon_264 import struct_anon_264
from .anon_265 import struct_anon_265
from .anon_266 import struct_anon_266
from .anon_267 import struct_anon_267
from .anon_268 import struct_anon_268
from .anon_269 import struct_anon_269


class union_anon_270(Union):
    pass

_S(union_anon_270, [
    ('struAlarmRet', struct_anon_264),
    ('struMotionRet', struct_anon_265),
    ('struVcaRet', struct_anon_266),
    ('struInquestRet', struct_anon_267),
    ('struStreamIDRet', struct_anon_268),
    ('struTrialRet', struct_anon_269),
])

