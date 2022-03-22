import csv

def save_to_file(title_and_keywords):
  file = open("title_and_keywords.csv", mode="w", encoding = "utf-8-sig")
  writer = csv.writer(file)
  writer.writerow(["제목","키워드"])
  for one in title_and_keywords :
    value_list = []
    title_value = []
    title_value.append(one.get('title'))
    keywords_value = one.get('keywords')
    value_list = title_value + keywords_value
    writer.writerow(value_list)
  return