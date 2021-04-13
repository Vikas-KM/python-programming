import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
# % matplotlib inline

from sklearn import datasets
from sklearn import manifold


X, y = datasets.fetch_openml('mnist_784', version=1, return_X_y=True)
print('Single Value of X[0]: ',X[0])
print('Single Values of y[0]: ',y[0])
print('Type of X values: ',type(X[0]))
print('Type of y values :',type(y[0]))

# the y values are in string format
y = y.astype(int)
print('type of y values: ',type(y[0]))

# shapes of the values
print(X[0].shape)

# 28*28 = 784
single_image = X[0].reshape(28,28)
plt.imshow(single_image, cmap='gray')
plt.show()

tsne = manifold.TSNE(n_components=2, random_state=42)
transformed_data = tsne.fit_transform(X[:3000])

tsne_df = pd.DataFrame(
    np.column_stack((transformed_data, y[:3000])),
    columns=['x','y','targets']
)
# tsne_df.loc[:, 'targets'] = tsne_df.y.astype(int)
print(tsne_df.head(10))

