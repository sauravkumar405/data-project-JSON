import json


def function(DataSet):
    """This function takes input a list of dictionaries and filters out
    population of India over years."

    Args:
        DataSet (list[dict]): list of dictionaries where every
        element of the list is a record of country's population corresponding
        to the respective year.
    """
    records = {}
    # Iterating through the DataSet entry
    for entry in DataSet:
        if entry['Region'] == "India":
            records[entry['Year']] = float(entry['Population'])
    out_file = open("./myfile1.json", "w")
    json.dump(records, out_file, indent=2)
    out_file.close()
