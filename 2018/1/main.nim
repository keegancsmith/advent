import strutils, sequtils, math, sets

let nums = readFile("input").splitWhitespace.map(parseInt)
echo "A: ", nums.sum

proc b(nums: seq[int]): int =
  var f = 0
  var seen: HashSet[int]
  seen.init
  while true:
    for d in nums:
      seen.incl(f)
      f += d
      if seen.contains(f):
        return f
echo "B: ", b(nums)
