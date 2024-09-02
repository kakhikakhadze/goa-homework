num = int(input("დაწერეთ რიცხვი :"))
num2 = int(input("დაწერეთ მეორე რიცხვი :"))

kl = input("განახორციელეთ მოქმედება :")
if kl == "*":
    print(num * num2)
elif num2 == 0 and kl == "//":
    print("ნულზე გაყოფა შეუძლებელია")
elif  kl == "//":
    print(num // num2)
elif  kl== "+":
    print(num + num2)
elif  kl == "-":
    print(num - num2)
elif num2 == 0 and kl == "//":
    print("ნულზე გაყოფა შეუძლებელია")
