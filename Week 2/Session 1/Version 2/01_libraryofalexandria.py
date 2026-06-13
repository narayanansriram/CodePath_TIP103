
def analyze_library(library_catalog, actual_distribution):
    results = {}
    for k,v in library_catalog.items():
        results[k] = actual_distribution[k] - v
    return results

# Example Usage:

library_catalog = {
    "Room A": 150,
    "Room B": 200,
    "Room C": 250,
    "Room D": 300
}

actual_distribution = {
    "Room A": 150,
    "Room B": 190,
    "Room C": 260,
    "Room D": 300
}


print(analyze_library(library_catalog, actual_distribution))

# Example Output:

# {'Room A': 0, 'Room B': -10, 'Room C': 10, 'Room D': 0}
