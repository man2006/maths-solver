print("Select The Type of Question You Want Solve:-")

a = print("1: 2D Figures")
b = print("2: 3D Figures")

question_type = input("Enter 1 or 2:")

if question_type ==  '1':
 	print("Select Figure:-")
 	print("1: Rectangle")
 	print("2: Square")
 	print("3: Circle")
 	print("4: Triangle")

 	select_figure = input("Enter 1, 2, 3, 4:")

 	if select_figure in ('1', '2', '3', '4'):
 		if select_figure == '1':
 			length =  float(input("Enter The Length of Rectangle: "))
 			breadth = float(input("Enter The Breadth of Rectangle: "))
 			r_perimeter = (length + breadth)*2
 			r_area = length * breadth 
 			print("Perimeter is:", r_perimeter ,  "Area is", r_area)
 		
 		elif select_figure == '2':
 			side = float(input("Enter The Side of Square: "))
 			s_perimeter = 4 * side
 			s_area = side**2
 			print("Perimeter is:", s_perimeter ,  "Area is", s_area)

 		elif select_figure == '3':
 			c_radius = float(input("Enter The Radius of Circle: "))
 			c_pie = 22/7
 			c_perimeter = (c_radius * c_pie) * 2
 			c_area = c_pie * c_radius**2 
 			print("Perimeter is:", c_perimeter ,  "Area is", c_area)

 		elif select_figure == '4':
 			t_1 = float(input("Enter The 1st Side of Triangle: "))
 			t_2 = float(input("Enter The 2nd Side of Triangle: "))
 			t_3 = float(input("Enter The 3rd Side of Triangle: "))
 			t_perimeter = t_1 + t_2 + t_3
 			t_semi = t_perimeter/2
 			t_area = (t_semi*(t_semi-t_1)*(t_semi-t_2)*(t_semi-t_3))**0.5
 			print("Perimeter is:", t_perimeter ,  "Area is", t_area)
 		
 	else:
 		print("Please Enter A Valid Input!")

elif question_type == '2':
	print("Select The Figure:-")
	print("1: Cube")
	print("2: Cuboid")
	print("3: Cylinder")
	print("4: Cone")
	print("5: Sphere")

	select_figure = input("Enter 1, 2, 3, 4, 5:")

	if select_figure in ("1","2","3","4","5"):
		if select_figure == '1':
			c_edge = float(input("Enter The Edge of Cube:"))
			c_volume = c_edge**3
			c_tsa = 6*(c_edge**2)
			c_lsa = 4*(c_edge**2)
			print("Volume is",c_volume,"T.S.A. is",c_tsa,"L.S.A. is",c_lsa)

		elif select_figure == '2':
			c_l = float(input("Enter The Length of Cuboid:"))
			c_b = float(input("Enter The Breadth of Cuboid:"))
			c_h = float(input("Enter The Height of Cuboid:"))
			c_v = c_l * c_b * c_h
			c_tsa = 2*(c_l*c_b+c_b*c_h+c_l*c_h)
			c_lsa = 2*(c_l+c_b)*c_h
			print("Volume is",c_v,"T.S.A. is",c_tsa,"L.S.A. is",c_lsa)

		elif select_figure == '3':
			cy_r = float(input("Enter The Radius of The Cylinder:"))
			cy_h = float(input("Enter The Height of The Cylinder:"))
			cy_p = 22/7
			cy_v = cy_p*(cy_r**2)*cy_h
			cy_csa = 2*cy_p*cy_r*cy_h
			cy_tsa = (2*(cy_p*cy_r**2))+cy_csa
			print("Volume is",cy_v,"T.S.A. is",cy_tsa,"C.S.A. is",cy_csa)

		elif select_figure == '4':
			co_r = float(input("Enter The Radius of The Cone:"))
			co_h = float(input("Enter The Height of The Cone:"))
			co_p = 22/7
			co_v =(co_p*(co_r**2)*co_h)*1/3
			co_l = (co_r**2 + co_h**2)**0.5
			co_csa = co_p*co_r*co_l
			co_tsa = (co_p*co_r**2)+co_csa
			print("Volume is ",co_v,"T.S.A. is ",co_tsa,"C.S.A is ",co_csa)

		elif select_figure == '5':
			sp_r = float(input("Enter The Radius of The Sphere: "))
			sp_p = 22/7
			sp_v = 4/3*sp_p*sp_r**3
			sp_a = 4*sp_p*sp_r**2
			print("Volume is",sp_v,"T.S.A. or C.S.A. is",sp_a)

	else:
		print("Enter a Valid Input!")
else:
	print("Enter a Valid Input!")

_exit_ = input("Press Enter Key To Exit.")