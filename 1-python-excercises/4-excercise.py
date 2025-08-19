

def show_details(limit,stop_in):
    print("The limit is : ", limit , "\nStops in : ", stop_in)

def count_to(limit,stop_in):

    show_details(limit,stop_in)

    for count in range(1,limit+1):
        print(count)
        if(stop_in == count):
            break


count_to(10,5)
