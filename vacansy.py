import csv

with open("vacancy.csv",encoding="utf8") as file:
    reader=csv.reader(file,delimiter=";")
    answer=list(reader)


with open("vacancy_new.csv","w",newline="") as file2:
    writer=csv.writer(file2)

    for salary, work_type,company_size, role, company in answer:
        writer.writerow([str(salary),role, company])


