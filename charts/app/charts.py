import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title(f'Population Over the Years - {name}')
    plt.savefig('./imgs/' + name + '.png')
    plt.close()

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig('pie.png')
  plt.close()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 40, 800]
  generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)