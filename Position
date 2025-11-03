import time

name = ("Chemical Mechanical Pipette Position Calculator")

print(name)
time.sleep(2)

print("formula")
time.sleep(1)
print("Rack travel distance = number of gear rotations * [number of gear teeth * (rack pitch + rack tooth thickness)]")
time.sleep(1)
print("h=N*[D*(a+K)]")
time.sleep(2)

print("dictionary")
time.sleep(1)
print("h = Rack travel distance")
time.sleep(0.30)
print("N = Number of gear rotations")
time.sleep(0.30)
print("D = Number of gear teeth")
time.sleep(0.30)
print("a = Rack pitch")
time.sleep(0.30)
print("K = Rack tooth thickness")
time.sleep(2)

print("CALCULATION")
time.sleep(1)

h = ("Calculating...")

# Fonksiyon: geçerli sayı girene kadar sor
def get_input(prompt):
    while True:
        value = input(prompt)
        if value.strip() == "":
            print("Input cannot be empty! Please enter a number.")
            continue
        try:
            return int(value)
        except ValueError:
            print("Invalid input! Please enter a valid number.")

N = get_input("Enter the value of N: ")
D = get_input("Enter the value of D: ")
a = get_input("Enter the value of a: ")
K = get_input("Enter the value of K: ")

time.sleep(0.30)
print("Saving your values...")
time.sleep(3)

info = [h, N, D, a, K]
print("Your values: h:{} N:{} D:{} a:{} K:{}".format(info[0], info[1], info[2], info[3], info[4]))
time.sleep(2)
print("Your formula: h={}*[{}*({}+{})]".format(info[1], info[2], info[3], info[4]))
time.sleep(2)

result = N * (D * (a + K))
result_data = [result]

print("Calculating your result...")
time.sleep(2)
print("Your h value = {}".format(result_data[0]))
time.sleep(1)
son = input("Press Enter to close!")
