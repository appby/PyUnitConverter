def write_units(param):
	def write_output(param_list):
		result_dic={param_list.index(x)+1:x for x in param_list}
		for keys,values in result_dic.items():
			print("{}- {}".format(keys,values))

	if param==1:
		length_list=["mm","cm","dm","m","dam","hm","km"]
		write_output(length_list)
	elif param==2:
		byte_units=["b","kb","mb","gb","tb","pb"]
		write_output(byte_units)
	elif param==3:
		temp_units=['c','f','k']
		write_output(temp_units)

def take_values():
	val1,val2,val3=float(input("Miktar: ")),int(input("Birim: ")),int(input("Donusecek Birim: "))
	return val1,val2,val3

def length_conversion(value,default_val,to_val):
	if default_val>to_val:
		return value*(10**(default_val-to_val))
	elif default_val<to_val:
		return value/(10**(to_val-default_val))
	else:
		return value

def byte_conversion(value,default_val,to_val):
	if default_val>to_val:
		return value*(2**(10*(default_val-to_val)))
	elif default_val<to_val:
		return float(value/(2**(10*(to_val-default_val))))
	else:
		return value

def temp_conversion(value,default_val,to_val):
	if (default_val-to_val==1 or to_val-default_val==1) and (default_val<2 or to_val<2) :
		if default_val>to_val:
			return (value-32)/1.8
		else:
			return (value*1.8+32)
	elif (default_val-to_val==2) or (to_val-default_val==2):
		if default_val>to_val:
			return value-273.15
		else:
			return value+273.15
	elif (default_val-to_val==1 or to_val-default_val==1) and (default_val>2 or to_val>2):
		if default_val>to_val:
			return (value*(9/5))-459.67
		else:
			return (value+459.67)*5/9
	else:
		return value

while True:
	try:
		print("1- Uzunluk Dönüşümü","2- Byte Dönüşümü","3- Sıcaklık Dönüşümü","4- Çıkış\n",sep=" | ")		
		for i in range(1):
			choice=int(input("Lütfen Yapmak istediğiniz işlemleri numara seçimi ile belirtin: "))
			if choice>4 or choice<=0:
				print("!"*3,"Aralık dışında seçim yaptınız. Tekrar deneyin.\n")
			else:
				break
		if choice==1:
			write_units(choice)
			vals=take_values()
			print("Sonuç: {}\n".format(length_conversion(vals[0],vals[1],vals[2])))
		elif choice==2:
			write_units(choice)
			vals=take_values()
			print("Sonuç: {:.6f}\n".format(byte_conversion(vals[0],vals[1],vals[2])))
		elif choice==3:
			write_units(choice)
			vals=take_values()
			print("Sonuç: {:.2f}\n".format(temp_conversion(vals[0],vals[1],vals[2])))
		else:
			break
	except:
		print("!"*3,"Hata oluştu\nSeçiminizi sayı değeri olarak yazın!\n")