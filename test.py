import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-2*np.pi, 2*np.pi, 1000)
y = np.sin(x) + 1
plt.plot(x,y,color='limegreen', label = '1 + f_1') #그래프그리기
'''
x = np.linspace(-2,2,1000)
y = np.full((1000),1/2)
for j in range(1,50):
    y += 2*(np.sin(j*np.pi/2)/j*np.cos(j*np.pi*x))/np.pi
plt.plot(x,y,color='violet',label = 'F_series')
'''

#축, 중심선, 좌표표시 등
#plt.plot(np.pi,0,'bo') # 점찍기
#plt.plot(0,np.pi,'bo')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.axis([-2*np.pi,2*np.pi,-2,2]) #그래프 범위
plt.hlines(0, -2*np.pi, 2*np.pi, color='black', linestyle='solid', linewidth=2) # x축
plt.vlines(0, -2*np.pi, 2*np.pi, color='black', linestyle='solid', linewidth=2) # y축

# 수직선,수평선(점선)
#plt.axhline(0.0378,0,1,color='gray',linestyle='--')
#plt.axvline(np.pi, 0, 1, color='gray', linestyle='--') #수직선 : (x좌표, 0:그래프 맨 아래, 1:그래프 맨 위, 색깔, 선 모양)


#실행
plt.legend() # 함수 범례 (함수 이름 표시해주는거)
plt.show()