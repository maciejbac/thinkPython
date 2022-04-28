# Sphere volume

def sphereVolume(r):
    pi = 3.14159
    volume = 1.33 * pi * r**3
    return volume

print(sphereVolume(5))

# Book and shipping price calculations
def wholesalePrice(count):
    price = 24.95
    discount = 1 - 0.4
    shipping = 3
    additional_copy_shipping = 0.75
    wholesale_price = (count * price * discount) + shipping + ((count - 1) * additional_copy_shipping)
    return wholesale_price

print (wholesalePrice(60))