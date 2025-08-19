
names = ["ana maría", "CARLOS PÉREZ", "  luis  ", "María José"]

def clear_names(names):

    new_names_count = 0
    for i in range(len(names)):
        slices = names[i].strip().split()
        slices = [s.capitalize() for s in slices]

        if len(slices) > 1:
            names[i] = "".join(slices)
            new_names_count += 1
    
    print("Nwe names list : ", names)
    print("Names with spaces changed : ", new_names_count)
    
print("Names : ",names)
clear_names(names)