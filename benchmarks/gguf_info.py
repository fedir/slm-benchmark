#!/usr/bin/env python3
"""Print selected GGUF metadata (architecture, size label, quantisation, context length, tensor count) of the benchmarked models."""
import json, os, struct, sys
T = {0: "<B", 1: "<b", 2: "<H", 3: "<h", 4: "<I", 5: "<i", 6: "<f", 7: "<?", 10: "<Q", 11: "<q", 12: "<d"}
def rd(f, t):
    if t in T: return struct.unpack(T[t], f.read(struct.calcsize(T[t])))[0]
    if t == 8: n = struct.unpack("<Q", f.read(8))[0]; return f.read(n).decode("utf8", "replace")
    if t == 9:
        et, n = struct.unpack("<IQ", f.read(12)); return [rd(f, et) for _ in range(n)] if n < 64 else (f.seek(0, 1), "<array>")[1] if [rd(f, et) for _ in range(n)] else "<array>"
    raise ValueError(t)
def info(path):
    f = open(os.path.expanduser(path), "rb"); assert f.read(4) == b"GGUF"
    ver, nt, nkv = struct.unpack("<IQQ", f.read(20)); kv = {}
    for _ in range(nkv):
        n = struct.unpack("<Q", f.read(8))[0]; k = f.read(n).decode(); t = struct.unpack("<I", f.read(4))[0]; kv[k] = rd(f, t)
    return ver, nt, kv
FT = {0: "F32", 1: "F16", 2: "Q4_0", 3: "Q4_1", 7: "Q8_0", 8: "Q5_0", 9: "Q5_1", 10: "Q2_K", 11: "Q3_K_S", 12: "Q3_K_M", 13: "Q3_K_L", 14: "Q4_K_S", 15: "Q4_K_M", 16: "Q5_K_S", 17: "Q5_K_M", 18: "Q6_K"}
for name, spec in json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "models.json"))).items():
    p = os.path.expanduser(spec["path"]); ver, nt, kv = info(p); arch = kv.get("general.architecture")
    ctx = kv.get(f"{arch}.context_length"); ft = kv.get("general.file_type")
    print(f"{name}: arch={arch} size_label={kv.get('general.size_label')} name={kv.get('general.name')} file_type={FT.get(ft, ft)} "
          f"ctx_train={ctx} tensors={nt} file={os.path.getsize(p)/1e9:.2f} GB basename={kv.get('general.basename')} finetune={kv.get('general.finetune')}")
