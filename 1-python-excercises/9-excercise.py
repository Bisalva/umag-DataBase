import statistics

temps = {
    "Santiago": [22, 25, 28, 26, 24, 20, 18, 21, 23, 27],
    "Valparaíso": [18, 20, 22, 21, 19, 17, 16, 18, 20, 23]
}
temp_average = {}
temp_variety = {}


def compare_temps(temps):

    for City, temps in temps.items():
        temp_average[City] = sum(temps)/len(temps)
        temp_variety[City] = statistics.stdev(temps)

    city_average = max(temp_average.items(), key=lambda x: x[1])[0]
    city_variety = max(temp_variety.items(), key=lambda x: x[1])[0]
    
    return {"Ciudad con mayor promedio": city_average, 
            "Ciudad con mayor diversidad " : city_variety
            }


print(compare_temps(temps))