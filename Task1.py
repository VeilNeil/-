"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def texts_count(Sum_list):
	Counts_sum = 0
	Counts_list = []
	for item in Sum_list:
		if item[0] not in Counts_list:
			Counts_list.append(item[0])
		if item[1] not in Counts_list:
			Counts_list.append(item[1])
	Counts_sum = len(Counts_list)
	return Counts_sum
Sum_list = texts + calls
print (texts_count(Sum_list))

"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."""
