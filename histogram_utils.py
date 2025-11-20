# Q: Write an import statement that imports the function pyplot from the module matplotlib and renames it to plt.
import matplotlib.pyplot as plt
def build_histogram(data):
  my_dict = {}
  for item in data:
    if item in my_dict.keys():
      my_dict[item] += 1
    else:
      my_dict.update({item:1})
  return my_dict

def plot_histogram(histogram):
    x_values = list(histogram.keys())
    y_values = list(histogram.values())

    plt.bar(x_values, y_values)
    plt.xlabel('Items')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.show()


