import pandas as pd
import math


def load_data(path, features):
    """

    :param path:
    :param features:
    :return:
    """
    df = pd.read_csv(path)
    data = df.to_dict(orient="list")

    data["earnings"] = [math.log10(earning) for earning in data["earnings"]]
    data = dict(filter(lambda element: element[0] in features, data.items()))

    return data


def filter_by_features(data, feature, values):
    """
    returns two sets of data (represented by dictionaries) -
    one with values corresponding to entries where feature get values in the values set
    :param data: original data set
    :param feature: feature according to which we want to filter the data
    :param values: set of desired values from feature
    :return: two sets of data (represented by dictionary) - one
    """

    selectors = [value in values for value in data[feature]]
    complement_selectors = [not item for item in selectors]

    data_with_features = {key: filter_values(value, selectors) for key, value in data.items()}
    data_without_features = {key: filter_values(value, complement_selectors) for key, value in data.items()}

    return data_with_features, data_without_features


def filter_values(data: list, selectors: list) -> list:
    """
    filters elements from data returning only those that have a
     corresponding element in selectors that evaluates to True.
     (equivalent to itertools.compress)

    :param data: list of values
    :param selectors: list of booleans
    :return: data filtered by selectors
    """

    return [data for data, selectors in zip(data, selectors) if selectors]


def print_details(population, data, features, statistic_functions):
    """
    print the desired statistic summary for the data of the population
    :param population: name of desired population
    :param data: data pertaining only to the desired population
    :param features : features to which apply the statistical functions
    :param statistic_functions: list of statistic methods to present
    """

    print("{}:".format(population))
    for feature in features:
        print("{}:".format(feature.capitalize()), end=" ")
        summary_statistics = [func(data[feature]) for func in statistic_functions]
        print(*summary_statistics, sep=", ")


