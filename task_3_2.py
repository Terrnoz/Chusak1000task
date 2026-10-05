import math

print("radians(180) =", math.radians(180))
print("degrees(math.pi) =", math.degrees(math.pi))

print("sin(pi/2) =", math.sin(math.pi / 2))
print("cos(0) =", math.cos(0))
print("tan(pi/4) =", math.tan(math.pi / 4))

print("asin(0.5) =", math.asin(0.5))
print("atan2(-1, -1) =", math.atan2(-1, -1))
print("hypot(3, 4) =", math.hypot(3, 4))

x1, y1 = 1, 2
x2, y2 = 4, 6
dist = math.hypot(x2 - x1, y2 - y1)
print(f"Расстояние между точками: {dist}")