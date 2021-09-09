from csv import DictReader
import module1
import module2
import module3
import module4


def fetchdata():
    file_handle = open("/home/saurabh/Desktop/project/data-project-javascript/DataSet/data.csv", "r")
    DataSet = DictReader(file_handle)
    return DataSet


if __name__ == '__main__':

    print("Enter 1 to view Population of India over Years")
    print("Enter 2 to view Bar Chart of population of ASEAN countries")
    print("Enter 3 to view BAR Chart of Total SAARC countries population vs \
        years")
    print("Enter 4 to view Grouped Bar Chart of ASEAN countries population \
        vs years")
    print("Enter 0 to exit")

    while(True):
        choice = int(input("Enter your choice "))
        DataSet = fetchdata()
        if choice == 1:
            module1.function(DataSet)
        elif choice == 2:
            module2.function(DataSet)
        elif choice == 3:
            module3.function(DataSet)
        elif choice == 4:
            module4.function(DataSet)
        else:
            break
