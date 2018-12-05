import strutils, sequtils

proc solve(y: string): int =
  var x = y
  var r: seq[(string, string)]
  for c in 'a'..'z':
    r.add((c & c.toUpperASCII, ""))
    r.add((c.toUpperASCII & c, ""))
  while true:
    let n = len(x)
    x = x.multiReplace(r)
    if len(x) == n:
      return len(x)

var x = readFile("input").strip
echo "A: ", solve(x)

var ans = len(x)
for c in 'a'..'z':
  let y = x.replace("" & c, "").replace("" & c.toUpperASCII, "")
  let l = solve(y)
  if l < ans:
    ans = l
echo "B: ", ans
