from tabulate import tabulate
data =[["Name","Place","Gender","Age"],["khalid","peshawar","Male","22"],["Ali","Kabul","Male","25"],["sarah","peshawar","female","20"],["sarmad","peshawar","Male","22"]]
print(tabulate(data,headers='firstrow',tablefmt='fancy_grid'))
