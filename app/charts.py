import matplotlib.pyplot as plt

def generate_bar_chat(name, labels, values):

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    # plt.show()
    plt.savefig(f'./imgs/{name}.png')
    plt.close()

def generate_pie_chat(labels, values):

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    # plt.show()
    plt.savefig('chart_pie_cambio.png')
    plt.close()

if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [100,200,300]
    generate_bar_chat(labels,values)
    generate_pie_chat(labels,values)

