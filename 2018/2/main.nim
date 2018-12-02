import sets, strutils, tables

proc a(ids: seq[string]): int =
  var
    t2 = 0
    t3 = 0
  for s in ids:
    var
      d2 = 0
      d3 = 0
    for k, v in toCountTable(s):
      if v == 2:
        d2 = 1
      if v == 3:
        d3 = 1
    t2 += d2
    t3 += d3
  return t2 * t3

proc b(ids: seq[string]): string =
  var seen = initSet[(string, string)]()
  for s in ids:
    for c in 0..len(s)-1:
      let k = (s[0..c-1], s[c+1..^1])
      if k in seen:
        return k[0] & k[1]
      seen.incl(k)

let ids = readFile("input").splitWhitespace
echo "A: ", a(ids)
echo "B: ", b(ids)
