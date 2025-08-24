
# POINTS : 3 FOR VICTORY AND 1 FOR TIE

matches = [
    {"rival": "Equipo A", "goles_favor": 2, "goles_contra": 1},
    {"rival": "Equipo B", "goles_favor": 0, "goles_contra": 3},
    {"rival": "Equipo C", "goles_favor": 4, "goles_contra": 2},
    {"rival": "Equipo D", "goles_favor": 1, "goles_contra": 1}
] # 3 + 0 + 3 + 1 = 7 // points = 7

def calculate_points(matches):
    points = 0    
    for team in matches:
        cal = team["goles_favor"] - team["goles_contra"]

        if cal > 0 :
            points += 3
        elif cal == 0:
            points += 1

    return points

# TOTAL_POINTS AND BEST_SCORE from Base de Datos 2 work
def total_points(matches):
    
    goals_for = sum(match["goles_favor"] for match in matches)
    goals_against = sum(match["goles_contra"] for match in matches)

    return {"Goles a favor ": goals_for, "Goles en contra": goals_against}

def best_score(matches):
    best_match = max(matches, key=lambda x: x["goles_favor"] - x["goles_contra"])
    return best_match

print(calculate_points(matches))
print(total_points(matches))
print(best_score(matches))