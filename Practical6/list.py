import numpy as np
import matplotlib.pyplot as plt
#import the used libraries
marks=[45,36,86,57,53,92,65,45]
marks.sort()
print(marks)
#print the marks in a order
plt.boxplot(marks,
            vert=True,
            whis=1.5,widths=0.8,
            meanline=False,
            patch_artist=True,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch= False,labels=None,)
plt.show()
#draw the boxplot
n=0
for i in range(len(marks)):
    n += 1
sum=0
for i in marks:
    sum += i
mean=sum/n
if mean > 60:
    print("pass")
else:
    print("fail")
print(np.average(marks))
#use numpy output the average of marks

