import matplotlib.pyplot as plt

def grafic(y_raw,t):
    str_valor  = y_raw[0]
    y=y_raw[1:]
    # Disperssion graph
    plt.scatter(t, y)
    # Lables
    plt.xlabel("Time")
    plt.ylabel(f"{str_valor} axis ")
    plt.title(f"{str_valor}-t graph")

    plt.grid()
    plt.show()

def plotter (full_data):
    time_list = full_data[0][1:]
    for value_list in full_data[1:]:
        grafic(value_list,time_list)



