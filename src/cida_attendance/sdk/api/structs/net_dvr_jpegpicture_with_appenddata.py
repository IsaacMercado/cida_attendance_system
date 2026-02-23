from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String
from .net_vca_rect import NET_VCA_RECT


class struct_tagNET_DVR_JPEGPICTURE_WITH_APPENDDATA(Structure):
    pass

_S(struct_tagNET_DVR_JPEGPICTURE_WITH_APPENDDATA, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('dwJpegPicLen', DWORD),
    ('pJpegPicBuff', String),
    ('dwJpegPicWidth', DWORD),
    ('dwJpegPicHeight', DWORD),
    ('dwP2PDataLen', DWORD),
    ('pP2PDataBuff', String),
    ('byIsFreezedata', BYTE),
    ('byRes1', BYTE * 3),
    ('dwVisiblePicLen', DWORD),
    ('pVisiblePicBuff', String),
    ('struThermalValidRect', NET_VCA_RECT),
    ('struVisibleValidRect', NET_VCA_RECT),
    ('byRes', BYTE * 208),
])

NET_DVR_JPEGPICTURE_WITH_APPENDDATA = struct_tagNET_DVR_JPEGPICTURE_WITH_APPENDDATA
LPNET_DVR_JPEGPICTURE_WITH_APPENDDATA = POINTER(struct_tagNET_DVR_JPEGPICTURE_WITH_APPENDDATA)
tagNET_DVR_JPEGPICTURE_WITH_APPENDDATA = struct_tagNET_DVR_JPEGPICTURE_WITH_APPENDDATA
