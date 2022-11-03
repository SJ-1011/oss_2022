import numpy as np
import matplotlib.pyplot as plt
from sklearn import (datasets, svm, metrics)
from matplotlib.lines import Line2D # For the custom legend

def load_wdbc_data(filename):
    class WDBCData:
        data = []
        target = []
        target_names = ['malignant', 'benign']
        feature_names = ['mean radius', 'mean texture', 'mean perimeter', 'mean area', 'mean smoothness', 'mean compactness', 'mean concavity', 'mean concave points', 'mean symmetry', 'mean fractal dimension',
                         'radius error', 'texture error', 'perimeter error', 'area error', 'smoothness error', 'compactness error', 'concavity error', 'concave points error', 'symmetry error', 'fractal dimension error',
                         'worst radius', 'worst texture', 'worst perimeter', 'worst area', 'worst smoothness', 'worst compactness', 'worst concavity', 'worst concave points', 'worst symmetry', 'worst fractal dimension']
    wdbc = WDBCData()
    with open(filename) as f:
        for line in f.readlines():
            items = line.split(',')
            if (items[1] == 'M'):
                wdbc.target.append(0)
            else:
                wdbc.target.append(1)
            data = []
            for i in range(2, len(items)):
                data.append(float(items[i]))
            wdbc.data.append(data)
                
        wdbc.data = np.array(wdbc.data)
    return wdbc

if __name__ == '__main__':
    # Load a dataset
    # wdbc = datasets.load_breast_cancer()
    wdbc = load_wdbc_data('data/wdbc.data')

    # Train a model
    model = svm.LinearSVC()
    model.fit(wdbc.data, wdbc.target)
    

    # Test the model
    predict = model.predict(wdbc.data)
    n_correct = sum(predict == wdbc.target)
    accuracy = n_correct / len(wdbc.data)
    
    

    # TODO #3) Visualize the confusion matrix
    conf_mat = metrics.confusion_matrix(wdbc.target, predict)
    conf_dis = metrics.ConfusionMatrixDisplay(conf_mat, display_labels=['Malignant', 'Benign'])
    conf_dis.plot()
    

    # Visualize testing results
    cmap = np.array([(1, 0, 0), (0, 1, 0)])
    clabel = [Line2D([0], [0], marker='o', lw=0, label=wdbc.target_names[i], color=cmap[i]) for i in range(len(cmap))]
    for (x, y) in [(0, 1)]: # Not mandatory, but try [(i, i+1) for i in range(0, 30, 2)]
        plt.figure()
        plt.title(f'My Classifier ({n_correct}/{len(wdbc.data)}={accuracy:.3f})')
        plt.scatter(wdbc.data[:,x], wdbc.data[:,y], c=cmap[wdbc.target], edgecolors=cmap[predict])
        plt.xlabel(wdbc.feature_names[x])
        plt.ylabel(wdbc.feature_names[y])
        plt.legend(handles=clabel, framealpha=0.5)
    plt.show()
