from os import walk

for subdir, dir, file in walk("."):
        with open(f"{subdir}\.keep", "w") as f:
            pass