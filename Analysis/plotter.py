import matplotlib.pyplot as plt

def grafict(y_raw,t):
    str_valor  = y_raw[0]
    y = y_raw[1:]
    
    # Dispersion graph
    plt.scatter(t, y, s=2)   # prueba con 10, 5 o 3
    
    # Labels
    plt.xlabel("Time")
    plt.ylabel(f"{str_valor} axis")
    plt.title(f"{str_valor}-t graph")

    plt.grid()
    plt.show()

def grafic(x_raw,y_raw):
    x_str_valor  = x_raw[0]
    y_str_valor  = y_raw[0]
    x = x_raw[1:]
    y = y_raw[1:]

    
    # Dispersion graph
    plt.scatter(x, y, s=2)   # prueba con 10, 5 o 3
    
    # Labels
    plt.xlabel(f"{x_str_valor}")
    plt.ylabel(f"{y_str_valor} axis")
    plt.title(f"{x_str_valor}-{y_str_valor} graph")

    plt.grid()
    plt.show()





def plotter(full_data):
    time_list = full_data[0][1:]
    store_full_data=full_data[1:]
    grafic((store_full_data[0]),(store_full_data[1]))
    for value_list in store_full_data:
        grafict(value_list, time_list)

