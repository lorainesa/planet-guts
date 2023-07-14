# Main code for code astro project
# Kenzie, Loraine, and Helena
from main import *
import massive_galaxies

print('Hello, welcome to the multidisciplinary package planet-guts! Please select your discipline; enter 0 for interferometric masking, 1 for galaxy catalogs, and 2 for numerical integration:')

in_val = input()

if in_val != (0 or 1 or 2):
    print("Oops! Input must be 0, 1, or 2.")

if in_val == 0:
    print("You've selected masking mode! Please enter number of holes:")
    nholes = int(input())
    print("Thanks! Next, please enter the hole diameter in meters:")
    hrad = float(input())
    print('Thanks! Making a mask...')
    main(nholes, hrad)

if in_val == 1:
    print("You've selected galaxy mode!")

if in_val == 2:
    print("You've selected numerical integration mode!")