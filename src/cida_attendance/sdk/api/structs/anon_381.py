from ctypes import Union

from ..base_classes import _S, BYTE
from .anon_374 import struct_anon_374
from .anon_375 import struct_anon_375
from .anon_376 import struct_anon_376
from .anon_377 import struct_anon_377
from .anon_378 import struct_anon_378
from .anon_379 import struct_anon_379
from .anon_380 import struct_anon_380


class union_anon_381(Union):
    pass

_S(union_anon_381, [
    ('byRes', BYTE * 740),
    ('struNtpPara', struct_anon_374),
    ('struNasPara', struct_anon_375),
    ('struFtpPara', struct_anon_376),
    ('struEmailPara', struct_anon_377),
    ('struIpPara', struct_anon_378),
    ('struCloudStoragePara', struct_anon_379),
    ('struPhoneNumPara', struct_anon_380),
])

