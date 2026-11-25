#!/usr/bin/env python3
"""validate.py <company-folder> [<extension>...]: check extensions with the installer's own code."""
import importlib.util
import os
import sys

company, names = os.path.abspath(sys.argv[1]), sys.argv[2:]
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("ext", os.path.join(company, ".claude/skills/extensions/extensions.py"))
ext = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ext)
names = names or sorted(d for d in os.listdir(root) if os.path.isfile(os.path.join(root, d, "extension.json")))
bad = 0
for name in names:
    files = {}
    for base, dirs, found in os.walk(os.path.join(root, name)):
        for n in found + [d for d in dirs if os.path.islink(os.path.join(base, d))]:
            p = os.path.join(base, n)
            if os.path.islink(p) or os.stat(p).st_mode & 0o111:
                print(f"{name}: {n}: links and executable files aren't allowed")
                bad = 1
                continue
            with open(p, "rb") as f:
                files[os.path.relpath(p, os.path.join(root, name)).replace(os.sep, "/")] = f.read()
    try:
        m, out = ext.validate(files)
        if m["id"] != name:
            raise ext.Refused(f"the folder must be named {m['id']}")
        print(f"{name} {m['version']}: OK, {len(out)} files")
    except ext.Refused as e:
        print(f"{name}: {e}")
        bad = 1
sys.exit(bad)
