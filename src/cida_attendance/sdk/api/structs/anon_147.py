from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_147(Structure):
    pass

_S(struct_anon_147, [
    ('dwSize', DWORD),
    ('dwAlarmOutChan', DWORD),
    ('dwAlarmChanSwitchTime', DWORD),
    ('dwAuxSwitchTime', DWORD * 4),
    ('byAuxOrder', (BYTE * 16) * 4),
])

NET_DVR_AUXOUTCFG = struct_anon_147
LPNET_DVR_AUXOUTCFG = POINTER(struct_anon_147)
