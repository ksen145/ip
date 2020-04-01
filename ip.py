import ipaddress

def sort(mas):

    if len(mas) < 2:
        return mas[:]

    else:
        middle = int(len(mas)/2)
        left = sort(mas[:middle])
        right = sort(mas[middle:])
        return merge(left, right)

def merge(left, right):

    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result

a = ['192.168.0.1', '192.168.0.5' , '192.168.3.4', '192.167.0.143']
m = []
for i in range(len(a)):
    m.append(int(ipaddress.IPv4Address(a[i])))
print(m)
k = 0
d = str(m[0])
o = []
for i in range(len(a)):
    f = str(m[i])
    h = ''
    for j in range(len(f)):
        if (f[j] == d[j]):
            h = h + f[j]
    o.append(h)

print(o)
o = sort(o)
print(o[0])
print(ipaddress.IPv4Address(int(o[0])))
