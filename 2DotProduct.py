import numpy as np

a = np.array([1,2])
b = np.array([2,1])
dot = 0
for i, j in zip(a,b):
    dot += i*j
print(dot)
print(a*b)
print(np.sum(a*b))
print((a*b).sum())
print(np.dot(a,b))

print("--"*114)

print(a.dot(b))
print(b.dot(a))

print("--"*114)

a_mag  = np.sqrt((a*a).sum())
print(a_mag)
a_mag = np.linalg.norm(a)
print(a_mag)

print("--"*114)

cosangle = a.dot(b/(np.linalg.norm(a) * np.linalg.norm(b)))
print(cosangle)
angle = np.cos(cosangle)
print(angle)