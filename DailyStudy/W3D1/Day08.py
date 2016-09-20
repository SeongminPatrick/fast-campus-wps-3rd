# _*_ coding: utf-8 _*_

""" csv 파일 리더 제작 """

# with open("./students.csv", "r") as fp:
# 	data = fp.read()
# 	rows = data.split("\n")
# 	columns = rows[0].split(",")
# 	students = []
#
# 	for row in rows[1:4]:
# 		fields = row.split(",")
#
# 		student = {}
#
# 		for index in range(len(columns)):
# 			field = fields[index]
# 			column = columns[index]
# 			student[column] = field
# 			students.append(student)
#
# 	print students

""" 함수로 개선 """

# def read_csv(filename, sep=","):
# 	with open(filename, "r") as fp:
# 		data = fp.read()
# 		rows = data.split("\n")
# 		students = []
# 		columns = rows[0].split(sep)
#
# 		for row in rows[1:4]:
# 			fields = row.split(sep)
# 			student = {}
# 			for index in range(len(columns)):
# 				field = fields[index]
# 				column = columns[index]
# 				student[column] = field
# 				students.append(student)
# 		print students
#
# read_csv("./students.csv", ",")


""" sep 종류 가리지 않고 read """

def read_csv(filename, sep=","):
	with open(filename, "r") as fp:
		data = fp.read()
		rows = data.split('\n')
		columns = rows[0].split(sep)
		contents = []

		for row in rows[1:4]:
			fields = row.split(sep)
			content ={}

			for index in range(len(columns)):
				field = fields[index]
				column = columns[index]
				content[column] = field
				contents.append(content)
		return contents

# def read_tsv(filename):
	# return read_csv(filename, sep="\t")

""" lambda로 개선 """

read_tsv = lambda filename: read_csv(filename, sep="\\t")
read_lsv = lambda filename: read_csv(filename, sep="|")

print read_tsv("./students.tsv")

""" 무적 함수 """

# seps = [",", ".", "::", "^"]
# reader = {}
# for sep in seps:
#     reader[sep] = lambda filename: read_csv(filename, sep) # dict 로 reader 함수 작성
#
# print reader[","]("./students.csv") # "," key 를 넣으면 lambda 가 value로 리턴

# print read_csv("./students.tsv", "::")
