import matplotlib.pyplot as plt
paternal_age=[30,35,40,45,50,55,60,65,70,75]
chd=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]

vs = dict(zip(paternal_age,chd))
print(vs)
#This method was taught by my friend Zhu Hengyu and he found this from https://blog.csdn.net/Kefenggewu_/article/details/123522854.
plt.scatter(paternal_age,chd,marker='o')
plt.xlabel('paternal_age')
plt.ylabel('chd')
plt.title('paternal_age vs chd')
#label the x and y axises
plt.show()
#determine the type of form (boxplot) and command it to draw
age = 30
#create a variable storing the input age
print(vs[age])
#print the risk of corresponding age using 'vs'
