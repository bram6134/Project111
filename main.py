import plotly.figure_factory as figure_factory
import plotly.graph_objects as graph_objects
import statistics
import random
import pandas
import csv

df = pandas.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

population_mean = statistics.mean(data)

#fig = figure_factory.create_distplot([data], ['reading_time'], show_hist=False)
#fig.show()

def random_sets_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

print("Population mean is ", population_mean)

def plot_graph(mean_list):
    df = mean_list
    fig = figure_factory.create_distplot([df], ["reading_time"], show_hist=False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0, 100):
        set_of_means = random_sets_of_mean((30))
        mean_list.append(set_of_means)
    plot_graph(mean_list)

    mean = statistics.mean(mean_list)
    print("Mean of samples is ", mean)

setup()

def standard_deviation(counter):
    mean_list = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        mean_list.append(value)
    standard_dev = statistics.stdev(mean_list)
    print("Standard Deviation is ", standard_dev)

standard_deviation(30)
