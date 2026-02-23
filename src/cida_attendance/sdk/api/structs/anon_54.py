from ctypes import Structure

from ..base_classes import _S, DWORD


class struct_anon_54(Structure):
    pass

_S(struct_anon_54, [
    ('dwEnablePresetChan', DWORD),
    ('dwPresetPointNo', DWORD),
])

NET_DVR_PRESETCHAN_INFO = struct_anon_54
LPNET_DVR_PRESETCHAN_INFO = struct_anon_54
