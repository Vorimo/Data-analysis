import numpy
import matplotlib.pyplot as plt


def plot_df(data, columns_to_show: list, x_label: str, y_label: str,
            title: str, label: str):
    for column_to_show in columns_to_show:
        plt.plot(numpy.array(data[column_to_show].tolist()), label=label)
    # show x,y labels
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    # show title
    plt.title(title)
    # show legend
    plt.legend()


def plot_chart_df(x_series, y_series, x_label: str, y_label: str):
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.figure(figsize=(25, 27), dpi=60)
    plt.xticks(rotation='vertical')
    plt.bar(x_series, y_series)


def save_plot_and_show(file_name: str):
    plt.savefig(file_name)
    plt.show()
