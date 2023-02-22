import pandas as pd
import matplotlib.pyplot as plt

data = {"Колличество кликов":[100,135,220, 300,],
"Количество показов":[678,1100,2450,2730],
"CTR %":[1474926254,1227272727,8979591837,1098901099]}
frame = pd.DataFrame(data)
print(frame['CTR %'])

plt.plot([678,1100,2450,2730],[100,135,220,300])
plt.show()