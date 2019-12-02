"""
Generate _spirv_constants.py
"""

preamble = '''
"""
All the SpirV constants. Generated by the Python file provided by Khronos at
https://raw.githubusercontent.com/KhronosGroup/SPIRV-Headers/master/include/spirv/unified1/spirv.py
"""

# NOTE: THIS CODE IS AUTOGENERATED; DO NOT EDIT

builtins = {}

class Enum(int):
    """ Enum (integer) with a meaningfull repr. """
    def __new__(cls, name, value):
        base = int.__new__(cls, value)
        base.name = name
        if name.startswith("BuiltIn_"):
            builtins[name[8:]] = base
        return base
    def __repr__(self):
        return self.name
'''


# Get dict
ns = {}
exec(open("spirv.py", "rb").read().decode(), ns, ns)
spv = ns["spv"]

# Process and generate lines
pylines = []
for key, val in spv.items():
    if isinstance(val, dict):
        pylines.append("")
        for subkey, val in val.items():
            fullkey = subkey if key.startswith("Op") else key + "_" + subkey
            pylines.append(f"{fullkey} = Enum({fullkey!r}, {val!r})")
    else:
        rval = (
            hex(val) if key in ("MagicNumber", "Version", "OpCodeMask") else repr(val)
        )
        pylines.append(f"{key} = Enum({key!r}, {rval})")

text = preamble.strip() + "\n\n\n" + "\n".join(pylines) + "\n"

with open("../_spirv_constants.py", "wb") as f:
    f.write(text.encode())