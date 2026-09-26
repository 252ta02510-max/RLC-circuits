import math

print("RLC Circuit Calculator")
print("----------------------")

R = float(input("Enter Resistance (Ohms): "))
L = float(input("Enter Inductance (H): "))
C = float(input("Enter Capacitance (F): "))
f = float(input("Enter Frequency (Hz): "))

XL = 2 * math.pi * f * L
XC = 1 / (2 * math.pi * f * C)

Z = math.sqrt(R**2 + (XL - XC)**2)
I = 1 / Z

fr = 1 / (2 * math.pi * math.sqrt(L * C))

print("\nResults:")
print("Inductive Reactance =", XL, "Ohms")
print("Capacitive Reactance =", XC, "Ohms")
print("Impedance =", Z, "Ohms")
print("Current for 1V =", I, "A")
print("Resonant Frequency =", fr, "Hz")
