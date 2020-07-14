'''
Menghitung Stress - Strain dan Hubungan Fisis dengan Parameter Lame
2D Problem Sederhana
mifta, 2020

referensi:
Shearer, Peter M. Introduction to Seismology, second edition (2009)
'''

import numpy as np
from numpy import linalg as la

#Input
sdt=45 #orientasi patahan terhadap sumbu X
tau=np.array([[-4,-10],[-10,-60]]);print('Stress Matrix \n',tau) #stress matrix
vp=6 #kecepatan P
vs=vp/np.sqrt(3) #Kecepatan S
rho=2.7

#Fungsi
def Young(lamb,miu):
	y=(3*lamb+2*miu)*miu/(lamb + miu)
	return y
	
def Bulk(lamb,miu):
	k=lamb+2/3*miu
	return k
	
def Poisson(lamb,miu):
	p=lamb/2*(lamb+miu)
	return p

def Lamb(vp,vs,rho):
	l=rho*(vp**2 - 2*vs**2)
	return l

def Miu(vs,rho):
	m=(vs**2)*rho
	return m


n=np.array([np.sin(np.pi*sdt/180), np.cos(np.pi*sdt/180)]) #unit vektor tegal lurus
f=np.array([np.sin(np.pi*sdt/180), -np.cos(np.pi*sdt/180)]) #unit vektor paralel patahan
trac=np.dot(tau,n);print(trac)

#normal stress
tauN=np.dot(trac,n);print('Normal Stress \n',tauN)
tauS=np.dot(trac,f);print('Shear Stress \n',tauS)

#eigenvalue dan eigenvektor
w,v=la.eig(tau)
print('eigen value \n',w)
print('eigen vektor \n',v)

'''
#Menghitung Strain
e=np.zeros([2,2])
print(e)



m=Miu(vs,rho)
l=Lamb(vp,vs,rho)
e[0,1]=tau[0,1]/m;e[1,0]=e[0,1]
e[1,1]=(tau[1,1]-l*((tau[0,0]-tau[1,1])/2*m))/(2*l + 2*m)
e[0,0]=(tau[0,0]-tau[1,1])/2*m + e[1,1]

print(e)

'''
	
