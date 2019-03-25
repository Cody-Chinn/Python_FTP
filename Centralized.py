import os

dict_list = []

def file_obj(speed, hostname, filename):

	global dict_list

	new_entry = {
		"speed" : speed,
		"hostname" : hostname,
		"filename" : filename
	}

	dict_list.append(new_entry)

spd = input("What is your internet speed? ")
hstnm = input("What is your hostname or IP? ")
flnm = input("What is the name of your file? ")
file_obj(spd, hstnm, flnm)

print(dict_list)
