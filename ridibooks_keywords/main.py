from tools import make_title_and_keywords_list
from save import save_to_file

title_and_keywords = []
title_and_keywords = make_title_and_keywords_list()
save_to_file(title_and_keywords)
print("completed")