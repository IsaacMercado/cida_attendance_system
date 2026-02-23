from ctypes import Union

from ..base_classes import _S, BYTE
from .anon_61 import struct_anon_61
from .anon_62 import struct_anon_62
from .anon_63 import struct_anon_63
from .anon_64 import struct_anon_64
from .anon_65 import struct_anon_65
from .anon_66 import struct_anon_66
from .anon_67 import struct_anon_67
from .anon_68 import struct_anon_68


class union_anon_69(Union):
    pass

_S(union_anon_69, [
    ('byUnionLen', BYTE * 116),
    ('struIOAlarm', struct_anon_61),
    ('struAlarmChannel', struct_anon_62),
    ('struAlarmHardDisk', struct_anon_63),
    ('struRecordingHost', struct_anon_64),
    ('struVoltageInstable', struct_anon_65),
    ('struPTLocking', struct_anon_66),
    ('struLogException', struct_anon_67),
    ('struAbnormalReboot', struct_anon_68),
])

