import numpy as np
import matplotlib.pyplot as plt
N = 8
marks=[45,36,86,57,53,92,65,45]
plt.boxplot(marks,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=False,
            showbox=True,
            showcaps=True,
            notch=False
                )
plt.show()
