from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_alarm_record_exception import NET_ALARM_RECORD_EXCEPTION
from .net_alarm_recordfile_loss import NET_ALARM_RECORDFILE_LOSS
from .net_alarm_resource_usage import NET_ALARM_RESOURCE_USAGE
from .net_alarm_stream_exception import NET_ALARM_STREAM_EXCEPTION


class union_tagNET_ALARM_CVR_SUBINFO_UNION(Union):
    pass

_S(union_tagNET_ALARM_CVR_SUBINFO_UNION, [
    ('byLen', BYTE * 492),
    ('struRecordLost', NET_ALARM_RECORDFILE_LOSS),
    ('struStreamException', NET_ALARM_STREAM_EXCEPTION),
    ('struResourceUsage', NET_ALARM_RESOURCE_USAGE),
    ('struRecordException', NET_ALARM_RECORD_EXCEPTION),
])

NET_ALARM_CVR_SUBINFO_UNION = union_tagNET_ALARM_CVR_SUBINFO_UNION
LPNET_ALARM_CVR_SUBINFO_UNION = POINTER(union_tagNET_ALARM_CVR_SUBINFO_UNION)
tagNET_ALARM_CVR_SUBINFO_UNION = union_tagNET_ALARM_CVR_SUBINFO_UNION
