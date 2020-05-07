import numpy as np

A = np.array([[1,2],[3,4]])
print(A)
A_inv = np.linalg.inv(A)
print(A_inv)
print(A_inv.dot(A))
print(A.dot(A_inv))


print("--"*114)


A_determinant = np.linalg.det(A)
print(A_determinant)

print(np.diag(A))  #diagonal element
print(np.diag([1,2]))
print(np.diag([1,2,3]))


print("--"*114)


a = np.array([1,2])
b = np.array([3,4])
print(np.outer(a,b)) #outer product
print(np.inner(a,b)) #inner product, it is same as dot product
print(a.dot(b))


print("--"*114)


print(np.trace(A))  #Matrix trace, it gives sum of diagonal of matrix
print(np.diag(A).sum())


print("--"*114)


X = np.random.randn(100,3)
print(X)

co_variance = np.cov(X)
print(co_variance)
print(co_variance.shape) #Shape must be 3*3 because data is 3 dimension
cov = np.cov(X.T)
print(cov)


print("--"*114)


print(np.linalg.eigh(cov))
print(np.linalg.eig(cov))