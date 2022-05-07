main_units=["Length Converter","Data Storage Converter","Temperature Converter"]
cntr=0
choice=0
length_units=["mm","cm","dm","m","dam","hm","km"]
byte_units=["b","kb","mb","gb","tb","pb"]
temp_units=['c','f','k']
result_list=list()
while True:
	
	try:
		if choice==0:
			for i in main_units:
				cntr+=1
				print(cntr,"-",i,"|",end=" ")
				if cntr==len(main_units):
					print(cntr+1,"-","Exit")
					cntr=0

			choice=int(input("Please select the operation perform by typing number: "))

		if choice==1:
			print("-"*3,"",main_units[choice-1],"","-"*3)
			first_val,second_val,third_val=float(input("Value: ")),input("From= "),str(input("To= "))	
			for j in range(len(length_units)):
				if length_units.index(second_val.lower())>length_units.index(third_val.lower()):#to go up or down in the "length_units" array 
					result_list.append(first_val*(10**j))
					if len(result_list)==len(length_units):#"if" is used to understand the end of the array
						final_result=result_list[length_units.index(second_val.lower())-length_units.index(third_val.lower())] #Finding the answer in return_list
						result_list.clear()
				elif length_units.index(second_val.lower())==length_units.index(third_val.lower()):
					final_result=first_val
				else:
					result_list.append(first_val/(10**j))
					if len(result_list)==len(length_units):
						final_result=result_list[length_units.index(third_val.lower())-length_units.index(second_val.lower())]
						result_list.clear()
			
			print("{0}{1} to {2}= {3:.6f}".format(first_val,second_val.lower(),third_val.lower(),final_result).rstrip("0"))

			choice=input("Do you want to make new {}? - Y/N: ".format(main_units[choice-1]))
			if choice.lower()=='y':
				choice=1
			else:
				choice=0
		
		elif choice==2:
			print("-"*3,"",main_units[choice-1],"","-"*3)
			first_val,second_val,third_val=float(input("Value: ")),input("From= "),str(input("To= "))
			second_val=second_val.lower()
			third_val=third_val.lower()

			for k in range(len(byte_units)):
				if byte_units.index(second_val)>byte_units.index(third_val):
					result_list.append(first_val*(2**(10*k)))
					if len(result_list)==len(byte_units):
						final_result=result_list[byte_units.index(second_val)-byte_units.index(third_val)]
						result_list.clear()
				elif byte_units.index(second_val)==byte_units.index(third_val):
					final_result=first_val
				else:
					result_list.append(first_val/(2**(10*k)))
					if len(result_list)==len(byte_units):
						final_result=result_list[byte_units.index(third_val)-byte_units.index(second_val)]
						result_list.clear()

			print("{0}{1} to {2}= {3:.6f}".format(first_val,second_val,third_val,final_result).rstrip(".0"))
			choice=input("Do you want to make new {}? - Y/N: ".format(main_units[choice-1]))

			if choice.lower()=='y':
				choice=2
			else:
				choice=0

		elif choice==3:
			print("-"*3,"",main_units[choice-1],"","-"*3)
			first_val,second_val,third_val=float(input("Value: ")),input("From= "),str(input("To= "))
			second_val=second_val.lower()
			third_val=third_val.lower()
		
			if (second_val=='c' and third_val=='f') or (second_val=='f' and third_val=='c'):
				if temp_units.index(second_val)>temp_units.index(third_val):
					final_result=(first_val-32)/1.8
				else:
					final_result=(first_val*1.8+32)
			elif (second_val=='k' and third_val=='c') or (second_val=='c' and third_val=='k'):
				if temp_units.index(second_val)>temp_units.index(third_val):
					final_result=first_val-273.15
				else:
					final_result=first_val+273.15
			elif (second_val=='k' and third_val=='f') or (second_val=='f' and third_val=='k'):
				if temp_units.index(second_val)>temp_units.index(third_val):
					final_result=(first_val*(9/5))-459.67
				else:
					final_result=(first_val+459.67)*5/9
			else:
				final_result=first_val

			print("{0}°{1} to °{2}= {3:.6f}".format(first_val,second_val,third_val,final_result).rstrip(".0"))
			choice=input("Do you want to make new {}? - Y/N: ".format(main_units[choice-1]))

			if choice.lower()=='y':
				choice=3
			else:
				choice=0

		elif choice==4:
			break

	except ValueError as e:
		print("An error occurred!")
		continue