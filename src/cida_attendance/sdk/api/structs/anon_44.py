from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD


class struct_anon_44(Structure):
    pass

_S(struct_anon_44, [
    ('dwType', DWORD),
    ('byDescribe', BYTE * 16),
])

NET_DVR_PTZ_PROTOCOL = struct_anon_44
