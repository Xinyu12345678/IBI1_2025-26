#store value of age, weight,gender,Cr
#Validate all inputs meet the requirments
#1.age<100(integer)
#2.weight between 20kg and 80kg(float)
#3.0<Cr<100(float)
#4.gender:male/female(case sensitive)
#report variables need corrected
#stop program if input is wrong
#calculate CrCl
age=int(input("your age (years):"))
if age<=0 or age>=100:
    print(f"Age {age} is invalid: must be less than 100")
    exit()
weight=float(input("your weight (kg):"))
if weight<=20 or weight>=80:
    print(f"Weight {weight} is invalid: must be >20kg and <80kg")
    exit()
gender=input("your gender (male/female):").lower()
if gender not in ["male","female"]:
    print(f"Gender {gender} is invalid: must be male/female")
    exit()
Cr=float(input("your Cr (µmol/l):"))
if not 0<Cr<100:
    print(f"Cr {Cr} is invalid:must be 0<Cr<100")
    exit()
if gender=="male":
    CrCl=(140-age)*weight/(72*Cr)
else:
    CrCl=(140-age)*weight*0.85/(72*Cr)
print(f"Your creatine clearance rate is {CrCl} ml/min")