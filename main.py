import sys
from Data import load_data, print_details, filter_by_features
import Statistics


def men_vs_women(data):
    """
    print summary statistic divided by men, women and whole population
    :param data:
    :return: None
    """

    print('Question 1:')
    order_of_print = ['Men', 'Women', 'All']

    women_data, men_data = filter_by_features(data, 'female', {1})

    population_to_data = {'Men': men_data, 'Women': women_data, 'All': data}
    features = ['age', 'earnings', 'hours', 'week']
    statistic_functions = [Statistics.sum, Statistics.mean, Statistics.median]

    for item in order_of_print:
        print_details(item, population_to_data[item], features, statistic_functions)

    print()


def married_women_vs_unmarried(data):
    """
    print summary statistics of  earnings by married women vs. unmarried women
    :param data:
    :return: None
    """

    women_data = filter_by_features(data, 'female', {1})[0]

    married_women_data, unmarried_women_data = filter_by_features(women_data, 'marital', {1, 2, 3})
    population_to_data = {'Married Women': married_women_data, 'Unmarried Women': unmarried_women_data}

    statistic_functions = [Statistics.mean, Statistics.median]

    education_scopes = [(0, 10), (11, 20)]

    order_of_print = ['Married Women', 'Unmarried Women']

    print('Question 2:')
    for scope in education_scopes:
        print("If {0}<=Y<={1}, then:".format(scope[0], scope[1]))
        for population in order_of_print:
            Statistics.population_statistics(population, population_to_data[population], 'education', 'earnings',
                                             scope[0], scope[1], statistic_functions)


def main(argv):

    path = argv[1]
    features = argv[2]

    data = load_data(path, features)

    men_vs_women(data)
    married_women_vs_unmarried(data)


if __name__ == "__main__":
    main(sys.argv)