#---------------------------------------------------------------------
# Example user initialisation script: idapythonrc.py
#
# Place this script to ~/.idapro/ or to
# %APPDATA%\Hex-Rays\IDA Pro
#---------------------------------------------------------------------
import idaapi
# from ida_ida import inf_is_32bit_exactly as is_32bit, inf_is_64bit as is_64bit

# Add your favourite script to ScriptBox for easy access
# scriptbox.addscript("/here/is/my/favourite/script.py")

# Uncomment if you want to set Python as default interpreter in IDA
idaapi.enable_extlang_python(True)

# Disable the Python from interactive command-line
# idaapi.enable_python_cli(False)

# Set the timeout for the script execution cancel dialog
# idaapi.set_script_timeout(10)

load_and_run_plugin("qscripts", 2)

def detect_guids():
    import idautils
    import idc
    from uuid import UUID
    print("Attempting to detect GUIDs and set repeatable comments on them")
    guids = set([ea for ea in idautils.Heads() if idc.get_type(ea) in {"IID", "GUID", "_GUID"}])
    print(f"Found {len(guids)} GUIDs")
    for ea in sorted(guids):
        binguid = idc.get_bytes(ea, 16)
        guid = UUID(bytes=binguid)
        idc.set_cmt(ea, f"{{{guid}}}", 1)

def register_pyfunc(funcname: str, hotkey: str):
    from  ida_expr import compile_idc_text
    from ida_kernwin import add_idc_hotkey, del_idc_hotkey
    hotkey_reg = hotkey.replace("+", "_")
    idcfunc = f"static key_{hotkey_reg}() {{ RunPythonStatement(\"{funcname}()\"); }}"
    print(f"{hotkey} -> {funcname}(): {idcfunc=}")
    compile_idc_text(idcfunc)
    del_idc_hotkey(hotkey)
    add_idc_hotkey(hotkey, f"key_{hotkey_reg}")

register_pyfunc("detect_guids", "Ctrl+Alt+G")
