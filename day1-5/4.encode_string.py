def encode_str(arr):
    ans = ""
    i = 0
    while i < len(arr):
        l = arr[i]
        count = 1
        i += 1
        while i < len(arr) and l == arr[i]:
            i += 1
            count += 1
        ans += "{0}{1}".format(l, count)
    return ans

if __name__=='__main__':
    arr = input().strip()
    print(encode_str(arr))
