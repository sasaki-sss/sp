import sys

argc = len(sys.argv)
if argc == 1:
     f = sys.stdin
elif argc == 2:
     try:
          f = open(sys.argv[1], "r")
     except FileNotFoundError:
          sys.exit("ファイルが存在しません: " + sys.argv[1])
          sys.exit()

s = f.read()
s = s.lower()
s = s.replace(',','')
s = s.replace('.','')
s = s.replace('_','')
s = s.replace(';','')
s = s.replace(':','')
s = s.replace('"','')
s = s.replace("'",'')
s = s.replace('(','')
s = s.replace(')','')
s = s.replace('/','')
words = s.split()

freqs = {}
for w in words:
    w = w.lower()
    if w in freqs:
        freqs[w] += 1
    else:
        freqs[w] = 1

sorted_freqs = sorted(freqs.items(), key=lambda x: x[1], reverse=True)

i = 0
for (k, v) in sorted_freqs:
    if i == 20:
        break
    print(" {}: {}".format(k, v))
    i += 1
