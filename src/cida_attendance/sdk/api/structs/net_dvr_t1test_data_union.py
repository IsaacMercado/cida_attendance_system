from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_t1test_send_data_buzzer import NET_DVR_T1TEST_SEND_DATA_BUZZER
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class union_NET_DVR_T1TEST_DATA_UNION(Union):
    pass

_S(union_NET_DVR_T1TEST_DATA_UNION, [
    ('byUnionLen', BYTE * 32),
    ('struBuzzer', NET_DVR_T1TEST_SEND_DATA_BUZZER),
    ('struCurTime', NET_DVR_TIME_V30),
])

NET_DVR_T1TEST_DATA_UNION = union_NET_DVR_T1TEST_DATA_UNION
LPNET_DVR_T1TEST_DATA_UNION = POINTER(union_NET_DVR_T1TEST_DATA_UNION)
NET_DVR_T1TEST_DATA_UNION = union_NET_DVR_T1TEST_DATA_UNION
