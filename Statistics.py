from Data import filter_values, print_details


def sum(values):
    """
    :param values:
    :return: sum of listed values
    """

    total = 0
    for value in values:
        total += value

    return total


def mean(values):
    """
    :param values:
    :return: mean of the listed values
    """
    return float(sum(values))/len(values)


def median(values):
    """
    :param values:
    :return: median of the listed values
    """

    sorted_values = sorted(values)
    median_index = int(len(values) / 2)

    # computation of the median depends on the parity of the sample size
    if len(values) % 2 == 1:
        return sorted_values[median_index]

    return (sorted_values[median_index-1]+sorted_values[median_index]) * 0.5


def population_statistics(population, data, feature_1, feature_2, min_val, max_val, statistics_functions):
    """
    prints summary statistics for one feature according to another feature range
    :param population:
    :param data:
    :param feature_1:
    :param feature_2:
    :param min_val:
    :param max_val:
    :param statistics_functions:
    """

    # creating a boolean list indicating if entry has values in the desired range of feature 1
    selectors = list(map(lambda val: min_val <= val <= max_val, data[feature_1]))

    # filtering feature 2 entries by the selectors list
    filtered_feature_2 = {feature_2: filter_values(data[feature_2], selectors)}

    print_details(population, filtered_feature_2, [feature_2], statistics_functions)
