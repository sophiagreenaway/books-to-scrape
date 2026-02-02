import csv

#EXPORT DATA TO CSV
def export_to_csv(filename, data):
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=data[0].keys()
        )
        writer.writeheader()
        writer.writerows(data)