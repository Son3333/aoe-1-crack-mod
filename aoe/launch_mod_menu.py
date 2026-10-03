import ctypes
from ctypes import wintypes
import sys

kernel32 = ctypes.windll.kernel32

class STARTUPINFO(ctypes.Structure):
    _fields_ = [
        ('cb', wintypes.DWORD),
        ('lpReserved', wintypes.LPWSTR),
        ('lpDesktop', wintypes.LPWSTR),
        ('lpTitle', wintypes.LPWSTR),
        ('dwX', wintypes.DWORD),
        ('dwY', wintypes.DWORD),
        ('dwXSize', wintypes.DWORD),
        ('dwYSize', wintypes.DWORD),
        ('dwXCountChars', wintypes.DWORD),
        ('dwYCountChars', wintypes.DWORD),
        ('dwFillAttribute', wintypes.DWORD),
        ('dwFlags', wintypes.DWORD),
        ('wShowWindow', wintypes.WORD),
        ('cbReserved2', wintypes.WORD),
        ('lpReserved2', ctypes.c_void_p),
        ('hStdInput', wintypes.HANDLE),
        ('hStdOutput', wintypes.HANDLE),
        ('hStdError', wintypes.HANDLE),
    ]

class PROCESS_INFORMATION(ctypes.Structure):
    _fields_ = [
        ('hProcess', wintypes.HANDLE),
        ('hThread', wintypes.HANDLE),
        ('dwProcessId', wintypes.DWORD),
        ('dwThreadId', wintypes.DWORD),
    ]

si = STARTUPINFO()
si.cb = ctypes.sizeof(STARTUPINFO)
si.lpDesktop = "WinSta0\\Default"

pi = PROCESS_INFORMATION()

cmdline = r'"C:\Program Files\Python313\pythonw.exe" "C:\Users\admin\Downloads\Cai-dat-AOE\Cai-dat-AOE\AOE\mod_menu.py"'
cwd = r"C:\Users\admin\Downloads\Cai-dat-AOE\Cai-dat-AOE\AOE"

success = kernel32.CreateProcessW(None, cmdline, None, None, False, 0, None, cwd, ctypes.byref(si), ctypes.byref(pi))
if not success:
    print("Failed to start Mod Menu, error:", kernel32.GetLastError())
    sys.exit(1)

print("Mod Menu successfully started on user desktop! PID:", pi.dwProcessId)
sys.stdout.flush()

kernel32.WaitForSingleObject(pi.hProcess, 0xFFFFFFFF)
print("Mod Menu closed.")

