import numpy as np


pm = [1,2,3]
am = np.array([1,2,3])


exec("print('----------------------------------------------------------------------------'*3)")


print(pm)
for i in pm:
    print(i)

print(am)
for i in am:
    print(i)


exec("print('----------------------------------------------------------------------------'*3)")


pm.append(4)
print(pm)

# am.append(4)
print(am)


exec("print('----------------------------------------------------------------------------'*3)")


pm = pm + [5]
print(pm)

# am = am + [4,5]
print(am)


exec("print('----------------------------------------------------------------------------'*3)")


km = []
for i in pm:
    km.append(i  + i)
print(km)

print(am + am)

print(pm + pm)


exec("print('----------------------------------------------------------------------------'*3)")


print(2*pm)

print(2*am)

exec("print('----------------------------------------------------------------------------'*3)")


# print(pm**2)
km = []
for i in pm:
    km.append(i*i)
print(km)

print(am**2)


exec("print('----------------------------------------------------------------------------'*3)")


print(np.sqrt(am))

print(np.log(am))

print(np.exp(am))
