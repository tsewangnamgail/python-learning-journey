import cmath

var = list(map(int, input("Enter coefficients a, b, c separated by space: ").split()))
a = var[0]
b = var[1]
c = var[2]
# 2. Calculate the discriminant
discriminant = (b**2) - (4 * a * c)

# 3. Branch into the 3 mathematical possibilities
if discriminant < 0:
    # Possibility 1: Two Imaginary Roots
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    
    # Keep raw complex numbers inside the tuple
    roots_tuple = (root1, root2)
    
    print("Possibility 1 - Imaginary roots detected (Saved in tuple):")
    # Format each complex root's real and imag parts to 2 decimal places
    print(f"({roots_tuple[0].real:.2f} + {roots_tuple[0].imag:.2f}j, {roots_tuple[1].real:.2f} + {roots_tuple[1].imag:.2f}j)")

elif discriminant == 0:
    # Possibility 2: Exactly One Repeated Real Root
    root = -b / (2 * a)
    print(f"Possibility 2 - One repeated real root: {root:.2f}")

else:
    # Possibility 3: Two Distinct Real Roots
    root1 = (-b + (discriminant)**0.5) / (2 * a)
    root2 = (-b - (discriminant)**0.5) / (2 * a)
    print(f"Possibility 3 - Two distinct real roots: {root1:.2f} and {root2:.2f}")
