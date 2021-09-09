
import json


def function(DataSet):
    """This function takes input a list of dictionaries and filters out
    population of SAARC Countries over years."

    Args:
        DataSet [list[dict]]: list of dictionaries where every
        element of the list is a record of country's population corresponding
        to the respective year
    """
    saarc = ["Afghanistan", "Bangladesh", "Bhutan", "India", "Maldives",
             "Nepal", "Sri Lanka", "Pakistan"]

    # creating a hashmap to track total population count of each year
    years_hashmap: dict[str:float] = {}
    # Iterating through the dataset
    for entry in DataSet:
        if entry['Region'] in saarc:
            if entry['Year'] in years_hashmap.keys():
                years_hashmap[entry['Year']] += float(entry['Population'])
            else:
                years_hashmap[entry['Year']] = float(entry['Population'])
    out_file = open("./myfile3.json", "w")
    json.dump(years_hashmap, out_file, indent=2)
    out_file.close()
