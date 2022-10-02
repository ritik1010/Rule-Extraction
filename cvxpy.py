Galpha=np.zeros(m)
Halpha=np.zeros(m)
self.m=m
X=np.array(X_train)
k=self.k_mat(X)
self.a = cp.Variable(m)
self.C = cp.Parameter(nonneg=True)
self.C.value = 0.02
deltamat=np.zeros((m,m))
for i in range (m):
    for j in range(m):
        if i==j:
            deltamat[i][j]=(1/self.C.value)**1
        else:
                deltamat[i][j]=1
res=0
cres=0
for i in range(m):
    res+= self.a[i]+ \
    self.a[i]*y[i]*( cp.sum(cp.multiply(cp.multiply(self.a,y),k[i]))+ cp.sum(cp.multiply(cp.multiply(self.a,y),deltamat[i])))
    cres=(Z[i]-np.mean(Z))*cp.sum(cp.multiply(cp.multiply(self.a,y),k[i]))
objective=cp.Minimize(res)
constraints=[cp.sum(cp.multiply(self.a,y))==0 , cres>= (-1)*self.C*m, cres <=self.C*m ]
prob=cp.Problem(objective,constraints)
print("is dcp:",prob.is_dcp())
