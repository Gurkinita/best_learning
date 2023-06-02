# требует доработки. не смотреть пока


# import csv
# from datetime import date
#
# with open('/home/julia/Downloads/test_file.csv', 'r') as hrivna, open('salaries_uah.csv', 'w', newline='') as dollar:
#     input_reader = csv.reader(hrivna)
#     output_writer = csv.writer(dollar)
#
#     today = date.today()
#
#     for row in input_reader:
#         try:
#             salary_usd = float(row[2])
#             exchange_rate = 37.5
#             salary_uah = salary_usd * exchange_rate
#             output_writer.writerow([today, salary_uah])
#         except ValueError:
#
#             continue
#
# dollar.close()
# hrivna.close()
