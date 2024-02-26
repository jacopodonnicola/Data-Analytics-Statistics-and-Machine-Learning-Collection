
# Z

def mean(l):
    m = sum(l)/len(l)
    return m


def variance(l):
    m = sum(l)/len(l)
    normalized = [(i - m) for i in l]
    normalized_square = [(i)**2 for i in normalized]
    variance = sum(normalized_square)/len(normalized_square)
    return variance


def std_dev(l):
    v = variance(l)
    std_dev = v**(1/2)
    return std_dev


def std_error(l,n):
    std_dev_pop = std_dev(l)
    std_dev_sample = std_dev_pop/((n)**(1/2))
    return std_dev_sample


def z_score(l,n,i):
    mean_pop = mean(l)
    std_dev_sample = std_error(l,n)
    return (i - mean_pop)/std_dev_sample


def confidence_interval(CI,l):

    mean_sample = mean(l)

    if CI == '95%':
        z_score = 1.96
    elif CI == '98%':
        z_score = 2.33
    elif CI == '99%':
        z_score = 2.57
    else:
        raise ValueError("Invalid confidence level. Supported values are '95%','98%' and '99%'.")

    std_error_sample = std_error(l)

    upper_bound = mean_sample + z_score * std_error_sample
    lower_bound = mean_sample - z_score * std_error_sample

    return (lower_bound, upper_bound)

# H0

def H0_2_tailed(l,n,i,alpha):

    z_score_sample = z_score(l,n,i)

    if alpha == '5%':
        z_critical = 1.96
    elif alpha == '2%':
        z_critical = 2.33
    elif alpha == '1%':
        z_critical = 2.57
    else:
        raise ValueError("Invalid alpha. Supported values are '5%','2%' and '1%'.")

    lower_bound = - z_critical
    upper_bound = z_critical

    if lower_bound < z_score_sample < upper_bound:
        print('H0 hypothesis is accepted')
    else:
        print('H0 hypothesis is rejeceted')

# T-Test

def variance_t_test(l):
    m = sum(l)/len(l)
    normalized = [(i - m) for i in l]
    normalized_square = [(i)**2 for i in normalized]
    variance = sum(normalized_square)/(len(normalized_square)-1) # Bessel's Correction
    return variance


def std_dev_t_test(l):
    variance = variance_t_test(l)
    std_dev = variance **(1/2)
    return std_dev


def std_error_t_test(l,n):
    std_dev_sample = std_dev_t_test(l)
    std_error_t_test = std_dev_sample/((n)**(1/2))
    return std_error_t_test


def t_test(l,n,mean_H0):
    mean_sample = mean(l)
    std_error_sample = std_error_t_test(l,n)
    return (mean_sample - mean_H0)/std_error_sample


def t_test_dependent_samples(l,n):
    mean_difference = mean(l)
    std_error_sample = std_error_t_test(l,n)
    return (mean_difference)/std_error_sample
