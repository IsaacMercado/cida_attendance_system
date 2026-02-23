from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, USHORT
from ..ctypes_preamble import POINTER


class struct_anon_115(Structure):
    pass

_S(struct_anon_115, [
    ('m_Year', USHORT),
    ('m_Month', USHORT),
    ('m_Day', USHORT),
    ('m_Hour', USHORT),
    ('m_Minute', USHORT),
    ('m_Second', USHORT),
    ('DeviceName', BYTE * 24),
    ('dwChannelNumer', DWORD),
    ('CardNumber', BYTE * 32),
    ('cTradeType', c_char * 12),
    ('dwCash', DWORD),
])

NET_DVR_TRADEINFO = struct_anon_115
LPNET_DVR_TRADEINFO = POINTER(struct_anon_115)
