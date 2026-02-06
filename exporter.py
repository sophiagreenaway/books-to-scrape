import csv

#EXPORT DATA TO CSV
def export_to_csv(filename, data):
    if not data:
        return
    
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)