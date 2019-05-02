import numpy as np

filhos = list([0, 1, 2, 3, 5])
freq = [20, 5, 7, 3, 1]
perc = [55.56, 13.89, 19.44, 8.33, 2.78] 

w_mean = np.average(filhos, freq)

print(w_mean)




def weighted_avg_and_std(values, weights):
    """
    Return the weighted average and standard deviation.

    values, weights -- Numpy ndarrays with the same shape.
    """
    average = np.average(values, weights=weights)
    # Fast and numerically precise:
    variance = np.average((values-average)**2, weights=weights)
    return (average, math.sqrt(variance))