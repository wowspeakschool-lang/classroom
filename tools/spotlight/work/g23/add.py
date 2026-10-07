import csv, sys
# usage: add.py <grade> <crop>  ; stdin lines: module|section|term|pos|translation|note
g, crop = sys.argv[1], sys.argv[2]
path = f"/home/user/classroom/tools/spotlight/tsv/grade_{g}.tsv"
rows = []
for line in sys.stdin:
    line = line.rstrip("\n")
    if not line.strip(): continue
    p = [x.strip().replace("’", "'").replace("‘", "'") for x in line.split("|")]
    p += [""] * (6 - len(p))
    rows.append([g] + p[:6])
with open(path, "a", newline="", encoding="utf-8") as f:
    csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
open("/home/user/classroom/tools/spotlight/work/g23/state.txt", "a").write(f"{g} {crop} {len(rows)}\n")
print(len(rows), "rows")
