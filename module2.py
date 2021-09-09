import json


def function(DataSet):
    """This function takes input a list of dictionaries and filters out
    countries and population of Asean countries in the year 2014.

    Args:
        DataSet [list[dict]]: list of dictionaries where every
        element of the list is a record of country's population corresponding
        to the respective year
    """
    asean = ["Brunei Darussalam", "Cambodia", "Indonesia", "Laos", "Malaysia",
             "Myanmar", "Philippines", "Singapore", "Thailand",
             "Vietnam"]
    records = {}
    for entry in DataSet:
        if (entry['Year'] == '2014') and (entry['Region'] in asean):
            records[entry['Region']] = entry['Population']
    out_file = open("./myfile2.json", 'w')
    json.dump(records, out_file, indent=2)
    out_file.close()
