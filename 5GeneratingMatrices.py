import numpy as np

a = np.array([1,2,3])
# b = array([4,5,6])


c = np.zeros(2)
print(c)

print("--"*114)

d = np.ones(2)
# d = np.threes(10)
print(d)

print("--"*114)

e = np.ones((2,2))
print(e)

print("--"*114)

f = np.zeros((2,2,2))
print(f)

print("--"*114)

g = np.zeros((2,3,3,3))
print(g)

print("--"*114)

i = np.random.random((10,10))
print(i)

print("--"*114)

j = np.random.randn(10)
print(j)

print("--"*114)

k = np.random.randn(10,10)
print(k)

print("--"*114)

print(j.mean())
print(j.var())