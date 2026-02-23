r"""Wrapper for HCNetSDK.h

Generated with:
scripts/generate_sdk/generate_sdk_bindings.py

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python

# End preamble
from .base_classes import *
from .constants import *
from .ctypes_preamble import *
from .ctypes_preamble import _variadic_function
from .enums import *
from .functions import *
from .macros import *
from .structs import *

_libs = {}
_libdirs = []

# Begin loader

from .ctypes_loader import *

# End loader

add_library_search_dirs([])

import os
import sys
from pathlib import Path
from typing import TYPE_CHECKING, Callable, TypeVar

if TYPE_CHECKING:
    from ctypes import _CData

R = TypeVar("R")

# --- Helper: Functions ---
# Reduces 6+ lines of setup per function to 1 line.
# Handles stdcall/cdecl, argtypes, restype, and error checking.
def _F(
    name: str,
    cc: str,
    res: R,
    args: list["_CData"],
    err=None,
) -> Callable[..., R] | None:
    if not _libs[lib_name].has(name, cc):
        return None
    func = _libs[lib_name].get(name, cc)
    func.argtypes = args
    func.restype = res
    # Handle strict String return types if needed (logic from ctypesgen)
    if res is String:
        if sizeof(c_int) == sizeof(c_void_p):
            func.restype = ReturnString
        else:
            func.errcheck = ReturnString
    if err:
        func.errcheck = err
    return func

# --- Helper: Variadic Functions ---
def _FV(
    name: str,
    cc: str,
    res: R,
    args: list["_CData"],
    err=None,
) -> Callable[..., R] | None:
    if not _libs[lib_name].has(name, cc):
        return None
    func = _libs[lib_name].get(name, cc)
    return _variadic_function(func, res, args, err)

def _cida_candidate_library_dirs():
    dirs = []
    env_dir = os.environ.get("CIDA_ATTENDANCE_LIBS_DIR")
    if env_dir:
        dirs.append(env_dir)

    nuitka_temp = os.environ.get("NUITKA_ONEFILE_TEMP_DIR")
    if nuitka_temp:
        dirs.append(os.path.join(nuitka_temp, "libs"))

    if hasattr(sys, "_MEIPASS"):
        dirs.append(os.path.join(sys._MEIPASS, "libs"))

    try:
        exe_dir = os.path.dirname(sys.executable)
        if exe_dir:
            dirs.append(os.path.join(exe_dir, "libs"))
            dirs.append(os.path.join(exe_dir, "_internal", "libs"))
    except Exception:
        pass

    try:
        here = Path(__file__).resolve().parent
        for parent in [here, *here.parents]:
            libs_dir = parent / "libs"
            if libs_dir.is_dir():
                dirs.append(str(libs_dir))
            internal_libs_dir = parent / "_internal" / "libs"
            if internal_libs_dir.is_dir():
                dirs.append(str(internal_libs_dir))
    except Exception:
        pass

    # Expand base dirs to include vendor subdirs when present.
    expanded = []
    for d in dirs:
        expanded.append(d)
        expanded.append(os.path.join(d, "HCNetSDKCom"))

    out = []
    seen = set()
    for d in expanded:
        if not d or d in seen:
            continue
        seen.add(d)
        if os.path.isdir(d):
            out.append(d)
    return out

add_library_search_dirs(_cida_candidate_library_dirs())

if sys.platform == "win32":
    lib_name = "HCNetSDK.dll"
elif sys.platform == "linux":
    lib_name = "libhcnetsdk.so"
else:
    raise OSError(f"Unsupported platform: {sys.platform}")

_libs[lib_name] = load_library(lib_name)

# No libraries

# No modules

for _lib in _libs.values():
    try:
        G726_EBCIN_DECOUT_SIZE = (c_uint).in_dll(_lib, "G726_EBCIN_DECOUT_SIZE")
        break
    except:
        pass

for _lib in _libs.values():
    try:
        G726_ENC_OUT_SIZE = (c_uint).in_dll(_lib, "G726_ENC_OUT_SIZE")
        break
    except:
        pass

for _lib in _libs.values():
    try:
        G726_DEC_IN_SIZE = (c_uint).in_dll(_lib, "G726_DEC_IN_SIZE")
        break
    except:
        pass

NET_DVR_Init = _F("NET_DVR_Init", "cdecl", c_int, [], None)

NET_DVR_Cleanup = _F("NET_DVR_Cleanup", "cdecl", c_int, [], None)

NET_DVR_SetExceptionCallBack_V30 = _F("NET_DVR_SetExceptionCallBack_V30", "cdecl", c_int, [UINT, POINTER(None), CFUNCTYPE(UNCHECKED(None), DWORD, LONG, LONG, POINTER(None)), POINTER(None)], None)

NET_DVR_DrawAreaInit = _F("NET_DVR_DrawAreaInit", "cdecl", c_int, [INITINFO, DWORD], None)

NET_DVR_DrawAreaRelease = _F("NET_DVR_DrawAreaRelease", "cdecl", c_int, [], None)

NET_DVR_LoadAllCom = _F("NET_DVR_LoadAllCom", "cdecl", c_int, [], None)

NET_DVR_SetDVRMessCallBack = _F("NET_DVR_SetDVRMessCallBack", "cdecl", c_int, [CFUNCTYPE(UNCHECKED(c_int), LONG, String, String, DWORD)], None)

NET_DVR_SetDVRMessCallBack_EX = _F("NET_DVR_SetDVRMessCallBack_EX", "cdecl", c_int, [CFUNCTYPE(UNCHECKED(c_int), LONG, LONG, String, DWORD)], None)

NET_DVR_SetDVRMessCallBack_NEW = _F("NET_DVR_SetDVRMessCallBack_NEW", "cdecl", c_int, [CFUNCTYPE(UNCHECKED(c_int), LONG, String, String, DWORD, WORD)], None)

NET_DVR_SetDVRMessageCallBack = _F("NET_DVR_SetDVRMessageCallBack", "cdecl", c_int, [CFUNCTYPE(UNCHECKED(c_int), LONG, String, String, DWORD, DWORD), DWORD], None)

NET_DVR_SetDVRMessageCallBack_V30 = _F("NET_DVR_SetDVRMessageCallBack_V30", "cdecl", c_int, [MSGCallBack, POINTER(None)], None)

NET_DVR_SetDVRMessageCallBack_V31 = _F("NET_DVR_SetDVRMessageCallBack_V31", "cdecl", c_int, [MSGCallBack_V31, POINTER(None)], None)

NET_DVR_SetDVRMessageCallBack_V50 = _F("NET_DVR_SetDVRMessageCallBack_V50", "cdecl", c_int, [c_int, MSGCallBack, POINTER(None)], None)

NET_DVR_SetDVRMessageCallBack_V51 = _F("NET_DVR_SetDVRMessageCallBack_V51", "cdecl", c_int, [c_int, MSGCallBack, POINTER(None)], None)

NET_DVR_SetConnectTime = _F("NET_DVR_SetConnectTime", "cdecl", c_int, [DWORD, DWORD], None)

NET_DVR_SetReconnect = _F("NET_DVR_SetReconnect", "cdecl", c_int, [DWORD, c_int], None)

NET_DVR_GetSDKVersion = _F("NET_DVR_GetSDKVersion", "cdecl", DWORD, [], None)

NET_DVR_GetSDKBuildVersion = _F("NET_DVR_GetSDKBuildVersion", "cdecl", DWORD, [], None)

NET_DVR_IsSupport = _F("NET_DVR_IsSupport", "cdecl", c_int, [], None)

NET_DVR_StartListen = _F("NET_DVR_StartListen", "cdecl", c_int, [String, WORD], None)

NET_DVR_StopListen = _F("NET_DVR_StopListen", "cdecl", c_int, [], None)

NET_DVR_StartListen_V30 = _F("NET_DVR_StartListen_V30", "cdecl", LONG, [String, WORD, MSGCallBack, POINTER(None)], None)

NET_DVR_StopListen_V30 = _F("NET_DVR_StopListen_V30", "cdecl", c_int, [LONG], None)

NET_DVR_StartServer = _F("NET_DVR_StartServer", "cdecl", LONG, [String, WORD, BYTE], None)

NET_DVR_StopServer = _F("NET_DVR_StopServer", "cdecl", c_int, [LONG], None)

NET_DVR_StartRecvNakedDataListen = _F("NET_DVR_StartRecvNakedDataListen", "cdecl", LONG, [NAKED_DATA_TYPE, LPNET_DVR_NAKED_DATA_PARAM], None)

NET_DVR_StopRecvNakedDataListen = _F("NET_DVR_StopRecvNakedDataListen", "cdecl", c_int, [LONG], None)

NET_DVR_SetNakedDataRecvCallBack = _F("NET_DVR_SetNakedDataRecvCallBack", "cdecl", c_int, [LONG, CFUNCTYPE(UNCHECKED(None), DWORD, POINTER(NET_DVR_NAKED_DATA_INFO), String, DWORD, POINTER(None)), POINTER(None)], None)

NET_DVR_Login = _F("NET_DVR_Login", "cdecl", LONG, [String, WORD, String, String, LPNET_DVR_DEVICEINFO], None)

NET_DVR_Login_V30 = _F("NET_DVR_Login_V30", "cdecl", LONG, [String, WORD, String, String, LPNET_DVR_DEVICEINFO_V30], None)

NET_DVR_Login_V40 = _F("NET_DVR_Login_V40", "cdecl", LONG, [LPNET_DVR_USER_LOGIN_INFO, LPNET_DVR_DEVICEINFO_V40], None)

NET_DVR_Login_Check = _F("NET_DVR_Login_Check", "cdecl", c_int, [String, WORD, String, String, LPNET_DVR_DEVICEINFO_V30], None)

NET_DVR_Logout = _F("NET_DVR_Logout", "cdecl", c_int, [LONG], None)

NET_DVR_Logout_V30 = _F("NET_DVR_Logout_V30", "cdecl", c_int, [LONG], None)

NET_DVR_GetLastError = _F("NET_DVR_GetLastError", "cdecl", DWORD, [], None)

NET_DVR_GetLastErrorModelCode = _F("NET_DVR_GetLastErrorModelCode", "cdecl", None, [POINTER(DWORD), POINTER(DWORD)], None)

NET_DVR_GetErrorMsg = _F("NET_DVR_GetErrorMsg", "cdecl", String, [POINTER(LONG)], None)

NET_DVR_SetShowMode = _F("NET_DVR_SetShowMode", "cdecl", c_int, [DWORD, COLORREF], None)

NET_DVR_GetDVRIPByResolveSvr = _F("NET_DVR_GetDVRIPByResolveSvr", "cdecl", c_int, [String, WORD, POINTER(BYTE), WORD, POINTER(BYTE), WORD, String], None)

NET_DVR_GetDVRIPByResolveSvr_EX = _F("NET_DVR_GetDVRIPByResolveSvr_EX", "cdecl", c_int, [String, WORD, POINTER(BYTE), WORD, POINTER(BYTE), WORD, String, POINTER(DWORD)], None)

NET_DVR_GetDVRNAMEByResolveSvr = _F("NET_DVR_GetDVRNAMEByResolveSvr", "cdecl", c_int, [String, WORD, String, String], None)

NET_DVR_PlayDirect = _F("NET_DVR_PlayDirect", "cdecl", LONG, [String, String, String, LPNET_DVR_CLIENTINFO, CFUNCTYPE(UNCHECKED(None), LONG, DWORD, POINTER(BYTE), DWORD, POINTER(None)), POINTER(None), c_int], None)

NET_DVR_RealPlay = _F("NET_DVR_RealPlay", "cdecl", LONG, [LONG, LPNET_DVR_CLIENTINFO], None)

NET_DVR_RealPlay_V30 = _F("NET_DVR_RealPlay_V30", "cdecl", LONG, [LONG, LPNET_DVR_CLIENTINFO, CFUNCTYPE(UNCHECKED(None), LONG, DWORD, POINTER(BYTE), DWORD, POINTER(None)), POINTER(None), c_int], None)

NET_DVR_RealPlay_V40 = _F("NET_DVR_RealPlay_V40", "cdecl", LONG, [LONG, LPNET_DVR_PREVIEWINFO, REALDATACALLBACK, POINTER(None)], None)

NET_DVR_RealPlaySpecial = _F("NET_DVR_RealPlaySpecial", "cdecl", LONG, [LONG, LPNET_DVR_PREVIEWINFO_SPECIAL, REALDATACALLBACK, POINTER(None)], None)

NET_DVR_GetLinkAddr = _F("NET_DVR_GetLinkAddr", "cdecl", c_int, [LONG, NET_DVR_LINK_KIND, LPNET_DVR_LINK_ADDR], None)

NET_DVR_StopRealPlay = _F("NET_DVR_StopRealPlay", "cdecl", c_int, [LONG], None)

NET_DVR_StopPlayDirect = _F("NET_DVR_StopPlayDirect", "cdecl", c_int, [LONG], None)

NET_DVR_RigisterDrawFun = _F("NET_DVR_RigisterDrawFun", "cdecl", c_int, [LONG, CFUNCTYPE(UNCHECKED(None), LONG, HDC, DWORD), DWORD], None)

NET_DVR_SetPlayerBufNumber = _F("NET_DVR_SetPlayerBufNumber", "cdecl", c_int, [LONG, DWORD], None)

NET_DVR_ThrowBFrame = _F("NET_DVR_ThrowBFrame", "cdecl", c_int, [LONG, DWORD], None)

NET_DVR_SetAudioMode = _F("NET_DVR_SetAudioMode", "cdecl", c_int, [DWORD], None)

NET_DVR_OpenSound = _F("NET_DVR_OpenSound", "cdecl", c_int, [LONG], None)

NET_DVR_CloseSound = _F("NET_DVR_CloseSound", "cdecl", c_int, [], None)

NET_DVR_OpenSoundShare = _F("NET_DVR_OpenSoundShare", "cdecl", c_int, [LONG], None)

NET_DVR_CloseSoundShare = _F("NET_DVR_CloseSoundShare", "cdecl", c_int, [LONG], None)

NET_DVR_Volume = _F("NET_DVR_Volume", "cdecl", c_int, [LONG, WORD], None)

NET_DVR_SaveRealData = _F("NET_DVR_SaveRealData", "cdecl", c_int, [LONG, String], None)

NET_DVR_StopSaveRealData = _F("NET_DVR_StopSaveRealData", "cdecl", c_int, [LONG], None)

NET_DVR_SetRealDataCallBack = _F("NET_DVR_SetRealDataCallBack", "cdecl", c_int, [LONG, CFUNCTYPE(UNCHECKED(None), LONG, DWORD, POINTER(BYTE), DWORD, DWORD), DWORD], None)

NET_DVR_SetRealDataCallBackEx = _F("NET_DVR_SetRealDataCallBackEx", "cdecl", c_int, [LONG, CFUNCTYPE(UNCHECKED(None), LONG, DWORD, POINTER(BYTE), DWORD, POINTER(None)), POINTER(None)], None)

NET_DVR_SetStandardDataCallBack = _F("NET_DVR_SetStandardDataCallBack", "cdecl", c_int, [LONG, CFUNCTYPE(UNCHECKED(None), LONG, DWORD, POINTER(BYTE), DWORD, DWORD), DWORD], None)

NET_DVR_SetStandardDataCallBackEx = _F("NET_DVR_SetStandardDataCallBackEx", "cdecl", c_int, [LONG, CFUNCTYPE(UNCHECKED(None), LONG, DWORD, POINTER(BYTE), DWORD, POINTER(None)), POINTER(None)], None)

NET_DVR_SetTransparentDataCallBack = _F("NET_DVR_SetTransparentDataCallBack", "cdecl", c_int, [LONG, CFUNCTYPE(UNCHECKED(None), LONG, DWORD, POINTER(BYTE), DWORD, POINTER(None)), POINTER(None)], None)

NET_DVR_CapturePicture = _F("NET_DVR_CapturePicture", "cdecl", c_int, [LONG, String], None)

NET_DVR_SetCapturePictureMode = _F("NET_DVR_SetCapturePictureMode", "cdecl", c_int, [DWORD], None)

NET_DVR_MakeKeyFrame = _F("NET_DVR_MakeKeyFrame", "cdecl", c_int, [LONG, LONG], None)

NET_DVR_MakeKeyFrameSub = _F("NET_DVR_MakeKeyFrameSub", "cdecl", c_int, [LONG, LONG], None)

NET_DVR_PTZControl = _F("NET_DVR_PTZControl", "cdecl", c_int, [LONG, DWORD, DWORD], None)

NET_DVR_PTZControl_Other = _F("NET_DVR_PTZControl_Other", "cdecl", c_int, [LONG, LONG, DWORD, DWORD], None)

NET_DVR_TransPTZ = _F("NET_DVR_TransPTZ", "cdecl", c_int, [LONG, String, DWORD], None)

NET_DVR_TransPTZ_Other = _F("NET_DVR_TransPTZ_Other", "cdecl", c_int, [LONG, LONG, String, DWORD], None)

NET_DVR_PTZPreset = _F("NET_DVR_PTZPreset", "cdecl", c_int, [LONG, DWORD, DWORD], None)

NET_DVR_PTZPreset_Other = _F("NET_DVR_PTZPreset_Other", "cdecl", c_int, [LONG, LONG, DWORD, DWORD], None)

NET_DVR_TransPTZ_EX = _F("NET_DVR_TransPTZ_EX", "cdecl", c_int, [LONG, String, DWORD], None)

NET_DVR_PTZControl_EX = _F("NET_DVR_PTZControl_EX", "cdecl", c_int, [LONG, DWORD, DWORD], None)

NET_DVR_PTZPreset_EX = _F("NET_DVR_PTZPreset_EX", "cdecl", c_int, [LONG, DWORD, DWORD], None)

NET_DVR_PTZCruise = _F("NET_DVR_PTZCruise", "cdecl", c_int, [LONG, DWORD, BYTE, BYTE, WORD], None)

NET_DVR_PTZCruise_Other = _F("NET_DVR_PTZCruise_Other", "cdecl", c_int, [LONG, LONG, DWORD, BYTE, BYTE, WORD], None)

NET_DVR_PTZCruise_EX = _F("NET_DVR_PTZCruise_EX", "cdecl", c_int, [LONG, DWORD, BYTE, BYTE, WORD], None)

NET_DVR_PTZTrack = _F("NET_DVR_PTZTrack", "cdecl", c_int, [LONG, DWORD], None)

NET_DVR_PTZTrack_Other = _F("NET_DVR_PTZTrack_Other", "cdecl", c_int, [LONG, LONG, DWORD], None)

NET_DVR_PTZTrack_EX = _F("NET_DVR_PTZTrack_EX", "cdecl", c_int, [LONG, DWORD], None)

NET_DVR_PTZControlWithSpeed = _F("NET_DVR_PTZControlWithSpeed", "cdecl", c_int, [LONG, DWORD, DWORD, DWORD], None)

NET_DVR_PTZControlWithSpeed_Other = _F("NET_DVR_PTZControlWithSpeed_Other", "cdecl", c_int, [LONG, LONG, DWORD, DWORD, DWORD], None)

NET_DVR_PTZControlWithSpeed_EX = _F("NET_DVR_PTZControlWithSpeed_EX", "cdecl", c_int, [LONG, DWORD, DWORD, DWORD], None)

NET_DVR_GetPTZCruise = _F("NET_DVR_GetPTZCruise", "cdecl", c_int, [LONG, LONG, LONG, LPNET_DVR_CRUISE_RET], None)

NET_DVR_FindFile = _F("NET_DVR_FindFile", "cdecl", LONG, [LONG, LONG, DWORD, LPNET_DVR_TIME, LPNET_DVR_TIME], None)

NET_DVR_FindNextFile = _F("NET_DVR_FindNextFile", "cdecl", LONG, [LONG, LPNET_DVR_FIND_DATA], None)

NET_DVR_FindNextFile_Card = _F("NET_DVR_FindNextFile_Card", "cdecl", LONG, [LONG, LPNET_DVR_FINDDATA_CARD], None)

NET_DVR_FindClose = _F("NET_DVR_FindClose", "cdecl", c_int, [LONG], None)

NET_DVR_FindNextFile_V30 = _F("NET_DVR_FindNextFile_V30", "cdecl", LONG, [LONG, LPNET_DVR_FINDDATA_V30], None)

NET_DVR_FindNextFile_V40 = _F("NET_DVR_FindNextFile_V40", "cdecl", LONG, [LONG, LPNET_DVR_FINDDATA_V40], None)

NET_DVR_FindNextFile_V50 = _F("NET_DVR_FindNextFile_V50", "cdecl", LONG, [LONG, LPNET_DVR_FINDDATA_V50], None)

NET_DVR_FindFile_V30 = _F("NET_DVR_FindFile_V30", "cdecl", LONG, [LONG, LPNET_DVR_FILECOND], None)

NET_DVR_FindFile_V50 = _F("NET_DVR_FindFile_V50", "cdecl", LONG, [LONG, LPNET_DVR_FILECOND_V50], None)

NET_DVR_FindClose_V30 = _F("NET_DVR_FindClose_V30", "cdecl", c_int, [LONG], None)

NET_DVR_LockFileByName = _F("NET_DVR_LockFileByName", "cdecl", c_int, [LONG, String], None)

NET_DVR_UnlockFileByName = _F("NET_DVR_UnlockFileByName", "cdecl", c_int, [LONG, String], None)

NET_DVR_LockFileByNameV40 = _F("NET_DVR_LockFileByNameV40", "cdecl", c_int, [LONG, c_int, POINTER(NET_DVR_LOCK_FILE_BY_NAME_PARA)], None)

NET_DVR_PlayBackByName = _F("NET_DVR_PlayBackByName", "cdecl", LONG, [LONG, String, HWND], None)

NET_DVR_PlayBackByName_V50 = _F("NET_DVR_PlayBackByName_V50", "cdecl", LONG, [LONG, LPNET_DVR_PLAY_BY_NAME_PARA], None)

NET_DVR_PlayBackByTime = _F("NET_DVR_PlayBackByTime", "cdecl", LONG, [LONG, LONG, LPNET_DVR_TIME, LPNET_DVR_TIME, HWND], None)

NET_DVR_PlayBackReverseByName = _F("NET_DVR_PlayBackReverseByName", "cdecl", LONG, [LONG, String, HWND], None)

NET_DVR_PlayBackReverseByName_V50 = _F("NET_DVR_PlayBackReverseByName_V50", "cdecl", LONG, [LONG, LPNET_DVR_PLAY_BY_NAME_PARA], None)

NET_DVR_PlayBackByTime_PCNVR = _F("NET_DVR_PlayBackByTime_PCNVR", "cdecl", LONG, [LONG, POINTER(NET_DVR_PLAYBCK_BYTIME_COND_PCNVR)], None)

NET_DVR_PlayBackControl = _F("NET_DVR_PlayBackControl", "cdecl", c_int, [LONG, DWORD, DWORD, POINTER(DWORD)], None)

NET_DVR_StopPlayBack = _F("NET_DVR_StopPlayBack", "cdecl", c_int, [LONG], None)

NET_DVR_SetPlayDataCallBack = _F("NET_DVR_SetPlayDataCallBack", "cdecl", c_int, [LONG, CFUNCTYPE(UNCHECKED(None), LONG, DWORD, POINTER(BYTE), DWORD, DWORD), DWORD], None)

NET_DVR_SetPlayBackESCallBack = _F("NET_DVR_SetPlayBackESCallBack", "cdecl", c_int, [LONG, CFUNCTYPE(UNCHECKED(None), LONG, POINTER(NET_DVR_PACKET_INFO_EX), POINTER(None)), POINTER(None)], None)

NET_DVR_SetPlayDataCallBack_V40 = _F("NET_DVR_SetPlayDataCallBack_V40", "cdecl", c_int, [LONG, CFUNCTYPE(UNCHECKED(None), LONG, DWORD, POINTER(BYTE), DWORD, POINTER(None)), POINTER(None)], None)

NET_DVR_PlayBackSaveData = _F("NET_DVR_PlayBackSaveData", "cdecl", c_int, [LONG, String], None)

NET_DVR_StopPlayBackSave = _F("NET_DVR_StopPlayBackSave", "cdecl", c_int, [LONG], None)

NET_DVR_GetPlayBackOsdTime = _F("NET_DVR_GetPlayBackOsdTime", "cdecl", c_int, [LONG, LPNET_DVR_TIME], None)

NET_DVR_PlayBackCaptureFile = _F("NET_DVR_PlayBackCaptureFile", "cdecl", c_int, [LONG, String], None)

NET_DVR_GetFileByName = _F("NET_DVR_GetFileByName", "cdecl", LONG, [LONG, String, String], None)

NET_DVR_GetFileByName_V50 = _F("NET_DVR_GetFileByName_V50", "cdecl", LONG, [LONG, LPNET_DVR_DOWNLOAD_BY_NAME_COND], None)

NET_DVR_GetFileByTime = _F("NET_DVR_GetFileByTime", "cdecl", LONG, [LONG, LONG, LPNET_DVR_TIME, LPNET_DVR_TIME, String], None)

NET_DVR_StopGetFile = _F("NET_DVR_StopGetFile", "cdecl", c_int, [LONG], None)

NET_DVR_GetDownloadPos = _F("NET_DVR_GetDownloadPos", "cdecl", LONG, [LONG], None)

NET_DVR_GetPlayBackPos = _F("NET_DVR_GetPlayBackPos", "cdecl", LONG, [LONG], None)

NET_DVR_AdapterUpgrade = _F("NET_DVR_AdapterUpgrade", "cdecl", LONG, [LONG, String], None)

NET_DVR_Upgrade = _F("NET_DVR_Upgrade", "cdecl", LONG, [LONG, String], None)

NET_DVR_VcalibUpgrade = _F("NET_DVR_VcalibUpgrade", "cdecl", LONG, [LONG, LONG, String], None)

NET_DVR_GetUpgradeState = _F("NET_DVR_GetUpgradeState", "cdecl", LONG, [LONG], None)

NET_DVR_GetUpgradeProgress = _F("NET_DVR_GetUpgradeProgress", "cdecl", LONG, [LONG], None)

NET_DVR_CloseUpgradeHandle = _F("NET_DVR_CloseUpgradeHandle", "cdecl", c_int, [LONG], None)

NET_DVR_SetNetworkEnvironment = _F("NET_DVR_SetNetworkEnvironment", "cdecl", c_int, [DWORD], None)

NET_DVR_FormatDisk = _F("NET_DVR_FormatDisk", "cdecl", LONG, [LONG, LONG], None)

NET_DVR_FormatDisk_V50 = _F("NET_DVR_FormatDisk_V50", "cdecl", LONG, [LONG, POINTER(NET_DVR_FORMAT_HDD)], None)

NET_DVR_GetFormatProgress = _F("NET_DVR_GetFormatProgress", "cdecl", c_int, [LONG, POINTER(LONG), POINTER(LONG), POINTER(LONG)], None)

NET_DVR_CloseFormatHandle = _F("NET_DVR_CloseFormatHandle", "cdecl", c_int, [LONG], None)

NET_DVR_SetupAlarmChan = _F("NET_DVR_SetupAlarmChan", "cdecl", LONG, [LONG], None)

NET_DVR_CloseAlarmChan = _F("NET_DVR_CloseAlarmChan", "cdecl", c_int, [LONG], None)

NET_DVR_SetupAlarmChan_V30 = _F("NET_DVR_SetupAlarmChan_V30", "cdecl", LONG, [LONG], None)

NET_DVR_CloseAlarmChan_V30 = _F("NET_DVR_CloseAlarmChan_V30", "cdecl", c_int, [LONG], None)

NET_DVR_StartVoiceCom = _F("NET_DVR_StartVoiceCom", "cdecl", LONG, [LONG, CFUNCTYPE(UNCHECKED(None), LONG, String, DWORD, BYTE, DWORD), DWORD], None)

NET_DVR_StartVoiceCom_V30 = _F("NET_DVR_StartVoiceCom_V30", "cdecl", LONG, [LONG, DWORD, c_int, CFUNCTYPE(UNCHECKED(None), LONG, String, DWORD, BYTE, POINTER(None)), POINTER(None)], None)

NET_DVR_SetVoiceComClientVolume = _F("NET_DVR_SetVoiceComClientVolume", "cdecl", c_int, [LONG, WORD], None)

NET_DVR_StopVoiceCom = _F("NET_DVR_StopVoiceCom", "cdecl", c_int, [LONG], None)

NET_DVR_StartVoiceCom_MR = _F("NET_DVR_StartVoiceCom_MR", "cdecl", LONG, [LONG, CFUNCTYPE(UNCHECKED(None), LONG, String, DWORD, BYTE, DWORD), DWORD], None)

NET_DVR_StartVoiceCom_MR_V30 = _F("NET_DVR_StartVoiceCom_MR_V30", "cdecl", LONG, [LONG, DWORD, CFUNCTYPE(UNCHECKED(None), LONG, String, DWORD, BYTE, POINTER(None)), POINTER(None)], None)

NET_DVR_VoiceComSendData = _F("NET_DVR_VoiceComSendData", "cdecl", c_int, [LONG, String, DWORD], None)

NET_DVR_GetCurrentAudioCompress = _F("NET_DVR_GetCurrentAudioCompress", "cdecl", c_int, [LONG, LPNET_DVR_COMPRESSION_AUDIO], None)

NET_DVR_GetCurrentAudioCompress_V50 = _F("NET_DVR_GetCurrentAudioCompress_V50", "cdecl", c_int, [LONG, LPNET_DVR_AUDIO_CHANNEL, LPNET_DVR_COMPRESSION_AUDIO], None)

NET_DVR_ClientAudioStart = _F("NET_DVR_ClientAudioStart", "cdecl", c_int, [], None)

NET_DVR_ClientAudioStart_V30 = _F("NET_DVR_ClientAudioStart_V30", "cdecl", c_int, [CFUNCTYPE(UNCHECKED(None), String, DWORD, POINTER(None)), POINTER(None)], None)

NET_DVR_ClientAudioStop = _F("NET_DVR_ClientAudioStop", "cdecl", c_int, [], None)

NET_DVR_AddDVR = _F("NET_DVR_AddDVR", "cdecl", c_int, [LONG], None)

NET_DVR_AddDVR_V30 = _F("NET_DVR_AddDVR_V30", "cdecl", LONG, [LONG, DWORD], None)

NET_DVR_DelDVR = _F("NET_DVR_DelDVR", "cdecl", c_int, [LONG], None)

NET_DVR_DelDVR_V30 = _F("NET_DVR_DelDVR_V30", "cdecl", c_int, [LONG], None)

NET_DVR_SerialStart = _F("NET_DVR_SerialStart", "cdecl", LONG, [LONG, LONG, CFUNCTYPE(UNCHECKED(None), LONG, String, DWORD, DWORD), DWORD], None)

NET_DVR_SerialStart_V40 = _F("NET_DVR_SerialStart_V40", "cdecl", LONG, [LONG, POINTER(None), LONG, CFUNCTYPE(UNCHECKED(None), LONG, LONG, String, DWORD, POINTER(None)), POINTER(None)], None)

NET_DVR_SerialSend = _F("NET_DVR_SerialSend", "cdecl", c_int, [LONG, LONG, String, DWORD], None)

NET_DVR_SerialStop = _F("NET_DVR_SerialStop", "cdecl", c_int, [LONG], None)

NET_DVR_SendTo232Port = _F("NET_DVR_SendTo232Port", "cdecl", c_int, [LONG, String, DWORD], None)

NET_DVR_SendToSerialPort = _F("NET_DVR_SendToSerialPort", "cdecl", c_int, [LONG, DWORD, DWORD, String, DWORD], None)

NET_DVR_InitG722Decoder = _F("NET_DVR_InitG722Decoder", "cdecl", POINTER(c_ubyte), [], lambda v,*a : cast(v, c_void_p))

NET_DVR_DecodeG722Frame = _F("NET_DVR_DecodeG722Frame", "cdecl", c_int, [POINTER(None), POINTER(NET_DVR_AUDIODEC_PROCESS_PARAM)], None)

NET_DVR_InitG722Encoder = _F("NET_DVR_InitG722Encoder", "cdecl", POINTER(c_ubyte), [POINTER(NET_DVR_AUDIOENC_INFO)], lambda v,*a : cast(v, c_void_p))

NET_DVR_EncodeG722Frame = _F("NET_DVR_EncodeG722Frame", "cdecl", c_int, [POINTER(None), POINTER(NET_DVR_AUDIOENC_PROCESS_PARAM)], None)

NET_DVR_ReleaseG722Decoder = _F("NET_DVR_ReleaseG722Decoder", "cdecl", None, [POINTER(None)], None)

NET_DVR_ReleaseG722Encoder = _F("NET_DVR_ReleaseG722Encoder", "cdecl", None, [POINTER(None)], None)

NET_DVR_InitG726Decoder = _F("NET_DVR_InitG726Decoder", "cdecl", POINTER(c_ubyte), [POINTER(POINTER(None))], lambda v,*a : cast(v, c_void_p))

NET_DVR_ReleaseG726Decoder = _F("NET_DVR_ReleaseG726Decoder", "cdecl", None, [POINTER(None)], None)

NET_DVR_DecodeG726Frame = _F("NET_DVR_DecodeG726Frame", "cdecl", c_int, [POINTER(None), POINTER(BYTE), POINTER(BYTE), BYTE], None)

NET_DVR_InitG726Encoder = _F("NET_DVR_InitG726Encoder", "cdecl", POINTER(c_ubyte), [POINTER(POINTER(None))], lambda v,*a : cast(v, c_void_p))

NET_DVR_EncodeG726Frame = _F("NET_DVR_EncodeG726Frame", "cdecl", c_int, [POINTER(None), POINTER(BYTE), POINTER(BYTE), BYTE], None)

NET_DVR_ReleaseG726Encoder = _F("NET_DVR_ReleaseG726Encoder", "cdecl", None, [POINTER(None)], None)

NET_DVR_ClickKey = _F("NET_DVR_ClickKey", "cdecl", c_int, [LONG, LONG], None)

NET_DVR_DoorBellControl = _F("NET_DVR_DoorBellControl", "cdecl", c_int, [LONG], None)

NET_DVR_Preview = _F("NET_DVR_Preview", "cdecl", c_int, [LONG, LONG], None)

NET_DVR_PreviewOne = _F("NET_DVR_PreviewOne", "cdecl", c_int, [LONG, LONG], None)

NET_DVR_PlayBackByNameLocDisplay = _F("NET_DVR_PlayBackByNameLocDisplay", "cdecl", c_int, [LONG, String], None)

NET_DVR_PlayBackByTimeLocDisplay = _F("NET_DVR_PlayBackByTimeLocDisplay", "cdecl", c_int, [LONG, LONG, POINTER(NET_DVR_TIME), POINTER(NET_DVR_TIME)], None)

NET_DVR_StopLocDisplayPlay = _F("NET_DVR_StopLocDisplayPlay", "cdecl", c_int, [LONG], None)

NET_DVR_PlayControlLocDisplay = _F("NET_DVR_PlayControlLocDisplay", "cdecl", c_int, [LONG, DWORD], None)

NET_DVR_StartDVRRecord = _F("NET_DVR_StartDVRRecord", "cdecl", c_int, [LONG, LONG, LONG], None)

NET_DVR_StopDVRRecord = _F("NET_DVR_StopDVRRecord", "cdecl", c_int, [LONG, LONG], None)

NET_DVR_InitDevice_Card = _F("NET_DVR_InitDevice_Card", "cdecl", c_int, [POINTER(c_long)], None)

NET_DVR_ReleaseDevice_Card = _F("NET_DVR_ReleaseDevice_Card", "cdecl", c_int, [], None)

NET_DVR_InitDDraw_Card = _F("NET_DVR_InitDDraw_Card", "cdecl", c_int, [HWND, COLORREF], None)

NET_DVR_ReleaseDDraw_Card = _F("NET_DVR_ReleaseDDraw_Card", "cdecl", c_int, [], None)

NET_DVR_RealPlay_Card_V30 = _F("NET_DVR_RealPlay_Card_V30", "cdecl", LONG, [LONG, POINTER(NET_DVR_CARDINFO), LONG, DWORD, c_int, REALDATACALLBACK, POINTER(None)], None)

NET_DVR_RealPlay_Card = _F("NET_DVR_RealPlay_Card", "cdecl", LONG, [LONG, LPNET_DVR_CARDINFO, c_long], None)

NET_DVR_ResetPara_Card = _F("NET_DVR_ResetPara_Card", "cdecl", c_int, [LONG, LPNET_DVR_DISPLAY_PARA], None)

NET_DVR_RefreshSurface_Card = _F("NET_DVR_RefreshSurface_Card", "cdecl", c_int, [], None)

NET_DVR_ClearSurface_Card = _F("NET_DVR_ClearSurface_Card", "cdecl", c_int, [], None)

NET_DVR_RestoreSurface_Card = _F("NET_DVR_RestoreSurface_Card", "cdecl", c_int, [], None)

NET_DVR_OpenSound_Card = _F("NET_DVR_OpenSound_Card", "cdecl", c_int, [LONG], None)

NET_DVR_CloseSound_Card = _F("NET_DVR_CloseSound_Card", "cdecl", c_int, [LONG], None)

NET_DVR_SetVolume_Card = _F("NET_DVR_SetVolume_Card", "cdecl", c_int, [LONG, WORD], None)

NET_DVR_AudioPreview_Card = _F("NET_DVR_AudioPreview_Card", "cdecl", c_int, [LONG, c_int], None)

NET_DVR_GetCardLastError_Card = _F("NET_DVR_GetCardLastError_Card", "cdecl", LONG, [], None)

NET_DVR_SetDspErrMsg_Card = _F("NET_DVR_SetDspErrMsg_Card", "cdecl", c_int, [DWORD, HANDLE], None)

NET_DVR_ResetDSP_Card = _F("NET_DVR_ResetDSP_Card", "cdecl", c_int, [LONG], None)

NET_DVR_GetChanHandle_Card = _F("NET_DVR_GetChanHandle_Card", "cdecl", HANDLE, [LONG], None)

NET_DVR_CapturePicture_Card = _F("NET_DVR_CapturePicture_Card", "cdecl", c_int, [LONG, String], None)

NET_DVR_GetSerialNum_Card = _F("NET_DVR_GetSerialNum_Card", "cdecl", c_int, [c_long, POINTER(DWORD)], None)

NET_DVR_FindDVRLog = _F("NET_DVR_FindDVRLog", "cdecl", LONG, [LONG, LONG, DWORD, DWORD, LPNET_DVR_TIME, LPNET_DVR_TIME], None)

NET_DVR_FindNextLog = _F("NET_DVR_FindNextLog", "cdecl", LONG, [LONG, LPNET_DVR_LOG], None)

NET_DVR_FindLogClose = _F("NET_DVR_FindLogClose", "cdecl", c_int, [LONG], None)

NET_DVR_FindDVRLog_V30 = _F("NET_DVR_FindDVRLog_V30", "cdecl", LONG, [LONG, LONG, DWORD, DWORD, LPNET_DVR_TIME, LPNET_DVR_TIME, c_int], None)

NET_DVR_FindNextLog_V30 = _F("NET_DVR_FindNextLog_V30", "cdecl", LONG, [LONG, LPNET_DVR_LOG_V30], None)

NET_DVR_FindDVRLog_V50 = _F("NET_DVR_FindDVRLog_V50", "cdecl", LONG, [LONG, LPNET_DVR_FIND_LOG_COND], None)

NET_DVR_FindNextLog_V50 = _F("NET_DVR_FindNextLog_V50", "cdecl", LONG, [LONG, LPNET_DVR_LOG_V50], None)

NET_DVR_FindLogClose_V30 = _F("NET_DVR_FindLogClose_V30", "cdecl", c_int, [LONG], None)

NET_DVR_FindFile_PCNVR = _F("NET_DVR_FindFile_PCNVR", "cdecl", LONG, [LONG, LPNET_DVR_FILE_COND_PCNVR], None)

NET_DVR_FindNextFile_PCNVR = _F("NET_DVR_FindNextFile_PCNVR", "cdecl", LONG, [LONG, LPNET_DVR_FINDDATA_PCNVR], None)

NET_DVR_FindClose_PCNVR = _F("NET_DVR_FindClose_PCNVR", "cdecl", c_int, [LONG], None)

NET_DVR_FindAlarmHostLog = _F("NET_DVR_FindAlarmHostLog", "cdecl", LONG, [LONG, LONG, POINTER(NET_DVR_ALARMHOST_SEARCH_LOG_PARAM)], None)

NET_DVR_FindNextAlarmHostLog = _F("NET_DVR_FindNextAlarmHostLog", "cdecl", LONG, [LONG, POINTER(NET_DVR_ALARMHOST_LOG_RET)], None)

NET_DVR_FindAlarmHostLogClose = _F("NET_DVR_FindAlarmHostLogClose", "cdecl", c_int, [LONG], None)

NET_DVR_FindFileByCard = _F("NET_DVR_FindFileByCard", "cdecl", LONG, [LONG, LONG, DWORD, c_int, POINTER(BYTE), LPNET_DVR_TIME, LPNET_DVR_TIME], None)

NET_DVR_CaptureJPEGPicture = _F("NET_DVR_CaptureJPEGPicture", "cdecl", c_int, [LONG, LONG, LPNET_DVR_JPEGPARA, String], None)

NET_DVR_CaptureJPEGPicture_NEW = _F("NET_DVR_CaptureJPEGPicture_NEW", "cdecl", c_int, [LONG, LONG, LPNET_DVR_JPEGPARA, String, DWORD, LPDWORD], None)

NET_DVR_CapturePicture_V50 = _F("NET_DVR_CapturePicture_V50", "cdecl", c_int, [LONG, LONG, LPNET_DVR_PICPARAM_V50, String, DWORD, LPDWORD], None)

NET_DVR_CaptureJPEGPicture_WithAppendData = _F("NET_DVR_CaptureJPEGPicture_WithAppendData", "cdecl", c_int, [LONG, LONG, POINTER(NET_DVR_JPEGPICTURE_WITH_APPENDDATA)], None)

NET_DVR_GetRealPlayOsdTime = _F("NET_DVR_GetRealPlayOsdTime", "cdecl", c_int, [LONG, LPNET_DVR_TIME], None)

NET_DVR_RealPlayPause = _F("NET_DVR_RealPlayPause", "cdecl", c_int, [LONG], None)

NET_DVR_RealPlayRestart = _F("NET_DVR_RealPlayRestart", "cdecl", c_int, [LONG, HWND], None)

NET_DVR_GetRealPlayerIndex = _F("NET_DVR_GetRealPlayerIndex", "cdecl", LONG, [LONG], None)

NET_DVR_GetPlayBackPlayerIndex = _F("NET_DVR_GetPlayBackPlayerIndex", "cdecl", LONG, [LONG], None)

NET_DVR_SetScaleCFG = _F("NET_DVR_SetScaleCFG", "cdecl", c_int, [LONG, DWORD], None)

NET_DVR_GetScaleCFG = _F("NET_DVR_GetScaleCFG", "cdecl", c_int, [LONG, POINTER(DWORD)], None)

NET_DVR_SetScaleCFG_V30 = _F("NET_DVR_SetScaleCFG_V30", "cdecl", c_int, [LONG, LPNET_DVR_SCALECFG], None)

NET_DVR_GetScaleCFG_V30 = _F("NET_DVR_GetScaleCFG_V30", "cdecl", c_int, [LONG, LPNET_DVR_SCALECFG], None)

NET_DVR_SetATMPortCFG = _F("NET_DVR_SetATMPortCFG", "cdecl", c_int, [LONG, WORD], None)

NET_DVR_GetATMPortCFG = _F("NET_DVR_GetATMPortCFG", "cdecl", c_int, [LONG, POINTER(WORD)], None)

NET_DVR_InitDDrawDevice = _F("NET_DVR_InitDDrawDevice", "cdecl", c_int, [], None)

NET_DVR_ReleaseDDrawDevice = _F("NET_DVR_ReleaseDDrawDevice", "cdecl", c_int, [], None)

NET_DVR_GetDDrawDeviceTotalNums = _F("NET_DVR_GetDDrawDeviceTotalNums", "cdecl", LONG, [], None)

NET_DVR_SetDDrawDevice = _F("NET_DVR_SetDDrawDevice", "cdecl", c_int, [LONG, DWORD], None)

NET_DVR_PTZSelZoomIn = _F("NET_DVR_PTZSelZoomIn", "cdecl", c_int, [LONG, LPNET_DVR_POINT_FRAME], None)

NET_DVR_PTZSelZoomIn_EX = _F("NET_DVR_PTZSelZoomIn_EX", "cdecl", c_int, [LONG, LONG, LPNET_DVR_POINT_FRAME], None)

NET_DVR_StartDecode = _F("NET_DVR_StartDecode", "cdecl", c_int, [LONG, LONG, LPNET_DVR_DECODERINFO], None)

NET_DVR_StopDecode = _F("NET_DVR_StopDecode", "cdecl", c_int, [LONG, LONG], None)

NET_DVR_GetDecoderState = _F("NET_DVR_GetDecoderState", "cdecl", c_int, [LONG, LONG, LPNET_DVR_DECODERSTATE], None)

NET_DVR_SetDecInfo = _F("NET_DVR_SetDecInfo", "cdecl", c_int, [LONG, LONG, LPNET_DVR_DECCFG], None)

NET_DVR_GetDecInfo = _F("NET_DVR_GetDecInfo", "cdecl", c_int, [LONG, LONG, LPNET_DVR_DECCFG], None)

NET_DVR_SetDecTransPort = _F("NET_DVR_SetDecTransPort", "cdecl", c_int, [LONG, LPNET_DVR_PORTCFG], None)

NET_DVR_GetDecTransPort = _F("NET_DVR_GetDecTransPort", "cdecl", c_int, [LONG, LPNET_DVR_PORTCFG], None)

NET_DVR_DecPlayBackCtrl = _F("NET_DVR_DecPlayBackCtrl", "cdecl", c_int, [LONG, LONG, DWORD, DWORD, POINTER(DWORD), LPNET_DVR_PLAYREMOTEFILE], None)

NET_DVR_StartDecSpecialCon = _F("NET_DVR_StartDecSpecialCon", "cdecl", c_int, [LONG, LONG, LPNET_DVR_DECCHANINFO], None)

NET_DVR_StopDecSpecialCon = _F("NET_DVR_StopDecSpecialCon", "cdecl", c_int, [LONG, LONG, LPNET_DVR_DECCHANINFO], None)

NET_DVR_DecCtrlDec = _F("NET_DVR_DecCtrlDec", "cdecl", c_int, [LONG, LONG, DWORD], None)

NET_DVR_DecCtrlScreen = _F("NET_DVR_DecCtrlScreen", "cdecl", c_int, [LONG, LONG, DWORD], None)

NET_DVR_GetDecCurLinkStatus = _F("NET_DVR_GetDecCurLinkStatus", "cdecl", c_int, [LONG, LONG, LPNET_DVR_DECSTATUS], None)

NET_DVR_MatrixStartDynamic = _F("NET_DVR_MatrixStartDynamic", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_MATRIX_DYNAMIC_DEC], None)

NET_DVR_MatrixStopDynamic = _F("NET_DVR_MatrixStopDynamic", "cdecl", c_int, [LONG, DWORD], None)

NET_DVR_MatrixGetDecChanInfo = _F("NET_DVR_MatrixGetDecChanInfo", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_MATRIX_DEC_CHAN_INFO], None)

NET_DVR_MatrixSetLoopDecChanInfo = _F("NET_DVR_MatrixSetLoopDecChanInfo", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_MATRIX_LOOP_DECINFO], None)

NET_DVR_MatrixGetLoopDecChanInfo = _F("NET_DVR_MatrixGetLoopDecChanInfo", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_MATRIX_LOOP_DECINFO], None)

NET_DVR_MatrixSetLoopDecChanEnable = _F("NET_DVR_MatrixSetLoopDecChanEnable", "cdecl", c_int, [LONG, DWORD, DWORD], None)

NET_DVR_MatrixGetLoopDecChanEnable = _F("NET_DVR_MatrixGetLoopDecChanEnable", "cdecl", c_int, [LONG, DWORD, LPDWORD], None)

NET_DVR_MatrixGetLoopDecEnable = _F("NET_DVR_MatrixGetLoopDecEnable", "cdecl", c_int, [LONG, LPDWORD], None)

NET_DVR_MatrixSetDecChanEnable = _F("NET_DVR_MatrixSetDecChanEnable", "cdecl", c_int, [LONG, DWORD, DWORD], None)

NET_DVR_MatrixGetDecChanEnable = _F("NET_DVR_MatrixGetDecChanEnable", "cdecl", c_int, [LONG, DWORD, LPDWORD], None)

NET_DVR_MatrixGetDecChanStatus = _F("NET_DVR_MatrixGetDecChanStatus", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_MATRIX_DEC_CHAN_STATUS], None)

NET_DVR_MatrixGetVideoStandard = _F("NET_DVR_MatrixGetVideoStandard", "cdecl", c_int, [LONG, DWORD, LPDWORD], None)

NET_DVR_MatrixSetVideoStandard = _F("NET_DVR_MatrixSetVideoStandard", "cdecl", c_int, [LONG, DWORD, DWORD], None)

NET_DVR_MatrixSetTranInfo = _F("NET_DVR_MatrixSetTranInfo", "cdecl", c_int, [LONG, LPNET_DVR_MATRIX_TRAN_CHAN_CONFIG], None)

NET_DVR_MatrixGetTranInfo = _F("NET_DVR_MatrixGetTranInfo", "cdecl", c_int, [LONG, LPNET_DVR_MATRIX_TRAN_CHAN_CONFIG], None)

NET_DVR_MatrixSetRemotePlay = _F("NET_DVR_MatrixSetRemotePlay", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_MATRIX_DEC_REMOTE_PLAY], None)

NET_DVR_MatrixSetRemotePlayControl = _F("NET_DVR_MatrixSetRemotePlayControl", "cdecl", c_int, [LONG, DWORD, DWORD, DWORD, POINTER(DWORD)], None)

NET_DVR_MatrixGetRemotePlayStatus = _F("NET_DVR_MatrixGetRemotePlayStatus", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_MATRIX_DEC_REMOTE_PLAY_STATUS], None)

NET_DVR_MatrixStartDynamic_V30 = _F("NET_DVR_MatrixStartDynamic_V30", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_PU_STREAM_CFG], None)

NET_DVR_MatrixSetLoopDecChanInfo_V30 = _F("NET_DVR_MatrixSetLoopDecChanInfo_V30", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_MATRIX_LOOP_DECINFO_V30], None)

NET_DVR_MatrixGetLoopDecChanInfo_V30 = _F("NET_DVR_MatrixGetLoopDecChanInfo_V30", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_MATRIX_LOOP_DECINFO_V30], None)

NET_DVR_MatrixGetDecChanInfo_V30 = _F("NET_DVR_MatrixGetDecChanInfo_V30", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_MATRIX_DEC_CHAN_INFO_V30], None)

NET_DVR_MatrixSetTranInfo_V30 = _F("NET_DVR_MatrixSetTranInfo_V30", "cdecl", c_int, [LONG, LPNET_DVR_MATRIX_TRAN_CHAN_CONFIG_V30], None)

NET_DVR_MatrixGetTranInfo_V30 = _F("NET_DVR_MatrixGetTranInfo_V30", "cdecl", c_int, [LONG, LPNET_DVR_MATRIX_TRAN_CHAN_CONFIG_V30], None)

NET_DVR_MatrixGetDisplayCfg = _F("NET_DVR_MatrixGetDisplayCfg", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_VGA_DISP_CHAN_CFG], None)

NET_DVR_MatrixSetDisplayCfg = _F("NET_DVR_MatrixSetDisplayCfg", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_VGA_DISP_CHAN_CFG], None)

NET_DVR_MatrixStartPassiveDecode = _F("NET_DVR_MatrixStartPassiveDecode", "cdecl", LONG, [LONG, DWORD, LPNET_DVR_MATRIX_PASSIVEMODE], None)

NET_DVR_MatrixSendData = _F("NET_DVR_MatrixSendData", "cdecl", c_int, [LONG, String, DWORD], None)

NET_DVR_MatrixStopPassiveDecode = _F("NET_DVR_MatrixStopPassiveDecode", "cdecl", c_int, [LONG], None)

NET_DVR_UploadLogo = _F("NET_DVR_UploadLogo", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_DISP_LOGOCFG, String], None)

NET_DVR_UploadLogo_NEW = _F("NET_DVR_UploadLogo_NEW", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_MATRIX_LOGO_INFO, String], None)

NET_DVR_DownloadLogo = _F("NET_DVR_DownloadLogo", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_MATRIX_LOGO_INFO, String, DWORD], None)

NET_DVR_LogoSwitch = _F("NET_DVR_LogoSwitch", "cdecl", c_int, [LONG, DWORD, DWORD], None)

NET_DVR_MatrixGetDeviceStatus = _F("NET_DVR_MatrixGetDeviceStatus", "cdecl", c_int, [LONG, LPNET_DVR_DECODER_WORK_STATUS], None)

NET_DVR_MatrixDiaplayControl = _F("NET_DVR_MatrixDiaplayControl", "cdecl", c_int, [LONG, DWORD, DWORD, DWORD], None)

NET_DVR_MatrixPassiveDecodeControl = _F("NET_DVR_MatrixPassiveDecodeControl", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_PASSIVEDECODE_CONTROL], None)

NET_DVR_MatrixGetPassiveDecodeStatus = _F("NET_DVR_MatrixGetPassiveDecodeStatus", "cdecl", LONG, [LONG], None)

NET_DVR_MatrixGetDecChanCfg = _F("NET_DVR_MatrixGetDecChanCfg", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_MATRIX_DECCHAN_CONTROL], None)

NET_DVR_MatrixSetDecChanCfg = _F("NET_DVR_MatrixSetDecChanCfg", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_MATRIX_DECCHAN_CONTROL], None)

NET_DVR_PlayBackByTime_NEW = _F("NET_DVR_PlayBackByTime_NEW", "cdecl", LONG, [LONG, LONG, POINTER(NET_DVR_TIME), POINTER(NET_DVR_TIME), LONG, LONG, HWND], None)

NET_DVR_RefreshPlay = _F("NET_DVR_RefreshPlay", "cdecl", c_int, [LONG], None)

NET_DVR_RestoreConfig = _F("NET_DVR_RestoreConfig", "cdecl", c_int, [LONG], None)

NET_DVR_SaveConfig = _F("NET_DVR_SaveConfig", "cdecl", c_int, [LONG], None)

NET_DVR_RebootDVR = _F("NET_DVR_RebootDVR", "cdecl", c_int, [LONG], None)

NET_DVR_ShutDownDVR = _F("NET_DVR_ShutDownDVR", "cdecl", c_int, [LONG], None)

NET_DVR_GetDVRConfig = _F("NET_DVR_GetDVRConfig", "cdecl", c_int, [LONG, DWORD, LONG, LPVOID, DWORD, LPDWORD], None)

NET_DVR_SetDVRConfig = _F("NET_DVR_SetDVRConfig", "cdecl", c_int, [LONG, DWORD, LONG, LPVOID, DWORD], None)

NET_DVR_GetDVRWorkState_V30 = _F("NET_DVR_GetDVRWorkState_V30", "cdecl", c_int, [LONG, LPNET_DVR_WORKSTATE_V30], None)

NET_DVR_GetDVRWorkState = _F("NET_DVR_GetDVRWorkState", "cdecl", c_int, [LONG, LPNET_DVR_WORKSTATE], None)

NET_DVR_SetVideoEffect = _F("NET_DVR_SetVideoEffect", "cdecl", c_int, [LONG, LONG, DWORD, DWORD, DWORD, DWORD], None)

NET_DVR_GetVideoEffect = _F("NET_DVR_GetVideoEffect", "cdecl", c_int, [LONG, LONG, POINTER(DWORD), POINTER(DWORD), POINTER(DWORD), POINTER(DWORD)], None)

NET_DVR_ClientGetframeformat = _F("NET_DVR_ClientGetframeformat", "cdecl", c_int, [LONG, LPNET_DVR_FRAMEFORMAT], None)

NET_DVR_ClientSetframeformat = _F("NET_DVR_ClientSetframeformat", "cdecl", c_int, [LONG, LPNET_DVR_FRAMEFORMAT], None)

NET_DVR_ClientGetframeformat_V30 = _F("NET_DVR_ClientGetframeformat_V30", "cdecl", c_int, [LONG, LPNET_DVR_FRAMEFORMAT_V30], None)

NET_DVR_ClientSetframeformat_V30 = _F("NET_DVR_ClientSetframeformat_V30", "cdecl", c_int, [LONG, LPNET_DVR_FRAMEFORMAT_V30], None)

NET_DVR_GetAtmFrameFormat_V30 = _F("NET_DVR_GetAtmFrameFormat_V30", "cdecl", c_int, [LONG, LONG, LPNET_DVR_ATM_FRAMEFORMAT_V30], None)

NET_DVR_SetAtmFrameFormat_V30 = _F("NET_DVR_SetAtmFrameFormat_V30", "cdecl", c_int, [LONG, LONG, LPNET_DVR_ATM_FRAMEFORMAT_V30], None)

NET_DVR_GetAtmProtocol = _F("NET_DVR_GetAtmProtocol", "cdecl", c_int, [LONG, LPNET_DVR_ATM_PROTOCOL], None)

NET_DVR_GetAlarmOut_V30 = _F("NET_DVR_GetAlarmOut_V30", "cdecl", c_int, [LONG, LPNET_DVR_ALARMOUTSTATUS_V30], None)

NET_DVR_GetAlarmOut = _F("NET_DVR_GetAlarmOut", "cdecl", c_int, [LONG, LPNET_DVR_ALARMOUTSTATUS], None)

NET_DVR_SetAlarmOut = _F("NET_DVR_SetAlarmOut", "cdecl", c_int, [LONG, LONG, LONG], None)

NET_DVR_ClientSetVideoEffect = _F("NET_DVR_ClientSetVideoEffect", "cdecl", c_int, [LONG, DWORD, DWORD, DWORD, DWORD], None)

NET_DVR_ClientGetVideoEffect = _F("NET_DVR_ClientGetVideoEffect", "cdecl", c_int, [LONG, POINTER(DWORD), POINTER(DWORD), POINTER(DWORD), POINTER(DWORD)], None)

NET_DVR_GetConfigFile = _F("NET_DVR_GetConfigFile", "cdecl", c_int, [LONG, String], None)

NET_DVR_SetConfigFile = _F("NET_DVR_SetConfigFile", "cdecl", c_int, [LONG, String], None)

NET_DVR_GetConfigFile_V30 = _F("NET_DVR_GetConfigFile_V30", "cdecl", c_int, [LONG, String, DWORD, POINTER(DWORD)], None)

NET_DVR_GetConfigFile_EX = _F("NET_DVR_GetConfigFile_EX", "cdecl", c_int, [LONG, String, DWORD], None)

NET_DVR_SetConfigFile_EX = _F("NET_DVR_SetConfigFile_EX", "cdecl", c_int, [LONG, String, DWORD], None)

NET_DVR_SetLogToFile = _F("NET_DVR_SetLogToFile", "cdecl", c_int, [DWORD, String, c_int], None)

NET_DVR_GetSDKState = _F("NET_DVR_GetSDKState", "cdecl", c_int, [LPNET_DVR_SDKSTATE], None)

NET_DVR_GetSDKAbility = _F("NET_DVR_GetSDKAbility", "cdecl", c_int, [LPNET_DVR_SDKABL], None)

NET_DVR_GetPTZProtocol = _F("NET_DVR_GetPTZProtocol", "cdecl", c_int, [LONG, POINTER(NET_DVR_PTZCFG)], None)

NET_DVR_GetPTZCtrl_Other = _F("NET_DVR_GetPTZCtrl_Other", "cdecl", c_int, [LONG, LONG], None)

NET_DVR_GetPTZCtrl = _F("NET_DVR_GetPTZCtrl", "cdecl", c_int, [LONG], None)

NET_DVR_LockPanel = _F("NET_DVR_LockPanel", "cdecl", c_int, [LONG], None)

NET_DVR_UnLockPanel = _F("NET_DVR_UnLockPanel", "cdecl", c_int, [LONG], None)

NET_DVR_StartPanelKey = _F("NET_DVR_StartPanelKey", "cdecl", c_int, [LONG], None)

NET_DVR_StopPanelKey = _F("NET_DVR_StopPanelKey", "cdecl", c_int, [LONG], None)

NET_DVR_SetRtspConfig = _F("NET_DVR_SetRtspConfig", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_RTSPCFG, DWORD], None)

NET_DVR_GetRtspConfig = _F("NET_DVR_GetRtspConfig", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_RTSPCFG, DWORD], None)

NET_DVR_GetDeviceAbility = _F("NET_DVR_GetDeviceAbility", "cdecl", c_int, [LONG, DWORD, String, DWORD, String, DWORD], None)

NET_DVR_SetSimAbilityPath = _F("NET_DVR_SetSimAbilityPath", "cdecl", c_int, [String, String], None)

NET_DVR_MatrixGetSubSystemInfo = _F("NET_DVR_MatrixGetSubSystemInfo", "cdecl", c_int, [LONG, LPNET_DVR_ALLSUBSYSTEMINFO], None)

NET_DVR_MatrixSetSubSystemInfo = _F("NET_DVR_MatrixSetSubSystemInfo", "cdecl", c_int, [LONG, LPNET_DVR_ALLSUBSYSTEMINFO], None)

NET_DVR_MatrixGetCodeSplitter = _F("NET_DVR_MatrixGetCodeSplitter", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_CODESPLITTERINFO], None)

NET_DVR_MatrixSetCodeSplitter = _F("NET_DVR_MatrixSetCodeSplitter", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_CODESPLITTERINFO], None)

NET_DVR_SetBehaviorParamKey = _F("NET_DVR_SetBehaviorParamKey", "cdecl", c_int, [LONG, LONG, DWORD, c_int], None)

NET_DVR_GetBehaviorParamKey = _F("NET_DVR_GetBehaviorParamKey", "cdecl", c_int, [LONG, LONG, DWORD, POINTER(c_int)], None)

NET_DVR_GetVCADrawMode = _F("NET_DVR_GetVCADrawMode", "cdecl", c_int, [LONG, LONG, LPNET_VCA_DRAW_MODE], None)

NET_DVR_SetVCADrawMode = _F("NET_DVR_SetVCADrawMode", "cdecl", c_int, [LONG, LONG, LPNET_VCA_DRAW_MODE], None)

NET_DVR_SetTrackMode = _F("NET_DVR_SetTrackMode", "cdecl", c_int, [LONG, LONG, LPNET_DVR_TRACK_MODE], None)

NET_DVR_GetTrackMode = _F("NET_DVR_GetTrackMode", "cdecl", c_int, [LONG, LONG, LPNET_DVR_TRACK_MODE], None)

NET_VCA_RestartLib = _F("NET_VCA_RestartLib", "cdecl", c_int, [LONG, LONG], None)

NET_DVR_SaveRealData_V30 = _F("NET_DVR_SaveRealData_V30", "cdecl", c_int, [LONG, DWORD, String], None)

NET_DVR_EncodeG711Frame = _F("NET_DVR_EncodeG711Frame", "cdecl", c_int, [LPVOID, POINTER(NET_DVR_AUDIOENC_PROCESS_PARAM)], None)

NET_DVR_DecodeG711Frame = _F("NET_DVR_DecodeG711Frame", "cdecl", c_int, [LPVOID, POINTER(NET_DVR_AUDIODEC_PROCESS_PARAM)], None)

NET_DVR_InitG711Decoder = _F("NET_DVR_InitG711Decoder", "cdecl", LPVOID, [], None)

NET_DVR_InitG711Encoder = _F("NET_DVR_InitG711Encoder", "cdecl", LPVOID, [POINTER(NET_DVR_AUDIOENC_INFO)], None)

NET_DVR_ReleaseG711Encoder = _F("NET_DVR_ReleaseG711Encoder", "cdecl", c_int, [LPVOID], None)

NET_DVR_ReleaseG711Decoder = _F("NET_DVR_ReleaseG711Decoder", "cdecl", c_int, [LPVOID], None)

NET_DVR_FindFileByEvent = _F("NET_DVR_FindFileByEvent", "cdecl", LONG, [LONG, LPNET_DVR_SEARCH_EVENT_PARAM], None)

NET_DVR_FindFileByEvent_V40 = _F("NET_DVR_FindFileByEvent_V40", "cdecl", LONG, [LONG, LPNET_DVR_SEARCH_EVENT_PARAM_V40], None)

NET_DVR_FindFileByEvent_V50 = _F("NET_DVR_FindFileByEvent_V50", "cdecl", LONG, [LONG, LPNET_DVR_SEARCH_EVENT_PARAM_V50], None)

NET_DVR_FindNextEvent = _F("NET_DVR_FindNextEvent", "cdecl", LONG, [LONG, LPNET_DVR_SEARCH_EVENT_RET], None)

NET_DVR_FindNextEvent_V40 = _F("NET_DVR_FindNextEvent_V40", "cdecl", LONG, [LONG, LPNET_DVR_SEARCH_EVENT_RET_V40], None)

NET_DVR_FindNextEvent_V50 = _F("NET_DVR_FindNextEvent_V50", "cdecl", LONG, [LONG, LPNET_DVR_SEARCH_EVENT_RET_V50], None)

NET_DVR_FindPDCInfo = _F("NET_DVR_FindPDCInfo", "cdecl", LONG, [LONG, LONG, LPNET_DVR_TIME, LPNET_DVR_TIME], None)

NET_DVR_FindNextPDCInfo = _F("NET_DVR_FindNextPDCInfo", "cdecl", LONG, [LONG, LPNET_DVR_PDC_QUERY], None)

NET_DVR_FindPDCClose = _F("NET_DVR_FindPDCClose", "cdecl", c_int, [LONG], None)

NET_DVR_VerifyCalibration = _F("NET_DVR_VerifyCalibration", "cdecl", c_int, [LONG, DWORD, LONG, LPVOID, DWORD, LPVOID, DWORD], None)

NET_DVR_ResetCounter = _F("NET_DVR_ResetCounter", "cdecl", c_int, [LONG, LONG], None)

NET_DVR_GetPtzPosition = _F("NET_DVR_GetPtzPosition", "cdecl", c_int, [LONG, LONG, LONG, LPNET_DVR_PTZ_POSITION], None)

NET_DVR_SetPtzPosition = _F("NET_DVR_SetPtzPosition", "cdecl", c_int, [LONG, LONG, LONG, LPNET_DVR_PTZ_POSITION], None)

NET_DVR_SetPatrolTrack = _F("NET_DVR_SetPatrolTrack", "cdecl", c_int, [LONG, LONG, LONG, LPNET_DVR_PATROL_TRACKCFG], None)

NET_DVR_GetPatrolTrack = _F("NET_DVR_GetPatrolTrack", "cdecl", c_int, [LONG, LONG, LONG, LPNET_DVR_PATROL_TRACKCFG], None)

NET_DVR_FindNextLog_MATRIX = _F("NET_DVR_FindNextLog_MATRIX", "cdecl", LONG, [LONG, LPNET_DVR_LOG_MATRIX], None)

NET_DVR_FindDVRLog_Matrix = _F("NET_DVR_FindDVRLog_Matrix", "cdecl", LONG, [LONG, LONG, DWORD, DWORD, LPNET_DVR_VEDIOPLATLOG, LPNET_DVR_TIME, LPNET_DVR_TIME], None)

NET_DVR_ManualSnap = _F("NET_DVR_ManualSnap", "cdecl", c_int, [LONG, POINTER(NET_DVR_MANUALSNAP), LPNET_DVR_PLATE_RESULT], None)

NET_DVR_ContinuousShoot = _F("NET_DVR_ContinuousShoot", "cdecl", c_int, [LONG, LPNET_DVR_SNAPCFG], None)

NET_DVR_GetPTZProtocol_Ex = _F("NET_DVR_GetPTZProtocol_Ex", "cdecl", c_int, [LONG, LONG, POINTER(NET_DVR_PTZCFG)], None)

NET_DVR_StartEmailTest = _F("NET_DVR_StartEmailTest", "cdecl", LONG, [LONG], None)

NET_DVR_StopEmailTest = _F("NET_DVR_StopEmailTest", "cdecl", c_int, [LONG], None)

NET_DVR_GetEmailTestProgress = _F("NET_DVR_GetEmailTestProgress", "cdecl", c_int, [LONG, POINTER(DWORD)], None)

NET_DVR_GetIPCProtoList = _F("NET_DVR_GetIPCProtoList", "cdecl", c_int, [LONG, LPNET_DVR_IPC_PROTO_LIST], None)

NET_DVR_GetIPCProtoList_V41 = _F("NET_DVR_GetIPCProtoList_V41", "cdecl", c_int, [LONG, LPNET_DVR_IPC_PROTO_LIST_V41], None)

NET_DVR_SmartSearch = _F("NET_DVR_SmartSearch", "cdecl", LONG, [LONG, LPNET_DVR_SMART_SEARCH_PARAM], None)

NET_DVR_SmartSearch_V40 = _F("NET_DVR_SmartSearch_V40", "cdecl", LONG, [LONG, LPNET_DVR_SMART_SEARCH_PARAM_V40], None)

NET_DVR_SearchNextInfo = _F("NET_DVR_SearchNextInfo", "cdecl", LONG, [LONG, LPNET_DVR_SMART_SEARCH_RET], None)

NET_DVR_StopSearch = _F("NET_DVR_StopSearch", "cdecl", c_int, [LONG], None)

NET_DVR_FindIpSanDirectory = _F("NET_DVR_FindIpSanDirectory", "cdecl", LONG, [LONG, LPNET_DVR_IPSAN_SERACH_PARAM], None)

NET_DVR_FindNextDirectory = _F("NET_DVR_FindNextDirectory", "cdecl", LONG, [LONG, LPNET_DVR_IPSAN_SERACH_RET], None)

NET_DVR_FindDirectoryClose = _F("NET_DVR_FindDirectoryClose", "cdecl", c_int, [LONG], None)

NET_DVR_ZeroStartPlay = _F("NET_DVR_ZeroStartPlay", "cdecl", LONG, [LONG, LPNET_DVR_CLIENTINFO, REALDATACALLBACK, POINTER(None), c_int], None)

NET_DVR_ZeroStopPlay = _F("NET_DVR_ZeroStopPlay", "cdecl", c_int, [LONG], None)

NET_DVR_ZeroMakeKeyFrame = _F("NET_DVR_ZeroMakeKeyFrame", "cdecl", c_int, [LONG, LONG], None)

NET_DVR_PlayBackControl_V40 = _F("NET_DVR_PlayBackControl_V40", "cdecl", c_int, [LONG, DWORD, LPVOID, DWORD, LPVOID, POINTER(DWORD)], None)

NET_DVR_ZeroTurnOver = _F("NET_DVR_ZeroTurnOver", "cdecl", c_int, [LONG, LONG, c_int], None)

NET_DVR_GetDiskList = _F("NET_DVR_GetDiskList", "cdecl", c_int, [LONG, LPNET_DVR_DISKABILITY_LIST], None)

NET_DVR_Backup = _F("NET_DVR_Backup", "cdecl", LONG, [LONG, DWORD, LPVOID, DWORD], None)

NET_DVR_BackupByName = _F("NET_DVR_BackupByName", "cdecl", LONG, [LONG, LPNET_DVR_BACKUP_NAME_PARAM], None)

NET_DVR_BackupByTime = _F("NET_DVR_BackupByTime", "cdecl", LONG, [LONG, LPNET_DVR_BACKUP_TIME_PARAM], None)

NET_DVR_GetBackupProgress = _F("NET_DVR_GetBackupProgress", "cdecl", c_int, [LONG, POINTER(DWORD)], None)

NET_DVR_StopBackup = _F("NET_DVR_StopBackup", "cdecl", c_int, [LONG], None)

NET_DVR_GetSadpInfoList = _F("NET_DVR_GetSadpInfoList", "cdecl", c_int, [LONG, LPNET_DVR_SADPINFO_LIST], None)

NET_DVR_UpdateSadpInfo = _F("NET_DVR_UpdateSadpInfo", "cdecl", c_int, [LONG, LPNET_DVR_SADP_VERIFY, LPNET_DVR_SADPINFO], None)

NET_DVR_MatrixGetSubDecSystemJoinInfo = _F("NET_DVR_MatrixGetSubDecSystemJoinInfo", "cdecl", c_int, [LONG, LPNET_DVR_ALLDECSUBSYSTEMJOININFO], None)

NET_DVR_SetCodeSplitterAssociate = _F("NET_DVR_SetCodeSplitterAssociate", "cdecl", c_int, [LONG, DWORD, DWORD, LPNET_DVR_CODESPLITTERASSOCIATE], None)

NET_DVR_GetCodeSplitterAssociate = _F("NET_DVR_GetCodeSplitterAssociate", "cdecl", c_int, [LONG, DWORD, DWORD, LPNET_DVR_CODESPLITTERASSOCIATE], None)

NET_DVR_InquestGetCDRWScheme = _F("NET_DVR_InquestGetCDRWScheme", "cdecl", c_int, [LONG, LPNET_DVR_INQUEST_CDRW_CFG], None)

NET_DVR_InquestSetCDRWScheme = _F("NET_DVR_InquestSetCDRWScheme", "cdecl", c_int, [LONG, LPNET_DVR_INQUEST_CDRW_CFG], None)

NET_DVR_InquestDeleteFile = _F("NET_DVR_InquestDeleteFile", "cdecl", c_int, [LONG, LPNET_DVR_INQUEST_FILES], None)

NET_DVR_InquestCDWByFile = _F("NET_DVR_InquestCDWByFile", "cdecl", c_int, [LONG, LPNET_DVR_INQUEST_FILES], None)

NET_DVR_InquestUploadFile = _F("NET_DVR_InquestUploadFile", "cdecl", LONG, [LONG, String], None)

NET_DVR_InquestUploadClose = _F("NET_DVR_InquestUploadClose", "cdecl", c_int, [LONG], None)

NET_DVR_InquestGetUploadState = _F("NET_DVR_InquestGetUploadState", "cdecl", LONG, [LONG, LPDWORD], None)

NET_DVR_InquestStartCDW = _F("NET_DVR_InquestStartCDW", "cdecl", c_int, [LONG, c_int], None)

NET_DVR_InquestStopCDW = _F("NET_DVR_InquestStopCDW", "cdecl", c_int, [LONG, c_int], None)

NET_DVR_InquestGetCDWState = _F("NET_DVR_InquestGetCDWState", "cdecl", c_int, [LONG, LPNET_DVR_INQUEST_CDRW_STATUS], None)

NET_DVR_InquestGetPIPStatus = _F("NET_DVR_InquestGetPIPStatus", "cdecl", c_int, [LONG, LPNET_DVR_INQUEST_PIP_STATUS], None)

NET_DVR_InquestSetPIPStatus = _F("NET_DVR_InquestSetPIPStatus", "cdecl", c_int, [LONG, LPNET_DVR_INQUEST_PIP_STATUS], None)

NET_DVR_InquestCheckSecretKey = _F("NET_DVR_InquestCheckSecretKey", "cdecl", c_int, [LONG, POINTER(c_int)], None)

NET_DVR_InquestSetSecretKey = _F("NET_DVR_InquestSetSecretKey", "cdecl", c_int, [LONG, LPNET_DVR_INQUEST_SECRET_INFO], None)

NET_DVR_InquestStreamEncrypt = _F("NET_DVR_InquestStreamEncrypt", "cdecl", c_int, [LONG, LONG, c_int], None)

NET_DVR_InquestGetEncryptState = _F("NET_DVR_InquestGetEncryptState", "cdecl", c_int, [LONG, LONG, POINTER(c_int)], None)

NET_DVR_InquestFindFile = _F("NET_DVR_InquestFindFile", "cdecl", LONG, [LONG], None)

NET_DVR_InquestFindNextFile = _F("NET_DVR_InquestFindNextFile", "cdecl", LONG, [LONG, LPNET_DVR_INQUEST_FILEINFO], None)

NET_DVR_InquestFindClose = _F("NET_DVR_InquestFindClose", "cdecl", c_int, [LONG], None)

NET_DVR_RaidFastConfig = _F("NET_DVR_RaidFastConfig", "cdecl", LONG, [LONG, String], None)

NET_DVR_FastConfigProcess = _F("NET_DVR_FastConfigProcess", "cdecl", c_int, [LONG, POINTER(DWORD)], None)

NET_DVR_CloseFastConfig = _F("NET_DVR_CloseFastConfig", "cdecl", c_int, [LONG], None)

NET_DVR_GetArraySpaceAlloc = _F("NET_DVR_GetArraySpaceAlloc", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_ARRAY_SPACE_ALLOC_INFO], None)

NET_DVR_DelArray = _F("NET_DVR_DelArray", "cdecl", c_int, [LONG, DWORD], None)

NET_DVR_CreateArray = _F("NET_DVR_CreateArray", "cdecl", c_int, [LONG, LPNET_DVR_OPERATE_ARRAY_PARAM], None)

NET_DVR_CalcArraySize = _F("NET_DVR_CalcArraySize", "cdecl", c_int, [LONG, LPNET_DVR_OPERATE_ARRAY_PARAM, POINTER(UINT64)], None)

NET_DVR_MigrateArray = _F("NET_DVR_MigrateArray", "cdecl", c_int, [LONG, LPNET_DVR_OPERATE_ARRAY_PARAM], None)

NET_DVR_RebuildArray = _F("NET_DVR_RebuildArray", "cdecl", c_int, [LONG, LPNET_DVR_OPERATE_ARRAY_PARAM], None)

NET_DVR_CreateVD = _F("NET_DVR_CreateVD", "cdecl", c_int, [LONG, LPNET_DVR_OPERATE_VD_PARAM], None)

NET_DVR_CreateVDEx = _F("NET_DVR_CreateVDEx", "cdecl", c_int, [LONG, LPNET_DVR_OPERATE_VD_PARAM_EX], None)

NET_DVR_DelVD = _F("NET_DVR_DelVD", "cdecl", c_int, [LONG, DWORD], None)

NET_DVR_RepairVD = _F("NET_DVR_RepairVD", "cdecl", c_int, [LONG, DWORD], None)

NET_DVR_SetSpareDisk = _F("NET_DVR_SetSpareDisk", "cdecl", c_int, [LONG, LPNET_DVR_SPARE_DISK_PARAM], None)

NET_DVR_GetPDList = _F("NET_DVR_GetPDList", "cdecl", c_int, [LONG, LPNET_DVR_PHY_DISK_LIST], None)

NET_DVR_GetArrayList = _F("NET_DVR_GetArrayList", "cdecl", c_int, [LONG, LPNET_DVR_ARRAY_LIST], None)

NET_DVR_GetVDList = _F("NET_DVR_GetVDList", "cdecl", c_int, [LONG, LPNET_DVR_VD_LIST], None)

NET_DVR_ExpandDisk = _F("NET_DVR_ExpandDisk", "cdecl", LONG, [LONG, DWORD], None)

NET_DVR_GetExpandProgress = _F("NET_DVR_GetExpandProgress", "cdecl", c_int, [LONG, POINTER(DWORD)], None)

NET_DVR_CloseExpandHandle = _F("NET_DVR_CloseExpandHandle", "cdecl", c_int, [LONG], None)

NET_DVR_AlgoDebugStart = _F("NET_DVR_AlgoDebugStart", "cdecl", LONG, [LONG, LONG, CFUNCTYPE(UNCHECKED(None), LONG, LONG, String, DWORD, POINTER(None)), POINTER(None)], None)

NET_DVR_AlgoDebugSend = _F("NET_DVR_AlgoDebugSend", "cdecl", c_int, [LONG, LONG, String, DWORD], None)

NET_DVR_AlgoDebugStop = _F("NET_DVR_AlgoDebugStop", "cdecl", c_int, [LONG], None)

NET_DVR_SetLogPrint = _F("NET_DVR_SetLogPrint", "cdecl", c_int, [c_int], None)

NET_DVR_SetLogPrintAction = _F("NET_DVR_SetLogPrintAction", "cdecl", c_int, [DWORD, DWORD, c_int, c_int, c_int], None)

NET_DVR_GetPositionRule = _F("NET_DVR_GetPositionRule", "cdecl", c_int, [LONG, LONG, LONG, LPNET_DVR_POSITION_RULE_CFG], None)

NET_DVR_GetPositionRule_V41 = _F("NET_DVR_GetPositionRule_V41", "cdecl", c_int, [LONG, LONG, LONG, LPNET_DVR_POSITION_RULE_CFG_V41], None)

NET_DVR_SetPositionRule = _F("NET_DVR_SetPositionRule", "cdecl", c_int, [LONG, LONG, LONG, LPNET_DVR_POSITION_RULE_CFG], None)

NET_DVR_SetPositionRule_V41 = _F("NET_DVR_SetPositionRule_V41", "cdecl", c_int, [LONG, LONG, LONG, LPNET_DVR_POSITION_RULE_CFG_V41], None)

NET_DVR_SetPositionLimitAngle = _F("NET_DVR_SetPositionLimitAngle", "cdecl", c_int, [LONG, LONG, LONG, LPNET_DVR_LIMIT_ANGLE], None)

NET_DVR_GetPositionLimitAngle = _F("NET_DVR_GetPositionLimitAngle", "cdecl", c_int, [LONG, LONG, LONG, LPNET_DVR_LIMIT_ANGLE], None)

NET_DVR_GetPtzPosition = _F("NET_DVR_GetPtzPosition", "cdecl", c_int, [LONG, LONG, LONG, LPNET_DVR_PTZ_POSITION], None)

NET_DVR_SetPtzPosition = _F("NET_DVR_SetPtzPosition", "cdecl", c_int, [LONG, LONG, LONG, LPNET_DVR_PTZ_POSITION], None)

NET_DVR_SetPatrolTrack = _F("NET_DVR_SetPatrolTrack", "cdecl", c_int, [LONG, LONG, LONG, LPNET_DVR_PATROL_TRACKCFG], None)

NET_DVR_GetPatrolTrack = _F("NET_DVR_GetPatrolTrack", "cdecl", c_int, [LONG, LONG, LONG, LPNET_DVR_PATROL_TRACKCFG], None)

NET_DVR_SetPatrolLimitAngle = _F("NET_DVR_SetPatrolLimitAngle", "cdecl", c_int, [LONG, LONG, LONG, LPNET_DVR_LIMIT_ANGLE], None)

NET_DVR_GetPatrolLimitAngle = _F("NET_DVR_GetPatrolLimitAngle", "cdecl", c_int, [LONG, LONG, LONG, LPNET_DVR_LIMIT_ANGLE], None)

NET_DVR_SetSceneMode = _F("NET_DVR_SetSceneMode", "cdecl", c_int, [LONG, LONG, DWORD], None)

NET_DVR_GetSceneMode = _F("NET_DVR_GetSceneMode", "cdecl", c_int, [LONG, LONG, POINTER(DWORD)], None)

NET_DVR_GetVCAVersion = _F("NET_DVR_GetVCAVersion", "cdecl", c_int, [LONG, LONG, LPNET_DVR_VCA_VERSION], None)

NET_DVR_MatrixPicAdjust = _F("NET_DVR_MatrixPicAdjust", "cdecl", c_int, [LONG, DWORD, DWORD, DWORD], None)

NET_DVR_AlarmJoinedRecord = _F("NET_DVR_AlarmJoinedRecord", "cdecl", c_int, [LONG, DWORD, DWORD, DWORD, DWORD], None)

NET_DVR_SetAlarmSetupResponseCallBack = _F("NET_DVR_SetAlarmSetupResponseCallBack", "cdecl", c_int, [ALARMSETUPRESPONSECallBack, POINTER(None)], None)

NET_DVR_SpringJPEGPicture = _F("NET_DVR_SpringJPEGPicture", "cdecl", c_int, [LONG, LONG, POINTER(NET_DVR_PUSHJPEGPARA)], None)

NET_DVR_SetPushModeParam = _F("NET_DVR_SetPushModeParam", "cdecl", c_int, [LPNET_DVR_PUSHMODEPARAM], None)

NET_DVR_AlarmHostSetupAlarmChan = _F("NET_DVR_AlarmHostSetupAlarmChan", "cdecl", c_int, [LONG, POINTER(NET_DVR_ALARMIN_SETUP)], None)

NET_DVR_AlarmHostCloseAlarmChan = _F("NET_DVR_AlarmHostCloseAlarmChan", "cdecl", c_int, [LONG, POINTER(NET_DVR_ALARMIN_SETUP)], None)

NET_DVR_BypassAlarmChan = _F("NET_DVR_BypassAlarmChan", "cdecl", c_int, [LONG, POINTER(NET_DVR_ALARMIN_SETUP)], None)

NET_DVR_UnBypassAlarmChan = _F("NET_DVR_UnBypassAlarmChan", "cdecl", c_int, [LONG, POINTER(NET_DVR_ALARMIN_SETUP)], None)

NET_DVR_AlarmHostAssistantControl = _F("NET_DVR_AlarmHostAssistantControl", "cdecl", c_int, [LONG, DWORD, DWORD, DWORD], None)

NET_DVR_SetAirCondition = _F("NET_DVR_SetAirCondition", "cdecl", c_int, [LONG, LONG, POINTER(NET_DVR_AIR_CONDITION_PARAM)], None)

NET_DVR_GetAirCondition = _F("NET_DVR_GetAirCondition", "cdecl", c_int, [LONG, LONG, POINTER(NET_DVR_AIR_CONDITION_PARAM)], None)

NET_DVR_GetDeviceTypeList = _F("NET_DVR_GetDeviceTypeList", "cdecl", c_int, [LONG, POINTER(NET_DVR_DEVICE_TYPE_LIST)], None)

NET_DVR_GetDeviceProtoList = _F("NET_DVR_GetDeviceProtoList", "cdecl", c_int, [LONG, LONG, POINTER(NET_DVR_DEVICE_PROTO_LIST)], None)

NET_DVR_GetBatteryVoltage = _F("NET_DVR_GetBatteryVoltage", "cdecl", c_int, [LONG, POINTER(c_float)], None)

NET_DVR_SetAlarmDeviceUser = _F("NET_DVR_SetAlarmDeviceUser", "cdecl", c_int, [LONG, LONG, POINTER(NET_DVR_ALARM_DEVICE_USER)], None)

NET_DVR_GetAlarmDeviceUser = _F("NET_DVR_GetAlarmDeviceUser", "cdecl", c_int, [LONG, LONG, POINTER(NET_DVR_ALARM_DEVICE_USER)], None)

NET_DVR_SetKeyboardUser = _F("NET_DVR_SetKeyboardUser", "cdecl", c_int, [LONG, LONG, POINTER(NET_DVR_KEYBOARD_USER)], None)

NET_DVR_GetKeyboardUser = _F("NET_DVR_GetKeyboardUser", "cdecl", c_int, [LONG, LONG, POINTER(NET_DVR_KEYBOARD_USER)], None)

NET_DVR_SetOperateUser = _F("NET_DVR_SetOperateUser", "cdecl", c_int, [LONG, LONG, POINTER(NET_DVR_OPERATE_USER)], None)

NET_DVR_GetOperateUser = _F("NET_DVR_GetOperateUser", "cdecl", c_int, [LONG, LONG, POINTER(NET_DVR_OPERATE_USER)], None)

NET_DVR_ControlGateway = _F("NET_DVR_ControlGateway", "cdecl", c_int, [LONG, LONG, DWORD], None)

NET_DVR_SetAlarmHostOut = _F("NET_DVR_SetAlarmHostOut", "cdecl", c_int, [LONG, LONG, LONG], None)

NET_DVR_AlarmHostSerialStart = _F("NET_DVR_AlarmHostSerialStart", "cdecl", LONG, [LONG, LONG, fAlarmHostSerialDataCallBack, POINTER(None)], None)

NET_DVR_AlarmHostSerialSend = _F("NET_DVR_AlarmHostSerialSend", "cdecl", c_int, [LONG, LONG, String, DWORD], None)

NET_DVR_AlarmHostSerialStop = _F("NET_DVR_AlarmHostSerialStop", "cdecl", c_int, [LONG], None)

NET_DVR_MatrixAlarmOffMonitor = _F("NET_DVR_MatrixAlarmOffMonitor", "cdecl", c_int, [LONG, DWORD, DWORD], None)

NET_DVR_GetGlobalNum = _F("NET_DVR_GetGlobalNum", "cdecl", c_int, [LONG, POINTER(DWORD), POINTER(DWORD)], None)

NET_DVR_GetCameraListInfo = _F("NET_DVR_GetCameraListInfo", "cdecl", c_int, [LONG, DWORD, DWORD, LPNET_DVR_MATRIX_CAMERALIST], None)

NET_DVR_GetMonitorListInfo = _F("NET_DVR_GetMonitorListInfo", "cdecl", c_int, [LONG, DWORD, DWORD, LPNET_DVR_MATRIX_MONITORLIST], None)

NET_DVR_StartNetworkFlowTest = _F("NET_DVR_StartNetworkFlowTest", "cdecl", LONG, [LONG, POINTER(NET_DVR_FLOW_TEST_PARAM), FLOWTESTCALLBACK, POINTER(None)], None)

NET_DVR_StopNetworkFlowTest = _F("NET_DVR_StopNetworkFlowTest", "cdecl", c_int, [LONG], None)

NET_DVR_FindRecordLabel = _F("NET_DVR_FindRecordLabel", "cdecl", LONG, [LONG, LPNET_DVR_FIND_LABEL], None)

NET_DVR_FindNextLabel = _F("NET_DVR_FindNextLabel", "cdecl", LONG, [LONG, LPNET_DVR_FINDLABEL_DATA], None)

NET_DVR_StopFindLabel = _F("NET_DVR_StopFindLabel", "cdecl", c_int, [LONG], None)

NET_DVR_InsertRecordLabel = _F("NET_DVR_InsertRecordLabel", "cdecl", c_int, [LONG, POINTER(NET_DVR_RECORD_LABEL), POINTER(NET_DVR_LABEL_IDENTIFY)], None)

NET_DVR_DelRecordLabel = _F("NET_DVR_DelRecordLabel", "cdecl", c_int, [LONG, POINTER(NET_DVR_DEL_LABEL_PARAM)], None)

NET_DVR_ModifyRecordLabel = _F("NET_DVR_ModifyRecordLabel", "cdecl", c_int, [LONG, POINTER(NET_DVR_MOD_LABEL_PARAM)], None)

NET_DVR_CapturePlaybackPictureBlock = _F("NET_DVR_CapturePlaybackPictureBlock", "cdecl", c_int, [LONG, String, DWORD], None)

NET_DVR_CapturePlaybackPictureBlock_New = _F("NET_DVR_CapturePlaybackPictureBlock_New", "cdecl", c_int, [LONG, String, DWORD, POINTER(DWORD)], None)

NET_DVR_FindPicture = _F("NET_DVR_FindPicture", "cdecl", LONG, [LONG, POINTER(NET_DVR_FIND_PICTURE_PARAM)], None)

NET_DVR_FindNextPicture = _F("NET_DVR_FindNextPicture", "cdecl", LONG, [LONG, LPNET_DVR_FIND_PICTURE], None)

NET_DVR_FindNextPicture_V40 = _F("NET_DVR_FindNextPicture_V40", "cdecl", LONG, [LONG, LPNET_DVR_FIND_PICTURE_V40], None)

NET_DVR_FindNextPicture_V50 = _F("NET_DVR_FindNextPicture_V50", "cdecl", LONG, [LONG, LPNET_DVR_FIND_PICTURE_V50], None)

NET_DVR_CloseFindPicture = _F("NET_DVR_CloseFindPicture", "cdecl", c_int, [LONG], None)

NET_DVR_GetPicture = _F("NET_DVR_GetPicture", "cdecl", c_int, [LONG, String, String], None)

NET_DVR_GetPicture_V30 = _F("NET_DVR_GetPicture_V30", "cdecl", c_int, [LONG, String, String, DWORD, POINTER(DWORD)], None)

NET_DVR_GetPicture_V50 = _F("NET_DVR_GetPicture_V50", "cdecl", c_int, [LONG, LPNET_DVR_PIC_PARAM], None)

NET_DVR_BackupPicture = _F("NET_DVR_BackupPicture", "cdecl", LONG, [LONG, POINTER(NET_DVR_BACKUP_PICTURE_PARAM)], None)

NET_DVR_GetUpgradeStep = _F("NET_DVR_GetUpgradeStep", "cdecl", LONG, [LONG, POINTER(LONG)], None)

NET_DVR_MatrixGetEncodeJoint = _F("NET_DVR_MatrixGetEncodeJoint", "cdecl", c_int, [LONG, LONG, LPNET_DVR_ENCODE_JOINT_PARAM], None)

NET_DVR_GetLocalIP = _F("NET_DVR_GetLocalIP", "cdecl", c_int, [(c_char * 16) * 16, POINTER(DWORD), POINTER(c_int)], None)

NET_DVR_SetValidIP = _F("NET_DVR_SetValidIP", "cdecl", c_int, [DWORD, c_int], None)

NET_DVR_GetLocalIPv6 = _F("NET_DVR_GetLocalIPv6", "cdecl", c_int, [(BYTE * 16) * 16, POINTER(DWORD), POINTER(c_int)], None)

NET_DVR_SetValidIPv6 = _F("NET_DVR_SetValidIPv6", "cdecl", c_int, [DWORD, c_int], None)

NET_DVR_GetVcaDevWorkState = _F("NET_DVR_GetVcaDevWorkState", "cdecl", c_int, [LONG, LPNET_DVR_VCA_DEV_WORKSTATUS], None)

NET_DVR_SetRecvTimeOut = _F("NET_DVR_SetRecvTimeOut", "cdecl", c_int, [DWORD], None)

NET_DVR_MatrixGetDisplayCfg_V40 = _F("NET_DVR_MatrixGetDisplayCfg_V40", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_VGA_DISP_CHAN_CFG_V40], None)

NET_DVR_MatrixSetDisplayCfg_V40 = _F("NET_DVR_MatrixSetDisplayCfg_V40", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_VGA_DISP_CHAN_CFG_V40], None)

NET_DVR_ShutterCompensation = _F("NET_DVR_ShutterCompensation", "cdecl", c_int, [LONG], None)

NET_DVR_CorrectDeadPixel = _F("NET_DVR_CorrectDeadPixel", "cdecl", c_int, [LONG, LONG, LPNET_DVR_CORRECT_DEADPIXEL_PARAM], None)

NET_DVR_CustomConfig = _F("NET_DVR_CustomConfig", "cdecl", c_int, [LONG, LONG, LPVOID, DWORD, LPVOID, DWORD, LPDWORD], None)

NET_DVR_GetHistoricDataInfo = _F("NET_DVR_GetHistoricDataInfo", "cdecl", c_int, [LONG, LONG, LPNET_DVR_HISTORICDATACFG], None)

NET_DVR_GetHistoricData = _F("NET_DVR_GetHistoricData", "cdecl", c_int, [LONG, LONG, LPNET_DVR_PLATE_RESULT], None)

NET_DVR_ClearHistoricData = _F("NET_DVR_ClearHistoricData", "cdecl", c_int, [LONG, LONG], None)

NET_VPD_SetShutter = _F("NET_VPD_SetShutter", "cdecl", c_int, [LONG, LONG, LPNET_VPD_SHUTTER], None)

NET_VPD_SendPicture = _F("NET_VPD_SendPicture", "cdecl", c_int, [LONG, DWORD, POINTER(BYTE), DWORD, DWORD], None)

NET_DVR_InquestUploadFile_V30 = _F("NET_DVR_InquestUploadFile_V30", "cdecl", LONG, [LONG, LPNET_DVR_INQUEST_ROOM, String], None)

NET_DVR_InquestDeleteFile_V30 = _F("NET_DVR_InquestDeleteFile_V30", "cdecl", c_int, [LONG, LPNET_DVR_INQUEST_ROOM, LPNET_DVR_INQUEST_FILES], None)

NET_DVR_InquestGetPIPStatus_V30 = _F("NET_DVR_InquestGetPIPStatus_V30", "cdecl", c_int, [LONG, LPNET_DVR_INQUEST_ROOM, LPNET_DVR_INQUEST_PIP_STATUS], None)

NET_DVR_InquestSetPIPStatus_V30 = _F("NET_DVR_InquestSetPIPStatus_V30", "cdecl", c_int, [LONG, LPNET_DVR_INQUEST_ROOM, LPNET_DVR_INQUEST_PIP_STATUS], None)

NET_DVR_InquestGetPIPStatus_V40 = _F("NET_DVR_InquestGetPIPStatus_V40", "cdecl", c_int, [LONG, POINTER(NET_DVR_INQUEST_ROOM), LPNET_DVR_INQUEST_PIP_STATUS_V40], None)

NET_DVR_InquestSetPIPStatus_V40 = _F("NET_DVR_InquestSetPIPStatus_V40", "cdecl", c_int, [LONG, POINTER(NET_DVR_INQUEST_ROOM), LPNET_DVR_INQUEST_PIP_STATUS_V40], None)

NET_DVR_InquestGetSystemInfo = _F("NET_DVR_InquestGetSystemInfo", "cdecl", c_int, [LONG, LPNET_DVR_INQUEST_SYSTEM_INFO], None)

NET_DVR_InquestSetSystemInfo = _F("NET_DVR_InquestSetSystemInfo", "cdecl", c_int, [LONG, LPNET_DVR_INQUEST_SYSTEM_INFO], None)

NET_DVR_InquestSendMessage = _F("NET_DVR_InquestSendMessage", "cdecl", c_int, [LONG, LPNET_DVR_INQUEST_ROOM, LPNET_DVR_INQUEST_MESSAGE], None)

NET_DVR_InquestStartCDW_V30 = _F("NET_DVR_InquestStartCDW_V30", "cdecl", c_int, [LONG, LPNET_DVR_INQUEST_ROOM, c_int], None)

NET_DVR_InquestStopCDW_V30 = _F("NET_DVR_InquestStopCDW_V30", "cdecl", c_int, [LONG, LPNET_DVR_INQUEST_ROOM, c_int], None)

NET_DVR_InquestGetCDWState_V30 = _F("NET_DVR_InquestGetCDWState_V30", "cdecl", c_int, [LONG, LPNET_DVR_INQUEST_ROOM, LPNET_DVR_INQUEST_CDRW_STATUS], None)

NET_DVR_InquestResumeEvent = _F("NET_DVR_InquestResumeEvent", "cdecl", LONG, [LONG, LPNET_DVR_INQUEST_RESUME_EVENT], None)

NET_DVR_InquestGetResumeProgress = _F("NET_DVR_InquestGetResumeProgress", "cdecl", c_int, [LONG, POINTER(DWORD)], None)

NET_DVR_InquestStopResume = _F("NET_DVR_InquestStopResume", "cdecl", c_int, [LONG], None)

NET_DVR_InquestFindFile_V30 = _F("NET_DVR_InquestFindFile_V30", "cdecl", LONG, [LONG, LPNET_DVR_INQUEST_ROOM], None)

NET_DVR_InquestGetDeviceVersion = _F("NET_DVR_InquestGetDeviceVersion", "cdecl", c_int, [LONG, LPNET_DVR_INQUEST_DEVICE_VERSION], None)

NET_DVR_SetSDKSecretKey = _F("NET_DVR_SetSDKSecretKey", "cdecl", c_int, [LONG, String], None)

NET_DVR_LockFileByTime = _F("NET_DVR_LockFileByTime", "cdecl", c_int, [LONG, LPNET_DVR_TIME_LOCK, LPNET_DVR_LOCK_RETURN], None)

NET_DVR_UnlockFileByTime = _F("NET_DVR_UnlockFileByTime", "cdecl", c_int, [LONG, LPNET_DVR_TIME_LOCK, LPNET_DVR_LOCK_RETURN], None)

NET_DVR_ScreenZoomIn = _F("NET_DVR_ScreenZoomIn", "cdecl", c_int, [LONG, LPNET_DVR_SCREENZOOM], None)

NET_DVR_MatrixGetAllCameraInfo = _F("NET_DVR_MatrixGetAllCameraInfo", "cdecl", c_int, [LONG, LPNET_DVR_MATRIX_CAMERALIST], None)

NET_DVR_MatrixGetSingleCameraInfo = _F("NET_DVR_MatrixGetSingleCameraInfo", "cdecl", c_int, [LONG, DWORD, LPNET_MATRIX_CAMERAINFO], None)

NET_DVR_MatrixAddCamera = _F("NET_DVR_MatrixAddCamera", "cdecl", c_int, [LONG, DWORD, POINTER(BYTE), DWORD], None)

NET_DVR_MatrixModCameraInfo = _F("NET_DVR_MatrixModCameraInfo", "cdecl", c_int, [LONG, LPNET_MATRIX_CAMERAINFO], None)

NET_DVR_MatrixDelCamera = _F("NET_DVR_MatrixDelCamera", "cdecl", c_int, [LONG, DWORD], None)

NET_DVR_DetectImage_V50 = _F("NET_DVR_DetectImage_V50", "cdecl", c_int, [LONG, LPNET_VCA_FD_PROCIMG_CFG, LPNET_VCA_FD_PROCIMG_RESULT_V50], None)

NET_DVR_MatrixAddMonitor = _F("NET_DVR_MatrixAddMonitor", "cdecl", c_int, [LONG, DWORD, POINTER(BYTE), DWORD], None)

NET_DVR_MatrixModMonitorInfo = _F("NET_DVR_MatrixModMonitorInfo", "cdecl", c_int, [LONG, LPNET_MATRIX_MONITORINFO], None)

NET_DVR_MatrixDelMonitor = _F("NET_DVR_MatrixDelMonitor", "cdecl", c_int, [LONG, DWORD], None)

NET_DVR_MatrixGetAllMonitorInfo = _F("NET_DVR_MatrixGetAllMonitorInfo", "cdecl", c_int, [LONG, LPNET_DVR_MATRIX_MONITORLIST], None)

NET_DVR_MatrixGetSingleMonitorInfo = _F("NET_DVR_MatrixGetSingleMonitorInfo", "cdecl", c_int, [LONG, DWORD, LPNET_MATRIX_MONITORINFO], None)

NET_DVR_MatrixGetAllMatrixInfo = _F("NET_DVR_MatrixGetAllMatrixInfo", "cdecl", c_int, [LONG, LPNET_DVR_MATRIXLIST], None)

NET_DVR_GetSingleMatrixInfo = _F("NET_DVR_GetSingleMatrixInfo", "cdecl", c_int, [LONG, DWORD, LPNET_MATRIX_MATRIXINFO], None)

NET_DVR_AddMatrix = _F("NET_DVR_AddMatrix", "cdecl", c_int, [LONG, LPNET_MATRIX_MATRIXINFO], None)

NET_DVR_ModMatrixInfo = _F("NET_DVR_ModMatrixInfo", "cdecl", c_int, [LONG, LPNET_MATRIX_MATRIXINFO], None)

NET_DVR_DelMatrix = _F("NET_DVR_DelMatrix", "cdecl", c_int, [LONG, DWORD], None)

NET_DVR_MatrixGetResourceInfo = _F("NET_DVR_MatrixGetResourceInfo", "cdecl", c_int, [LONG, DWORD, LPNET_MATRIX_RESOURSEGROUPPARAM], None)

NET_DVR_MatrixAddResourceInfo = _F("NET_DVR_MatrixAddResourceInfo", "cdecl", c_int, [LONG, DWORD, LPNET_MATRIX_RESOURSEGROUPPARAM], None)

NET_DVR_MatrixModResourceInfo = _F("NET_DVR_MatrixModResourceInfo", "cdecl", c_int, [LONG, DWORD, LPNET_MATRIX_RESOURSEGROUPPARAM], None)

NET_DVR_MatrixDelResourceInfo = _F("NET_DVR_MatrixDelResourceInfo", "cdecl", c_int, [LONG, DWORD], None)

NET_DVR_MatrixGetUartParam = _F("NET_DVR_MatrixGetUartParam", "cdecl", c_int, [LONG, DWORD, LPNET_MATRIX_UARTPARAM], None)

NET_DVR_MatrixSetUartParam = _F("NET_DVR_MatrixSetUartParam", "cdecl", c_int, [LONG, DWORD, LPNET_MATRIX_UARTPARAM], None)

NET_DVR_MatrixSeNET_DVR_MatrixGetUserInfotUartParam = _F("NET_DVR_MatrixSeNET_DVR_MatrixGetUserInfotUartParam", "cdecl", c_int, [LONG, DWORD, LPNET_MATRIX_UARTPARAM], None)

NET_DVR_MatrixGetUserInfo = _F("NET_DVR_MatrixGetUserInfo", "cdecl", c_int, [LONG, DWORD, LPNET_MATRIX_USERPARAM], None)

NET_DVR_MatrixAddUser = _F("NET_DVR_MatrixAddUser", "cdecl", c_int, [LONG, DWORD, LPNET_MATRIX_USERPARAM], None)

NET_DVR_MatrixModUserInfo = _F("NET_DVR_MatrixModUserInfo", "cdecl", c_int, [LONG, DWORD, LPNET_MATRIX_USERPARAM], None)

NET_DVR_MatrixDelUser = _F("NET_DVR_MatrixDelUser", "cdecl", c_int, [LONG, DWORD], None)

NET_DVR_MatrixDelResourceInfo = _F("NET_DVR_MatrixDelResourceInfo", "cdecl", c_int, [LONG, DWORD], None)

NET_DVR_MatrixGetUserGroupInfo = _F("NET_DVR_MatrixGetUserGroupInfo", "cdecl", c_int, [LONG, DWORD, LPNET_MATRIX_USERGROUPPARAM], None)

NET_DVR_MatrixAddUserGroupInfo = _F("NET_DVR_MatrixAddUserGroupInfo", "cdecl", c_int, [LONG, DWORD, LPNET_MATRIX_USERGROUPPARAM], None)

NET_DVR_MatrixModUserGroupInfo = _F("NET_DVR_MatrixModUserGroupInfo", "cdecl", c_int, [LONG, DWORD, LPNET_MATRIX_USERGROUPPARAM], None)

NET_DVR_MatrixDelUserGroup = _F("NET_DVR_MatrixDelUserGroup", "cdecl", c_int, [LONG, DWORD], None)

NET_DVR_MatrixGetAllTrunkInfo = _F("NET_DVR_MatrixGetAllTrunkInfo", "cdecl", c_int, [LONG, LPNET_DVR_MATRIX_TRUNKLIST], None)

NET_DVR_MatrixGetTrunkInfo = _F("NET_DVR_MatrixGetTrunkInfo", "cdecl", c_int, [LONG, DWORD, LPNET_MATRIX_TRUNKPARAM], None)

NET_DVR_MatrixAddTrunk = _F("NET_DVR_MatrixAddTrunk", "cdecl", c_int, [LONG, LPNET_MATRIX_TRUNKPARAM], None)

NET_DVR_MatrixModTrunkInfo = _F("NET_DVR_MatrixModTrunkInfo", "cdecl", c_int, [LONG, LPNET_MATRIX_TRUNKPARAM], None)

NET_DVR_MatrixTrunkCtrl = _F("NET_DVR_MatrixTrunkCtrl", "cdecl", c_int, [LONG, DWORD, BYTE], None)

NET_DVR_MatrixTrunkStatusQuery = _F("NET_DVR_MatrixTrunkStatusQuery", "cdecl", c_int, [LONG, DWORD, POINTER(BYTE)], None)

NET_DVR_FindBackgroundPic = _F("NET_DVR_FindBackgroundPic", "cdecl", c_int, [LONG, DWORD, POINTER(BYTE), POINTER(DWORD)], None)

NET_DVR_DetectImage = _F("NET_DVR_DetectImage", "cdecl", c_int, [LONG, LPNET_VCA_FD_PROCIMG_CFG, LPNET_VCA_FD_PROCIMG_RESULT], None)

NET_DVR_GetPictureModel = _F("NET_DVR_GetPictureModel", "cdecl", c_int, [LONG, LPNET_VCA_REGISTER_PIC, LPNET_VCA_PICMODEL_RESULT], None)

NET_DVR_AddBlockList = _F("NET_DVR_AddBlockList", "cdecl", c_int, [LONG, LONG, LPNET_VCA_BLOCKLIST_PARA], None)

NET_DVR_FindBlockList = _F("NET_DVR_FindBlockList", "cdecl", LONG, [LONG, LPNET_VCA_BLOCKLIST_COND], None)

NET_DVR_FindNextBlockList = _F("NET_DVR_FindNextBlockList", "cdecl", LONG, [LONG, LPNET_VCA_BLOCKLIST_INFO], None)

NET_DVR_FindBlockListClose = _F("NET_DVR_FindBlockListClose", "cdecl", c_int, [LONG], None)

NET_DVR_GetBlockListPicture = _F("NET_DVR_GetBlockListPicture", "cdecl", c_int, [LONG, DWORD, LPNET_VCA_BLOCKLIST_PIC], None)

NET_DVR_UpdateBlockList = _F("NET_DVR_UpdateBlockList", "cdecl", c_int, [LONG, LONG, LPNET_VCA_BLOCKLIST_PARA], None)

NET_DVR_DelBlockList = _F("NET_DVR_DelBlockList", "cdecl", c_int, [LONG, LONG, DWORD], None)

NET_DVR_FindSnapPicture = _F("NET_DVR_FindSnapPicture", "cdecl", LONG, [LONG, LPNET_VCA_FIND_PICTURECOND], None)

NET_DVR_FindNextSnapPic = _F("NET_DVR_FindNextSnapPic", "cdecl", LONG, [LONG, LPNET_VCA_SUB_SNAPPIC_DATA], None)

NET_DVR_FindSnapPicClose = _F("NET_DVR_FindSnapPicClose", "cdecl", c_int, [LONG], None)

NET_DVR_AdvanceFindSnapPicture = _F("NET_DVR_AdvanceFindSnapPicture", "cdecl", LONG, [LONG, LPNET_VCA_FIND_PICTURECOND_ADVANCE], None)

NET_DVR_FindFaceMatchAlarm = _F("NET_DVR_FindFaceMatchAlarm", "cdecl", LONG, [LONG, LPNET_VCA_FIND_PICTURECOND], None)

NET_DVR_FindNextFaceMatchAlarm = _F("NET_DVR_FindNextFaceMatchAlarm", "cdecl", LONG, [LONG, LPNET_VCA_FACESNAP_MATCH_ALARM_LOG], None)

NET_DVR_FindFaceMatchAlarmClose = _F("NET_DVR_FindFaceMatchAlarmClose", "cdecl", c_int, [LONG], None)

NET_DVR_GetFaceMatchPic = _F("NET_DVR_GetFaceMatchPic", "cdecl", c_int, [LONG, LPNET_VCA_FACEMATCH_PICCOND, LPNET_VCA_FACEMATCH_PICTURE], None)

NET_DVR_FastAddBlockList = _F("NET_DVR_FastAddBlockList", "cdecl", c_int, [LONG, LONG, LPNET_VCA_BLOCKLIST_FASTREGISTER_PARA], None)

NET_DVR_MatrixSetRemotePlay_V41 = _F("NET_DVR_MatrixSetRemotePlay_V41", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_MATRIX_DEC_REMOTE_PLAY_V41], None)

NET_DVR_MatrixGetDisplayCfg_V41 = _F("NET_DVR_MatrixGetDisplayCfg_V41", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_MATRIX_VOUTCFG], None)

NET_DVR_MatrixSetDisplayCfg_V41 = _F("NET_DVR_MatrixSetDisplayCfg_V41", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_MATRIX_VOUTCFG], None)

NET_DVR_MatrixGetDeviceStatus_V41 = _F("NET_DVR_MatrixGetDeviceStatus_V41", "cdecl", c_int, [LONG, LPNET_DVR_DECODER_WORK_STATUS_V41], None)

NET_DVR_MatrixGetSceneCfg = _F("NET_DVR_MatrixGetSceneCfg", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_MATRIX_SCENECFG], None)

NET_DVR_MatrixSetSceneCfg = _F("NET_DVR_MatrixSetSceneCfg", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_MATRIX_SCENECFG], None)

NET_DVR_MatrixSceneControl = _F("NET_DVR_MatrixSceneControl", "cdecl", c_int, [LONG, DWORD, DWORD, DWORD], None)

NET_DVR_MatrixGetCurrentSceneMode = _F("NET_DVR_MatrixGetCurrentSceneMode", "cdecl", c_int, [LONG, POINTER(DWORD)], None)

NET_DVR_GetAllValidWinInfo = _F("NET_DVR_GetAllValidWinInfo", "cdecl", c_int, [LONG, LPNET_DVR_WINLIST], None)

NET_DVR_ScreenWinCtrl = _F("NET_DVR_ScreenWinCtrl", "cdecl", c_int, [LONG, DWORD, DWORD, LPNET_DVR_SCREEN_WINCFG], None)

NET_DVR_GetScreenInputStatus = _F("NET_DVR_GetScreenInputStatus", "cdecl", c_int, [LONG, LPNET_DVR_SCREENINPUTSTATUS], None)

NET_DVR_PicUpload = _F("NET_DVR_PicUpload", "cdecl", LONG, [LONG, String, LPNET_DVR_PICTURECFG], None)

NET_DVR_GetPicUploadProgress = _F("NET_DVR_GetPicUploadProgress", "cdecl", LONG, [LONG], None)

NET_DVR_CloseUploadHandle = _F("NET_DVR_CloseUploadHandle", "cdecl", c_int, [LONG], None)

NET_DVR_PicControl = _F("NET_DVR_PicControl", "cdecl", c_int, [LONG, BYTE, BYTE, BYTE], None)

NET_DVR_GetPicUploadState = _F("NET_DVR_GetPicUploadState", "cdecl", LONG, [LONG], None)

NET_DVR_ScreenCtrl = _F("NET_DVR_ScreenCtrl", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_SCREEN_CONTROL], None)

NET_DVR_StartScreenPic = _F("NET_DVR_StartScreenPic", "cdecl", LONG, [LONG, DWORD, SCREENPICDATACB, POINTER(None)], None)

NET_DVR_StopScreenPic = _F("NET_DVR_StopScreenPic", "cdecl", c_int, [LONG], None)

NET_DVR_FocusOnePush = _F("NET_DVR_FocusOnePush", "cdecl", c_int, [LONG, LONG], None)

NET_DVR_ResetLens = _F("NET_DVR_ResetLens", "cdecl", c_int, [LONG, LONG], None)

NET_DVR_StartRemoteConfig = _F("NET_DVR_StartRemoteConfig", "cdecl", LONG, [LONG, DWORD, LPVOID, DWORD, fRemoteConfigCallback, LPVOID], None)

NET_DVR_StopRemoteConfig = _F("NET_DVR_StopRemoteConfig", "cdecl", c_int, [LONG], None)

NET_DVR_GetNextRemoteConfig = _F("NET_DVR_GetNextRemoteConfig", "cdecl", LONG, [LONG, POINTER(None), DWORD], None)

NET_DVR_GetRemoteConfigState = _F("NET_DVR_GetRemoteConfigState", "cdecl", c_int, [LONG, POINTER(None)], None)

NET_DVR_SendRemoteConfig = _F("NET_DVR_SendRemoteConfig", "cdecl", c_int, [LONG, DWORD, String, DWORD], None)

NET_DVR_SendWithRecvRemoteConfig = _F("NET_DVR_SendWithRecvRemoteConfig", "cdecl", LONG, [LONG, POINTER(None), DWORD, POINTER(None), DWORD, POINTER(DWORD)], None)

NET_DVR_CloseLongCfgHandle = _F("NET_DVR_CloseLongCfgHandle", "cdecl", c_int, [LONG], None)

NET_DVR_RaidPullDiskStart = _F("NET_DVR_RaidPullDiskStart", "cdecl", LONG, [LONG, LONG, fLongCfgStateCallback, LPVOID], None)

NET_DVR_ScanRaidStart = _F("NET_DVR_ScanRaidStart", "cdecl", LONG, [LONG, fLongCfgStateCallback, LPVOID], None)

NET_DVR_SetAccessCameraInfo = _F("NET_DVR_SetAccessCameraInfo", "cdecl", LONG, [LONG, DWORD, LPNET_DVR_ACCESS_CAMERA_INFO, fLongCfgStateCallback, LPVOID], None)

NET_DVR_InquiryRecordTimeSpan = _F("NET_DVR_InquiryRecordTimeSpan", "cdecl", c_int, [LONG, DWORD, POINTER(NET_DVR_RECORD_TIME_SPAN_INQUIRY), LPNET_DVR_RECORD_TIME_SPAN], None)

NET_DVR_UpdateRecordIndex = _F("NET_DVR_UpdateRecordIndex", "cdecl", c_int, [LONG, DWORD], None)

NET_DVR_GetUpnpNatState = _F("NET_DVR_GetUpnpNatState", "cdecl", c_int, [LONG, LPNET_DVR_UPNP_NAT_STATE], None)

NET_DVR_MatrixGetLoopPlanArray = _F("NET_DVR_MatrixGetLoopPlanArray", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_MATRIX_LOOP_DECINFO_V30], None)

NET_DVR_MatrixSetLoopPlanArray = _F("NET_DVR_MatrixSetLoopPlanArray", "cdecl", c_int, [LONG, DWORD, POINTER(NET_DVR_MATRIX_LOOP_DECINFO_V30)], None)

NET_DVR_MatrixGetAlarmShowMode = _F("NET_DVR_MatrixGetAlarmShowMode", "cdecl", c_int, [LONG, LPNET_DVR_ALARMMODECFG], None)

NET_DVR_MatrixSetAlarmShowMode = _F("NET_DVR_MatrixSetAlarmShowMode", "cdecl", c_int, [LONG, POINTER(NET_DVR_ALARMMODECFG)], None)

NET_DVR_MatrixStartDynamicAssociateDecode = _F("NET_DVR_MatrixStartDynamicAssociateDecode", "cdecl", c_int, [LONG, DWORD, POINTER(NET_DVR_DYNAMICDECODE)], None)

NET_DVR_MatrixAlarmTurn = _F("NET_DVR_MatrixAlarmTurn", "cdecl", c_int, [LONG, DWORD, DWORD], None)

NET_DVR_MatrixAlarmShowControl = _F("NET_DVR_MatrixAlarmShowControl", "cdecl", c_int, [LONG, DWORD, DWORD], None)

NET_DVR_MatrixGetPlanDecode = _F("NET_DVR_MatrixGetPlanDecode", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_PLANDECODE], None)

NET_DVR_MatrixSetPlanDecode = _F("NET_DVR_MatrixSetPlanDecode", "cdecl", c_int, [LONG, DWORD, POINTER(NET_DVR_PLANDECODE)], None)

NET_DVR_MatrixSetLoopDecChanInfo_EX = _F("NET_DVR_MatrixSetLoopDecChanInfo_EX", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_MATRIX_LOOP_DECINFO_EX], None)

NET_DVR_MatrixGetLoopDecChanInfo_EX = _F("NET_DVR_MatrixGetLoopDecChanInfo_EX", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_MATRIX_LOOP_DECINFO_EX], None)

NET_DVR_MatrixStartDynamic_EX = _F("NET_DVR_MatrixStartDynamic_EX", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_PU_STREAM_CFG_EX], None)

NET_DVR_GetTrunkListInfo = _F("NET_DVR_GetTrunkListInfo", "cdecl", c_int, [LONG, DWORD, DWORD, LPNET_DVR_MATRIX_TRUNKLIST, POINTER(DWORD)], None)

NET_DVR_AlarmHostSubSystemSetupAlarmChan = _F("NET_DVR_AlarmHostSubSystemSetupAlarmChan", "cdecl", c_int, [LONG, DWORD], None)

NET_DVR_AlarmHostSubSystemCloseAlarmChan = _F("NET_DVR_AlarmHostSubSystemCloseAlarmChan", "cdecl", c_int, [LONG, DWORD], None)

NET_DVR_AlarmHostClearAlarm = _F("NET_DVR_AlarmHostClearAlarm", "cdecl", c_int, [LONG, DWORD], None)

NET_DVR_AlarmHostArrayBypass = _F("NET_DVR_AlarmHostArrayBypass", "cdecl", c_int, [LONG], None)

NET_DVR_AlarmHostArrayBypassResume = _F("NET_DVR_AlarmHostArrayBypassResume", "cdecl", c_int, [LONG], None)

NET_DVR_AlarmHostSetReportMode = _F("NET_DVR_AlarmHostSetReportMode", "cdecl", c_int, [LONG, LONG, LPVOID, DWORD], None)

NET_DVR_AlarmHostGetReportMode = _F("NET_DVR_AlarmHostGetReportMode", "cdecl", c_int, [LONG, LPVOID, DWORD], None)

NET_DVR_StartUploadAudio = _F("NET_DVR_StartUploadAudio", "cdecl", LONG, [LONG, DWORD, DWORD, String], None)

NET_DVR_StartDownloadAudio = _F("NET_DVR_StartDownloadAudio", "cdecl", LONG, [LONG, DWORD, String], None)

NET_DVR_StopAudioOperate = _F("NET_DVR_StopAudioOperate", "cdecl", c_int, [LONG], None)

NET_DVR_GetAudioProgress = _F("NET_DVR_GetAudioProgress", "cdecl", LONG, [LONG], None)

NET_DVR_AudioCtrl = _F("NET_DVR_AudioCtrl", "cdecl", c_int, [LONG, DWORD, DWORD], None)

NET_DVR_GetDeviceConfig = _F("NET_DVR_GetDeviceConfig", "cdecl", c_int, [LONG, DWORD, DWORD, LPVOID, DWORD, LPVOID, LPVOID, DWORD], None)

NET_DVR_SetDeviceConfig = _F("NET_DVR_SetDeviceConfig", "cdecl", c_int, [LONG, DWORD, DWORD, LPVOID, DWORD, LPVOID, LPVOID, DWORD], None)

NET_DVR_LockStreamFileByTime = _F("NET_DVR_LockStreamFileByTime", "cdecl", c_int, [LONG, LPNET_DVR_STREAM_TIME_LOCK, LPNET_DVR_LOCK_RETURN], None)

NET_DVR_UnlockStreamFileByTime = _F("NET_DVR_UnlockStreamFileByTime", "cdecl", c_int, [LONG, LPNET_DVR_STREAM_TIME_LOCK, LPNET_DVR_LOCK_RETURN], None)

NET_DVR_StartManualRecord = _F("NET_DVR_StartManualRecord", "cdecl", c_int, [LONG, LPNET_DVR_MANUAL_RECORD_PARA], None)

NET_DVR_StopManualRecord = _F("NET_DVR_StopManualRecord", "cdecl", c_int, [LONG, LPNET_DVR_STREAM_INFO], None)

NET_DVR_PlayBackReverseByName = _F("NET_DVR_PlayBackReverseByName", "cdecl", LONG, [LONG, String, HWND], None)

NET_DVR_PlayBackByTime_V40 = _F("NET_DVR_PlayBackByTime_V40", "cdecl", LONG, [LONG, POINTER(NET_DVR_VOD_PARA)], None)

NET_DVR_PlayBackByTime_V50 = _F("NET_DVR_PlayBackByTime_V50", "cdecl", LONG, [LONG, POINTER(NET_DVR_VOD_PARA_V50)], None)

NET_DVR_PlayBackReverseByTime_V40 = _F("NET_DVR_PlayBackReverseByTime_V40", "cdecl", LONG, [LONG, HWND, LPNET_DVR_PLAYCOND], None)

NET_DVR_GetFileByTime_V40 = _F("NET_DVR_GetFileByTime_V40", "cdecl", LONG, [LONG, String, LPNET_DVR_PLAYCOND], None)

NET_DVR_FindFile_V40 = _F("NET_DVR_FindFile_V40", "cdecl", LONG, [LONG, LPNET_DVR_FILECOND_V40], None)

NET_DVR_SetupAlarmChan_V41 = _F("NET_DVR_SetupAlarmChan_V41", "cdecl", LONG, [LONG, LPNET_DVR_SETUPALARM_PARAM], None)

NET_DVR_AddDataBase = _F("NET_DVR_AddDataBase", "cdecl", c_int, [LONG, LPNET_VCA_DATABASE_PARAM], None)

NET_DVR_FindDataBase = _F("NET_DVR_FindDataBase", "cdecl", LONG, [LONG, LPNET_VCA_FIND_DATABASE_COND], None)

NET_DVR_FindNextDataBase = _F("NET_DVR_FindNextDataBase", "cdecl", LONG, [LONG, LPNET_VCA_DATABASE_PARAM], None)

NET_DVR_FindDataBaseClose = _F("NET_DVR_FindDataBaseClose", "cdecl", c_int, [LONG], None)

NET_DVR_UpdateDataBase = _F("NET_DVR_UpdateDataBase", "cdecl", c_int, [LONG, LPNET_VCA_DATABASE_PARAM], None)

NET_DVR_DeleteDataBase = _F("NET_DVR_DeleteDataBase", "cdecl", c_int, [LONG, LPNET_VCA_DELETE_DATABASE_COND], None)

NET_DVR_InquireSnapDBRecord = _F("NET_DVR_InquireSnapDBRecord", "cdecl", LONG, [LONG, DWORD, LPNET_VCA_INQUIRE_SNAPDB_COND, fSearchDBCallBack, POINTER(None)], None)

NET_DVR_GetInquireSnapDBProgress = _F("NET_DVR_GetInquireSnapDBProgress", "cdecl", c_int, [LONG, POINTER(DWORD)], None)

NET_DVR_DeleteSnapDBRecord = _F("NET_DVR_DeleteSnapDBRecord", "cdecl", c_int, [LONG, DWORD, LPNET_VCA_DELETE_SNAPRECORD_COND], None)

NET_DVR_SearchSnapDB = _F("NET_DVR_SearchSnapDB", "cdecl", LONG, [LONG, LPNET_VCA_SEARCH_SNAPDB_COND, fSearchDBCallBack, POINTER(None)], None)

NET_DVR_GetSearchSnapDBProgress = _F("NET_DVR_GetSearchSnapDBProgress", "cdecl", c_int, [LONG, POINTER(DWORD)], None)

NET_DVR_AddFaceDBRecord = _F("NET_DVR_AddFaceDBRecord", "cdecl", c_int, [LONG, DWORD, LPNET_VCA_DATARECORD_INFO], None)

NET_DVR_FastAddFaceDBRecord = _F("NET_DVR_FastAddFaceDBRecord", "cdecl", c_int, [LONG, DWORD, LPNET_VCA_FAST_DATARECORD_INFO], None)

NET_DVR_InquireFaceDBRecord = _F("NET_DVR_InquireFaceDBRecord", "cdecl", LONG, [LONG, LPNET_VCA_DATARECORD_COND, fSearchDBCallBack, POINTER(None)], None)

NET_DVR_GetInquireFaceDBProgress = _F("NET_DVR_GetInquireFaceDBProgress", "cdecl", c_int, [LONG, POINTER(DWORD)], None)

NET_DVR_UpdateFaceDBRecord = _F("NET_DVR_UpdateFaceDBRecord", "cdecl", c_int, [LONG, DWORD, LPNET_VCA_DATARECORD_INFO], None)

NET_DVR_DeleteFaceDBRecord = _F("NET_DVR_DeleteFaceDBRecord", "cdecl", c_int, [LONG, DWORD, LPNET_VCA_DELETE_RECORD_COND], None)

NET_DVR_SearchFaceDB = _F("NET_DVR_SearchFaceDB", "cdecl", LONG, [LONG, LPNET_VCA_SEARCH_FACEDB_COND, fSearchDBCallBack, POINTER(None)], None)

NET_DVR_GetSearchFaceDBProgress = _F("NET_DVR_GetSearchFaceDBProgress", "cdecl", c_int, [LONG, POINTER(DWORD)], None)

NET_DVR_StopSearchDB = _F("NET_DVR_StopSearchDB", "cdecl", c_int, [LONG], None)

NET_DVR_FindMatchPicture = _F("NET_DVR_FindMatchPicture", "cdecl", c_int, [LONG, LPNET_VCA_FIND_MATCHPIC_COND, LPNET_VCA_FIND_MATCHPIC_RESULT], None)

NET_DVR_RemoteControl = _F("NET_DVR_RemoteControl", "cdecl", c_int, [LONG, DWORD, LPVOID, DWORD], None)

NET_DVR_GetBMPByTime = _F("NET_DVR_GetBMPByTime", "cdecl", LONG, [LONG, LONG, POINTER(NET_DVR_TIME), String], None)

NET_DVR_CommandDevice = _F("NET_DVR_CommandDevice", "cdecl", c_int, [LONG, DWORD, LPVOID, DWORD], None)

NET_DVR_TestDVRAlive = _F("NET_DVR_TestDVRAlive", "cdecl", c_int, [LONG], None)

NET_DVR_PicViewRequest = _F("NET_DVR_PicViewRequest", "cdecl", c_int, [LONG, POINTER(NET_DVR_PIC_VIEW_PARAM)], None)

NET_DVR_SetPicViewResponseCallBack = _F("NET_DVR_SetPicViewResponseCallBack", "cdecl", c_int, [PicViewCallBack, POINTER(None)], None)

NET_DVR_SetPicViewDataCallBack = _F("NET_DVR_SetPicViewDataCallBack", "cdecl", c_int, [LONG, SCREENPICDATACB, POINTER(None)], None)

NET_DVR_GetDevList = _F("NET_DVR_GetDevList", "cdecl", c_int, [LONG, LPNET_DVR_DEVLIST], None)

NET_DVR_GetScreenList = _F("NET_DVR_GetScreenList", "cdecl", c_int, [LONG, LPNET_DVR_SCREENLIST], None)

NET_DVR_SetScreenRelation = _F("NET_DVR_SetScreenRelation", "cdecl", c_int, [LONG, POINTER(NET_DVR_DISP_SCREEN)], None)

NET_DVR_TextShowCtrl = _F("NET_DVR_TextShowCtrl", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_TEXTSHOW], None)

NET_DVR_StartUpgrade = _F("NET_DVR_StartUpgrade", "cdecl", LONG, [LONG, LPNET_DVR_OPERATE_DEVICE, DVCS_UPGRADESTATE_CB, POINTER(None)], None)

NET_DVR_StopUpgrade = _F("NET_DVR_StopUpgrade", "cdecl", c_int, [LONG, LPNET_DVR_OPERATE_DEVICE, LONG], None)

NET_DVR_AddNetSignal = _F("NET_DVR_AddNetSignal", "cdecl", c_int, [LONG, LPNET_DVR_NETSIGNAL_INFO, POINTER(None), DWORD], None)

NET_DVR_StartPicPreview = _F("NET_DVR_StartPicPreview", "cdecl", LONG, [LONG, POINTER(NET_DVR_START_PIC_VIEW_INFO), SCREENPICDATACB, POINTER(None)], None)

NET_DVR_GetDeviceStatus = _F("NET_DVR_GetDeviceStatus", "cdecl", c_int, [LONG, DWORD, DWORD, LPVOID, DWORD, LPVOID, LPVOID, DWORD], None)

NET_DVR_GetPlanList = _F("NET_DVR_GetPlanList", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_PLAN_LIST], None)

NET_DVR_GetInputSignalList = _F("NET_DVR_GetInputSignalList", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_INPUT_SIGNAL_LIST], None)

NET_DVR_GetInputSignalList_V40 = _F("NET_DVR_GetInputSignalList_V40", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_INPUT_SIGNAL_LIST], None)

NET_DVR_UploadFile = _F("NET_DVR_UploadFile", "cdecl", LONG, [LONG, DWORD, LPVOID, DWORD, String], None)

NET_DVR_UploadFile_V40 = _F("NET_DVR_UploadFile_V40", "cdecl", LONG, [LONG, DWORD, LPVOID, DWORD, String, LPVOID, DWORD], None)

NET_DVR_GetUploadResult = _F("NET_DVR_GetUploadResult", "cdecl", c_int, [LONG, LPVOID, DWORD], None)

NET_DVR_GetUploadState = _F("NET_DVR_GetUploadState", "cdecl", LONG, [LONG, LPDWORD], None)

NET_DVR_UploadClose = _F("NET_DVR_UploadClose", "cdecl", c_int, [LONG], None)

NET_DVR_StartUploadFile = _F("NET_DVR_StartUploadFile", "cdecl", LONG, [LONG, LPNET_DVR_UPLOAD_PARAM], None)

NET_DVR_GetUploadFileProgress = _F("NET_DVR_GetUploadFileProgress", "cdecl", LONG, [LONG], None)

NET_DVR_GetUploadFileState = _F("NET_DVR_GetUploadFileState", "cdecl", LONG, [LONG], None)

NET_DVR_StopUploadFile = _F("NET_DVR_StopUploadFile", "cdecl", c_int, [LONG], None)

NET_DVR_StartDownloadFile = _F("NET_DVR_StartDownloadFile", "cdecl", LONG, [LONG, LPNET_DVR_DOWNLOAD_PARAM], None)

NET_DVR_GetDownloadFileProgress = _F("NET_DVR_GetDownloadFileProgress", "cdecl", LONG, [LONG], None)

NET_DVR_GetDownloadFileState = _F("NET_DVR_GetDownloadFileState", "cdecl", LONG, [LONG], None)

NET_DVR_StopDownloadFile = _F("NET_DVR_StopDownloadFile", "cdecl", c_int, [LONG], None)

NET_DVR_DownloadControl = _F("NET_DVR_DownloadControl", "cdecl", c_int, [LONG, NET_SDK_DOWNLOAD_CONTROL_TYPE_ENUM, POINTER(None), DWORD, POINTER(None), DWORD], None)

NET_DVR_UploadSend = _F("NET_DVR_UploadSend", "cdecl", LONG, [LONG, POINTER(NET_DVR_SEND_PARAM_IN), POINTER(None)], None)

NET_DVR_GetMobileDevStatus = _F("NET_DVR_GetMobileDevStatus", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_MB_MOBILEDEV_STATUS], None)

NET_DVR_SetVoiceDataCallBack = _F("NET_DVR_SetVoiceDataCallBack", "cdecl", c_int, [LONG, c_int, CFUNCTYPE(UNCHECKED(None), LONG, String, DWORD, BYTE, POINTER(None)), POINTER(None)], None)

NET_DVR_SetTransparentParam = _F("NET_DVR_SetTransparentParam", "cdecl", c_int, [LONG, String, DWORD], None)

NET_DVR_GetTransparentParam = _F("NET_DVR_GetTransparentParam", "cdecl", c_int, [LONG, String, DWORD, String, DWORD], None)

NET_DVR_OpticalUpgrade = _F("NET_DVR_OpticalUpgrade", "cdecl", LONG, [LONG, String, LPNET_DVR_OPTICAL_INFO], None)

NET_DVR_SetSDKLocalConfig = _F("NET_DVR_SetSDKLocalConfig", "cdecl", c_int, [LPNET_DVR_SDKLOCAL_CFG], None)

NET_DVR_GetSDKLocalConfig = _F("NET_DVR_GetSDKLocalConfig", "cdecl", c_int, [LPNET_DVR_SDKLOCAL_CFG], None)

NET_DVR_SetSDKLocalCfg = _F("NET_DVR_SetSDKLocalCfg", "cdecl", c_int, [NET_SDK_LOCAL_CFG_TYPE, POINTER(None)], None)

NET_DVR_GetSDKLocalCfg = _F("NET_DVR_GetSDKLocalCfg", "cdecl", c_int, [NET_SDK_LOCAL_CFG_TYPE, POINTER(None)], None)

NET_DVR_GetVehicleGpsInfo = _F("NET_DVR_GetVehicleGpsInfo", "cdecl", LONG, [LONG, LPNET_DVR_GET_GPS_DATA_PARAM, fGPSDataCallback, POINTER(None)], None)

NET_DVR_ClosePreview = _F("NET_DVR_ClosePreview", "cdecl", c_int, [LONG, DWORD], None)

NET_DVR_ClosePlayBack = _F("NET_DVR_ClosePlayBack", "cdecl", c_int, [LONG, DWORD], None)

NET_DVR_StartDownload = _F("NET_DVR_StartDownload", "cdecl", LONG, [LONG, DWORD, LPVOID, DWORD, String], None)

NET_DVR_GetDownloadState = _F("NET_DVR_GetDownloadState", "cdecl", LONG, [LONG, LPDWORD], None)

NET_DVR_GetDownloadStateInfo = _F("NET_DVR_GetDownloadStateInfo", "cdecl", c_int, [LONG, POINTER(None)], None)

NET_DVR_StopDownload = _F("NET_DVR_StopDownload", "cdecl", c_int, [LONG], None)

NET_DVR_MatrixStartDynamic_V41 = _F("NET_DVR_MatrixStartDynamic_V41", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_PU_STREAM_CFG_V41], None)

NET_DVR_MatrixGetLoopDecChanInfo_V41 = _F("NET_DVR_MatrixGetLoopDecChanInfo_V41", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_MATRIX_LOOP_DECINFO_V41], None)

NET_DVR_MatrixSetLoopDecChanInfo_V41 = _F("NET_DVR_MatrixSetLoopDecChanInfo_V41", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_MATRIX_LOOP_DECINFO_V41], None)

NET_DVR_MatrixGetDecChanInfo_V41 = _F("NET_DVR_MatrixGetDecChanInfo_V41", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_MATRIX_DEC_CHAN_INFO_V41], None)

NET_DVR_StartT1Test = _F("NET_DVR_StartT1Test", "cdecl", LONG, [LONG, LPNET_DVR_ALARMHOST_DOWNLOAD_PARAM], None)

NET_DVR_StopTT1Test = _F("NET_DVR_StopTT1Test", "cdecl", c_int, [c_int], None)

NET_DVR_GetT1TestStatus = _F("NET_DVR_GetT1TestStatus", "cdecl", c_int, [LONG, POINTER(LONG)], None)

NET_DVR_SendT1TestData = _F("NET_DVR_SendT1TestData", "cdecl", c_int, [LONG, DWORD, String, DWORD], None)

NET_DVR_UploadLogo_NEW = _F("NET_DVR_UploadLogo_NEW", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_MATRIX_LOGO_INFO, String], None)

NET_DVR_StartPassiveTransCode = _F("NET_DVR_StartPassiveTransCode", "cdecl", LONG, [LONG, POINTER(NET_DVR_STREAM_INFO), POINTER(NET_DVR_COMPRESSIONCFG_V30), POINTER(NET_DVR_PASSIVETRANSINFO), CFUNCTYPE(UNCHECKED(None), LONG, DWORD, POINTER(BYTE), DWORD, POINTER(None)), POINTER(None)], None)

NET_DVR_TransCodeInputData = _F("NET_DVR_TransCodeInputData", "cdecl", c_int, [LONG, POINTER(BYTE), DWORD], None)

NET_DVR_StopPassiveTransCode = _F("NET_DVR_StopPassiveTransCode", "cdecl", c_int, [LONG], None)

NET_DVR_GetPassiveTransChanNum = _F("NET_DVR_GetPassiveTransChanNum", "cdecl", LONG, [LONG], None)

NET_DVR_SetDeviceConfigEx = _F("NET_DVR_SetDeviceConfigEx", "cdecl", c_int, [LONG, DWORD, DWORD, POINTER(NET_DVR_IN_PARAM), POINTER(NET_DVR_OUT_PARAM)], None)

NET_DVR_MatrixGetUnitedMatrixInfo = _F("NET_DVR_MatrixGetUnitedMatrixInfo", "cdecl", c_int, [LONG, LPNET_DVR_ALLUNITEDMATRIXINFO], None)

NET_DVR_MatrixSetUnitedMatrixInfo = _F("NET_DVR_MatrixSetUnitedMatrixInfo", "cdecl", c_int, [LONG, LPNET_DVR_ALLUNITEDMATRIXINFO], None)

NET_DVR_MatrixGetGatewayInfo = _F("NET_DVR_MatrixGetGatewayInfo", "cdecl", c_int, [LONG, LPNET_DVR_MATRIXGATEWAYINFO], None)

NET_DVR_MatrixSetGatewayInfo = _F("NET_DVR_MatrixSetGatewayInfo", "cdecl", c_int, [LONG, LPNET_DVR_MATRIXGATEWAYINFO], None)

NET_DVR_MatrixSpanSwitch = _F("NET_DVR_MatrixSpanSwitch", "cdecl", c_int, [LONG, BYTE, LPNET_DVR_MATRIXSWITCH], None)

NET_DVR_MatrixStartSwitch = _F("NET_DVR_MatrixStartSwitch", "cdecl", c_int, [LONG, LPNET_DVR_MATRIXSWITCHCTRL], None)

NET_DVR_MatrixSetConfigFile = _F("NET_DVR_MatrixSetConfigFile", "cdecl", c_int, [LONG, LPNET_DVR_MATRIXDATABASE, String, DWORD], None)

NET_DVR_MatrixGetConfigFile = _F("NET_DVR_MatrixGetConfigFile", "cdecl", c_int, [LONG, LPNET_DVR_MATRIXDATABASE, String, DWORD, POINTER(DWORD)], None)

NET_DVR_MatrixGetSubSystemInfo_V40 = _F("NET_DVR_MatrixGetSubSystemInfo_V40", "cdecl", c_int, [LONG, LPNET_DVR_ALLSUBSYSTEMINFO_V40], None)

NET_DVR_MatrixSetSubSystemInfo_V40 = _F("NET_DVR_MatrixSetSubSystemInfo_V40", "cdecl", c_int, [LONG, LPNET_DVR_ALLSUBSYSTEMINFO_V40], None)

NET_DVR_MatrixGetSubDecSystemJoinInfo_V40 = _F("NET_DVR_MatrixGetSubDecSystemJoinInfo_V40", "cdecl", c_int, [LONG, LPNET_DVR_ALLDECSUBSYSTEMJOININFO_V40], None)

NET_DVR_GetSTDConfig = _F("NET_DVR_GetSTDConfig", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_STD_CONFIG], None)

NET_DVR_SetSTDConfig = _F("NET_DVR_SetSTDConfig", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_STD_CONFIG], None)

NET_DVR_GetSTDAbility = _F("NET_DVR_GetSTDAbility", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_STD_ABILITY], None)

NET_DVR_STDControl = _F("NET_DVR_STDControl", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_STD_CONTROL], None)

NET_DVR_STDXMLConfig = _F("NET_DVR_STDXMLConfig", "cdecl", c_int, [LONG, POINTER(NET_DVR_XML_CONFIG_INPUT), POINTER(NET_DVR_XML_CONFIG_OUTPUT)], None)

NET_DVR_Upgrade_V40 = _F("NET_DVR_Upgrade_V40", "cdecl", LONG, [DWORD, DWORD, String, POINTER(None), DWORD], None)

NET_DVR_Upgrade_V50 = _F("NET_DVR_Upgrade_V50", "cdecl", LONG, [DWORD, LPNET_DVR_UPGRADE_PARAM], None)

NET_DVR_GetUnitedMatrixInfo = _F("NET_DVR_GetUnitedMatrixInfo", "cdecl", c_int, [LONG, LPNET_DVR_UNITEDMATRIXINFO], None)

NET_DVR_SetRegisterCallBack = _F("NET_DVR_SetRegisterCallBack", "cdecl", c_int, [REGCallBack, POINTER(None)], None)

NET_DVR_PreviewRequest = _F("NET_DVR_PreviewRequest", "cdecl", c_int, [LONG, LONG, LPNET_DVR_PREVIEWPARAM, LPNET_DVR_DEVICENATINFO], None)

NET_DVR_SetPreviewResponseCallBack = _F("NET_DVR_SetPreviewResponseCallBack", "cdecl", c_int, [PREVIEWRESPONSECallBack, POINTER(None)], None)

NET_DVR_PlaybackRequest = _F("NET_DVR_PlaybackRequest", "cdecl", c_int, [LONG, LPNET_DVR_PLAYBACKREQUESTPARAM], None)

NET_DVR_SetPlaybackResponseCallBack = _F("NET_DVR_SetPlaybackResponseCallBack", "cdecl", c_int, [PLAYBACKRESPONSECallBack, POINTER(None)], None)

NET_DVR_SetVoiceResponseCallBack = _F("NET_DVR_SetVoiceResponseCallBack", "cdecl", c_int, [VOICERESPONSECallBack, POINTER(None)], None)

NET_DVR_VoiceRequest = _F("NET_DVR_VoiceRequest", "cdecl", c_int, [LONG, LPNET_DVR_VOICEREQUESTPARAM], None)

NET_DVR_AlarmSetupRequest = _F("NET_DVR_AlarmSetupRequest", "cdecl", c_int, [LONG, LPNET_DVR_ALARMSETUPREQUESTPARAM], None)

NET_DVR_GetDialParam = _F("NET_DVR_GetDialParam", "cdecl", c_int, [LONG, LPNET_DVR_DIALREQUEST, LPNET_DVR_DIALPARAM], None)

NET_DVR_SetDialParam = _F("NET_DVR_SetDialParam", "cdecl", c_int, [LONG, LPNET_DVR_DIALREQUEST, LPNET_DVR_DIALPARAM], None)

NET_DVR_GetSmsListInfo = _F("NET_DVR_GetSmsListInfo", "cdecl", c_int, [LONG, LPNET_DVR_TIME_EX, LPNET_DVR_TIME_EX, LPNET_DVR_SMSLISTINFO], None)

NET_DVR_SendSms = _F("NET_DVR_SendSms", "cdecl", c_int, [LONG, LPNET_DVR_SMSCONTENT], None)

NET_DVR_GetSmsContent = _F("NET_DVR_GetSmsContent", "cdecl", c_int, [LONG, DWORD, LPNET_DVR_SMSCONTENT], None)

NET_DVR_SmartSearchPicture = _F("NET_DVR_SmartSearchPicture", "cdecl", LONG, [LONG, POINTER(NET_DVR_SMART_SEARCH_PIC_PARA)], None)

NET_DVR_FindNextSmartPicture = _F("NET_DVR_FindNextSmartPicture", "cdecl", LONG, [LONG, LPNET_DVR_SMART_SEARCH_PIC_RET], None)

NET_DVR_CloseSmartSearchPicture = _F("NET_DVR_CloseSmartSearchPicture", "cdecl", c_int, [LONG], None)

NET_DVR_MatrixGetSubDecSystemJoinInfo_V41 = _F("NET_DVR_MatrixGetSubDecSystemJoinInfo_V41", "cdecl", c_int, [LONG, LPNET_DVR_ALLDECSUBSYSTEMJOININFO_V41], None)

NET_DVR_SetESCallBack = _F("NET_DVR_SetESCallBack", "cdecl", c_int, [LONG, CFUNCTYPE(UNCHECKED(None), LONG, DWORD, POINTER(BYTE), DWORD, POINTER(None)), POINTER(None)], None)

NET_DVR_SetESRealPlayCallBack = _F("NET_DVR_SetESRealPlayCallBack", "cdecl", c_int, [LONG, CFUNCTYPE(UNCHECKED(None), LONG, POINTER(NET_DVR_PACKET_INFO_EX), POINTER(None)), POINTER(None)], None)

NET_DVR_ActivateDevice = _F("NET_DVR_ActivateDevice", "cdecl", c_int, [String, WORD, LPNET_DVR_ACTIVATECFG], None)

NET_DVR_GetAddrInfoByServer = _F("NET_DVR_GetAddrInfoByServer", "cdecl", c_int, [DWORD, POINTER(None), DWORD, POINTER(None), DWORD], None)

NET_DVR_StartGetDevState = _F("NET_DVR_StartGetDevState", "cdecl", c_int, [LPNET_DVR_CHECK_DEV_STATE], None)

NET_DVR_StopGetDevState = _F("NET_DVR_StopGetDevState", "cdecl", c_int, [], None)

NET_DVR_RigisterPlayBackDrawFun = _F("NET_DVR_RigisterPlayBackDrawFun", "cdecl", c_int, [LONG, CFUNCTYPE(UNCHECKED(None), LONG, HDC, DWORD), DWORD], None)

NET_DVR_SetSDKInitCfg = _F("NET_DVR_SetSDKInitCfg", "cdecl", c_int, [NET_SDK_INIT_CFG_TYPE, POINTER(None)], None)

NET_DVR_ReleaseSDKMemPool = _F("NET_DVR_ReleaseSDKMemPool", "cdecl", c_int, [LPNET_DVR_SDKMEMPOOL_CFG], None)

NET_DVR_CapturePictureBlock = _F("NET_DVR_CapturePictureBlock", "cdecl", c_int, [LONG, String, DWORD], None)

NET_DVR_CapturePictureBlock_New = _F("NET_DVR_CapturePictureBlock_New", "cdecl", c_int, [LONG, String, DWORD, POINTER(DWORD)], None)

NET_DVR_ChangeWndResolution = _F("NET_DVR_ChangeWndResolution", "cdecl", c_int, [LONG], None)

NET_DVR_SDKChannelToISAPI = _F("NET_DVR_SDKChannelToISAPI", "cdecl", LONG, [LONG, LONG, c_int], None)

NET_DVR_STDXMLConfig_Conv = _F("NET_DVR_STDXMLConfig_Conv", "cdecl", c_int, [LONG, POINTER(NET_DVR_XML_CONFIG_INPUT), POINTER(NET_DVR_XML_CONFIG_OUTPUT)], None)

NET_DVR_SetDevXmlLen = _F("NET_DVR_SetDevXmlLen", "cdecl", c_int, [LONG, WORD], None)

NET_DVR_SetupAlarmChan_V50 = _F("NET_DVR_SetupAlarmChan_V50", "cdecl", LONG, [LONG, LPNET_DVR_SETUPALARM_PARAM_V50, String, DWORD], None)

NET_DVR_GetAlarmSubscribe = _F("NET_DVR_GetAlarmSubscribe", "cdecl", c_int, [LONG, String, DWORD], None)

NET_DVR_SetAlarmSubscribe = _F("NET_DVR_SetAlarmSubscribe", "cdecl", c_int, [LONG, String, DWORD], None)

NET_DVR_GetNPQStat = _F("NET_DVR_GetNPQStat", "cdecl", c_int, [LONG, POINTER(NET_SDK_NPQ_STATE)], None)

NET_DVR_SetNPQNotifyParam = _F("NET_DVR_SetNPQNotifyParam", "cdecl", c_int, [LONG, POINTER(NET_SDK_NPQ_NOTIFY_PARAM)], None)

NET_DVR_PlaybackGetNPQStat = _F("NET_DVR_PlaybackGetNPQStat", "cdecl", c_int, [LONG, POINTER(NET_SDK_NPQ_STATE)], None)

NET_DVR_RenderPrivateData = _F("NET_DVR_RenderPrivateData", "cdecl", c_int, [LONG, c_int, c_int], None)

NET_DVR_RenderPrivateDataEx = _F("NET_DVR_RenderPrivateDataEx", "cdecl", c_int, [LONG, c_int, c_int, c_int], None)

NET_DVR_PlaybackSetNPQNotifyParam = _F("NET_DVR_PlaybackSetNPQNotifyParam", "cdecl", c_int, [LONG, POINTER(NET_SDK_NPQ_NOTIFY_PARAM)], None)

NET_DVR_EnableRelogon = _F("NET_DVR_EnableRelogon", "cdecl", c_int, [c_int, DWORD], None)

NET_DVR_CreateEzvizUser = _F("NET_DVR_CreateEzvizUser", "cdecl", LONG, [LPNET_DVR_EZVIZ_USER_LOGIN_INFO, LPNET_DVR_DEVICEINFO_V30], None)

NET_DVR_DeleteEzvizUser = _F("NET_DVR_DeleteEzvizUser", "cdecl", c_int, [LONG], None)

NET_DVR_CreateOpenEzvizUser = _F("NET_DVR_CreateOpenEzvizUser", "cdecl", LONG, [LPNET_DVR_OPEN_EZVIZ_USER_LOGIN_INFO, LPNET_DVR_DEVICEINFO_V40], None)

NET_DVR_DeleteOpenEzvizUser = _F("NET_DVR_DeleteOpenEzvizUser", "cdecl", c_int, [LONG], None)

NET_DVR_LoadAdditionalLib = _F("NET_DVR_LoadAdditionalLib", "cdecl", c_int, [enum_ADDITIONAL_LIB, String], None)

# No inserted files

# No prefix-stripping

