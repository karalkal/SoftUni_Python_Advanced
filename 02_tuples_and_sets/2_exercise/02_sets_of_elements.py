(n_len, m_len) = input().split()

n_set = set()
m_set = set()

for n in range(int(n_len)):
    n_set.add(int(input()))

for m in range(int(m_len)):
    m_set.add(int(input()))

result = n_set.intersection(m_set)
print(*result, sep="\n")

