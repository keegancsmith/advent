import sets, strutils, tables

type Claim = tuple[id, x, y, dx, dy: int]

proc a(claims: seq[Claim]): int =
  var d = initCountTable[(int, int)]()
  for c in claims:
    for x in c.x..<c.x + c.dx:
      for y in c.y..<c.y + c.dy:
        d.inc((x, y))

  for count in d.values:
    if count > 1:
      result += 1

proc b(claims: seq[Claim]): int =
  var
    free = initSet[int]()
    d = initTable[(int, int), int]()
  for c in claims:
    free.incl(c.id)
    for x in c.x..<c.x + c.dx:
      for y in c.y..<c.y + c.dy:
        let k = (x, y)
        if k in d:
          free.excl(d[k])
          free.excl(c.id)
        else:
          d[k] = c.id

  assert len(free) == 1
  return free.pop

var claims: seq[Claim]
for line in readFile("input").splitLines:
  let p = line.split({' ', '#', '@', ',', ':', 'x'})
  if len(p) < 8:
    continue
  claims.add((p[1].parseInt, p[4].parseInt, p[5].parseInt, p[7].parseInt, p[8].parseInt))

echo "A: ", a(claims)
echo "B: ", b(claims)
