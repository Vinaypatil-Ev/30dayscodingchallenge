import collections

def Anagrams(words, n):
    a = ord("a")
    d = collections.defaultdict(list)
    for word in words:
        no = 0
        for i in word:
            no |= (1 << (ord(i) - a))
        d[no].append(word)
    return [v for _, v in d.items()]


if __name__ == "__main__":
    n = input()
    words = input().split()
    ans = Anagrams(words, n)
    for grp in sorted(ans):
        for word in grp:
            print(word,end=' ')
        print()