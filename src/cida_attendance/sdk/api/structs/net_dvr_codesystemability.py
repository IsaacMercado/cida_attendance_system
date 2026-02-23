from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CODESYSTEMABILITY(Structure):
    pass

_S(struct_tagNET_DVR_CODESYSTEMABILITY, [
    ('dwSize', DWORD),
    ('dwAbilityVersion', DWORD),
    ('dwSupportMaxVideoFrameRate', DWORD),
    ('dwSupportRecordType', DWORD),
    ('bySupportLinkMode', BYTE),
    ('bySupportStringRow', BYTE),
    ('byRes1', BYTE * 2),
    ('byMainStreamSupportResolution', BYTE * 32),
    ('bySubStreamSupportResolution', BYTE * 32),
    ('byEventStreamSupportResolution', BYTE * 32),
    ('byRes2', BYTE * 28),
])

NET_DVR_CODESYSTEMABILITY = struct_tagNET_DVR_CODESYSTEMABILITY
LPNET_DVR_CODESYSTEMABILITY = POINTER(struct_tagNET_DVR_CODESYSTEMABILITY)
tagNET_DVR_CODESYSTEMABILITY = struct_tagNET_DVR_CODESYSTEMABILITY
