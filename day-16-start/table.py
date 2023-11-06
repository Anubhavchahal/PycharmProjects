from prettytable import PrettyTable

# Specify the Column Names while initializing the Table
myTable = PrettyTable()
myTable.add_column("pokemon name",["pikachu","squirtle", "charmander"])
myTable.add_column("type",["electric", "water", "fire"])
print(myTable)


