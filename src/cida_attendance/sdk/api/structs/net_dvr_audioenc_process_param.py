from ctypes import Structure, c_int, c_ubyte

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from ..enums import ENUM_AUDIO_ENC_MODE


class struct__NET_DVR_AUDIOENC_PROCESS_PARAM_(Structure):
    pass

_S(struct__NET_DVR_AUDIOENC_PROCESS_PARAM_, [
    ('in_buf', POINTER(c_ubyte)),
    ('out_buf', POINTER(c_ubyte)),
    ('out_frame_size', DWORD),
    ('g726enc_reset', c_int),
    ('g711_type', c_int),
    ('enc_mode', ENUM_AUDIO_ENC_MODE),
    ('reserved', c_int * 16),
])

NET_DVR_AUDIOENC_PROCESS_PARAM = struct__NET_DVR_AUDIOENC_PROCESS_PARAM_
_NET_DVR_AUDIOENC_PROCESS_PARAM_ = struct__NET_DVR_AUDIOENC_PROCESS_PARAM_
