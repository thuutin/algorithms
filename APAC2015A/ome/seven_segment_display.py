all = [
  "1111011", "1111111", "1110000", "1011111", "1011011", "0110011", "1111001", "1101101", "0110000", "1111110",
  "1111011", "1111111", "1110000", "1011111", "1011011", "0110011", "1111001", "1101101", "0110000", "1111110",
  "1111011", "1111111", "1110000", "1011111", "1011011", "0110011", "1111001", "1101101", "0110000", "1111110",
  "1111011", "1111111", "1110000", "1011111", "1011011", "0110011", "1111001", "1101101", "0110000", "1111110",
  "1111011", "1111111", "1110000", "1011111", "1011011", "0110011", "1111001", "1101101", "0110000", "1111110",
]


def matches(state, num, broken, workingFine):
  for i in xrange(len(state)):
    if i in broken:
      if state[i] == '1':
        return False
      continue

    if state[i] == '1' and num[i] == '0':
      return False
    if i in workingFine and num[i] == '1' and state[i] == '0':
      return False
  return True


def findBroken(state, num, broken):
  for i in xrange(len(state)):
    if state[i] == '0' and num[i] == '1':
      broken.add(i)
  pass


def findWorking(state, num, working):
  for i in xrange(len(state)):
    if state[i] == '1' and num[i] == '1':
      working.add(i)


def seven_segment(states, begin, beginInAll, broken, workingFine):
  # list of string
  now = states[begin]
  if matches(now, all[beginInAll], broken, workingFine):
    findBroken(now, all[beginInAll], broken)
    findWorking(now, all[beginInAll], workingFine)
    if begin == 9 or begin == len(states) - 1:
      if len(broken) + len(workingFine) < 7:
        missing = {0, 1, 2, 3, 4, 5, 6}
        for b in broken:
          missing.remove(b)
        for w in workingFine:
          missing.remove(w)
        for nn in xrange(7):
          if nn in missing and all[beginInAll + 1][nn] == '1':
            return True, 2
        return True, 1
      else:
        return True, 1
    else:
      return seven_segment(states, begin + 1, beginInAll + 1, broken, workingFine)

  return False, None


def seven_segment_display(states):
  res = None
  for i in xrange(10):
    br = set()
    re = seven_segment(states, 0, i, br, set())
    if re[0]:
      if re[1] > 1:
        return "ERROR!"
      lastNumber = list(all[i + len(states) % 10])
      for b in br:
        lastNumber[b] = '0'
      new = "".join(lastNumber)
      if res is None or new == res:
        res = new
      else:
        return "ERROR!"
  if res is not None:
    return "".join(res)
  else:
    return "ERROR!"


if __name__ == "__main__":
  T = input()
  for t in xrange(1, T + 1):
    arr = raw_input().split(" ")
    print "Case #" + str(t) + ": " + seven_segment_display(arr[1:])
