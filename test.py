name = str(input("\nName          : "))
rollno = int(input("Exam Number   : "))
dob = str(input("Date of Birth : "))
print("\n10th Marks")
sslc1 = int(input("Enter highest mark 1 : "))
sslc2 = int(input("Enter highest mark 2 : "))
sslc3 = int(input("Enter highest mark 3 : "))
sslc = ((sslc1+sslc2+sslc3)/300)*50
print("-"*48)
print("10th marks percentage for 50% : ", sslc,"%")
print("-"*48)

print("\n11th Marks \n(without adding practical and internal marks)")
h_tamil = int(input("Enter Tamizh mark           : "))
h_english = int(input("Enter English mark          : "))
h_physics = int(input("Enter Physics mark          : "))
h_chemistry = int(input("Enter Chemistry mark        : "))
h_computer = int(input("Enter Computer Science mark : "))
h_maths = int(input("Enter Maths mark            : "))
h_total = ((h_tamil+h_english+h_physics+h_chemistry+h_computer+h_maths)/480)*20
print("-"*48)
print("11th marks percentage for 20% : ", h_total,"%")
print("-"*48)
h_tamil = (h_tamil/90)*20
h_english = (h_english/90)*20
h_physics = (h_physics/70)*20
h_chemistry = (h_chemistry/70)*20
h_computer = (h_computer/70)*20
h_maths = (h_maths/90)*20


print("\nYou're practical marks may be 30 out of 30")

print("\n12th Individual subjects marks:")
print("Tamizh            ",sslc+h_tamil+30)
print("English           ",sslc+h_english+30)
print("Physics           ",sslc+h_physics+30)
print("Chemistry         ",sslc+h_chemistry+30)
print("Computer Science  ",sslc+h_computer+30)
print("Maths             ",sslc+h_maths+30)

final_mark = sslc+h_tamil+30+sslc+h_english+30+sslc+h_physics+30+sslc+h_chemistry+30+sslc+h_computer+30+sslc+h_maths+30
final_percentage = sslc + h_total + 30

cutoff = 0
if h_computer > h_chemistry:
    cutoff = ((sslc+h_computer+30)/2) + (sslc+h_maths+30) + ((sslc+h_physics+30)/2)
elif h_computer < h_chemistry:
    cutoff = ((sslc+h_chemistry+30)/2) + (sslc+h_maths+30) + ((sslc+h_physics+30)/2)


print("-"*48)
print("Total mark          : ",final_mark,"/ 600")
print("Overall percentage  : ", final_percentage,"%")
print("Engineering Cut-off : ",cutoff,"%")
print("-"*48)