import matplotlib.pyplot as plt;
import seaborn as sns;
import plotly.express as px;
import plotly.graph_objects as go;
import pandas as pd;
import numpy as np;

t = np.linspace(0.0, 2.0, 200)

f1 = np.sin(np.pi * t)
f2 = np.sin(2 * np.pi * t)

plt.figure(figsize=(10, 10))

plt.plot(t, f1, linewidth=2.0, label='Seno de pi * t')
plt.plot(t, f2, linewidth=4.0, label='Seno de 2 * pi * t')

plt.legend()
plt.title('Senoides')

plt.grid(visible=True, color='gray', linestyle='--', linewidth=0.5)
plt.show()