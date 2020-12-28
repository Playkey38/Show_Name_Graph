import matplotlib.pyplot as plt

def show_name_graph():
    xs = []
    ys = []
    with open("names.csv" , "r") as file:
        #Get's user input
        name = input("Which name do you wanna search after? ")
        state  = input("Which state (use the Abbreviaton)? ")
        gender = input("Which gender? ")
        if gender.lower() == "male":
            gender = 'M'
        else:
            gender = 'F'
        start_year = int(input("From which year? "))
        end_year = int(input("Till which year? "))
        #Goes through each line and compares
        for line in file:
            t = line.strip().split(",")
            if t[0] == "Id":
                continue
            if start_year <= int(t[2]) <= end_year and t[1] == name and t[3] == gender and t[4] == state:
                # appends the counting numbers and the year to the axes
                xs.append(int(t[2]))
                ys.append(int(t[5]))

        plt.plot(xs, ys)
        plt.show()
        print("Thanks for trying out!")

show_name_graph()