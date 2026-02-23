from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct__NET_VCA_DURATION_(Structure):
    pass

_S(struct__NET_VCA_DURATION_, [
    ('wRelationEventType', WORD),
    ('byRes', BYTE * 90),
])

NET_VCA_DURATION = struct__NET_VCA_DURATION_
LPNET_VCA_DURATION = POINTER(struct__NET_VCA_DURATION_)
_NET_VCA_DURATION_ = struct__NET_VCA_DURATION_
