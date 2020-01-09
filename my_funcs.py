from functools import reduce

def mse_with_variance_bias(variance, bias, variance_condition = None, bias_condition = None):
    """
    This function calculates mean squared error given the variance and bias in the estimate of a statistical learning method.
    
    The function expects two arguments - list of variances and list of bias. It optionally takes a condition for the bias
    or a condition for the variance
    """
    
    try:
        error_terms = []
        if variance_condition != None and bias_condition != None:
            return 'You can only set one of variance_condition and bias_condition'
        
        if variance_condition != None:
            variance = list(filter(lambda x: x <= variance_condition, variance))
            variance_indexes = [idx for idx, item in enumerate(variance) if item <= variance_condition]
            bias = [item for idx, item in enumerate(bias) if idx in variance_indexes]
            
        elif bias_condition != None:
            bias = list(filter(lambda x: x <= bias_condition, bias))
            bias_indexes = [idx for idx, item in enumerate(bias) if item <= bias_condition]
            variance = [item for idx, item in enumerate(variance) if idx in bias_indexes]
    
        for n in range(len(variance)):
            error_terms.append(n ** (1 / 3))
            
        squared_errors = reduce((lambda x, y: x + y), map(lambda x: x[0] + (x[1]) ** 2 + x[2], zip(variance, bias, error_terms)))
        mean_square_error = math.trunc(100 * (squared_errors / len(variance))) / 100
        result = 'Mean Square Errror: {}'.format(mean_square_error)
        return result
    
    except TypeError:
        return 'Ensure your input is of the appropriate type'




def mean_squared_error(estimated_output, output, condition):
    """
    This program takes in two lists and a condition. One list contains the estimated output for a set of N observations.
    while the other one contains the actual outputs for the observations. This function returns the mean squared error
    for all observations where the actual output is less than or equal to the user specified value. It also returns a 
    tuple of values for which the error is least.
    
    The function expects three arguments - two lists and one number
    """
    
    try:
        new_output = list(filter(lambda x: x <= condition, output))
        new_output_index = [idx for idx, item in enumerate(output) if item <= condition]
        new_estimated_output = [item for idx, item in enumerate(estimated_output) if idx in new_output_index]
    
    
        squared_errors = reduce((lambda x, y: x + y), map(lambda x: (x[0] - x[1]) ** 2, zip(new_estimated_output, new_output)))
        mean_square_error = math.trunc(100 * (squared_errors / len(new_output))) / 100
        result = 'Mean Square Errror: {}'.format(mean_square_error)
        return result
    
    except TypeError:
        return 'Ensure your input is of the appropriate type'