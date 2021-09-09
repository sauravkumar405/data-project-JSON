import json


def function(DataSet):
    """This function takes input parameter as a list of dictionaries and
    filters out population of ASEAN Countries over years between 2004 and
    2014."

    Args:
        DataSet [list[dict]]: list of dictionaries where every
        element of the list is a record of country's population corresponding
        to the respective year
    """
    asean = ["Brunei Darussalam", "Cambodia", "Indonesia", "Laos", "Malaysia",
             "Myanmar", "Philippines", "Singapore", "Thailand", "Vietnam"]
    # Creating an empty dictionary to keep track of each years population data
    years_hashmap = {}
    for countries in asean:
        years_hashmap[countries] = {}
    # Iterating through the Dataset
    for entry in DataSet:
        if '2004' <= entry['Year'] <= '2014' and entry['Region'] in asean:
            if entry['Region'] in years_hashmap.keys():
                years_hashmap[entry['Region']][entry['Year']] = float(entry['Population'])
            else:
                years_hashmap[entry['Region']] = [float(entry['Population'])]
    out_file = open("/home/saurabh/Desktop/project/data-project-javascript/myfile4.json", "w")
    json.dump(years_hashmap, out_file, indent=2)
    out_file.close()
