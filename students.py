import csv

with open("vacancy.csv",encoding="utf8") as file:
    reader=csv.reader(file,delimiter=";")
    answer=list(reader)
"""читаем файл csv """

name=0
while name!="None":
    name = input()
    flag=False
    """идем по списку и выводим вакансии"""
    for salary, work_type,company_size,role, company in answer:
        if company == name:
            print("В", company ,"найдена вакансия: ",role, "З/п составит: ",salary)
            flag=True
    """если ничего не найдено выводим"""
    if flag==False:
        print("К сожалению, ничего не удалось найти")
