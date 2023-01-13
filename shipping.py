# Takes the input of the weight

weight = float(input("Please enter the weight:"))

# Ground Shipping

if weight <= 2:
  cost_ground = weight * 1.50 + 20
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3.00 + 20
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4.00 + 20
else:
  cost_ground = weight * 4.75 + 20

# Premium Ground Shipping

cost_premium_ground = 125

# Drone Shipping

if weight <= 2:
  cost_drone_shipping = weight * 4.50
elif weight > 2 and weight <= 6:
  cost_drone_shipping = weight * 9.00
elif weight > 6 and weight <= 10:
  cost_drone_shipping = weight * 12.00
else:
  cost_drone_shipping = weight * 14.25

# Prints the cheapest shipping method for the given weight

if cost_ground < cost_premium_ground and cost_ground < cost_drone_shipping:
  print("Ground shipping is the cheapest option, the price will be:", cost_ground)

elif cost_premium_ground < cost_ground and cost_premium_ground < cost_drone_shipping:
  print("Premium Ground shipping is the cheapest option, the price will be:", cost_premium_ground)

elif cost_drone_shipping < cost_premium_ground and cost_drone_shipping < cost_ground:
  print("Drone shipping is the cheapest option, the price will be:", cost_drone_shipping)

# I didn't have time to compare if some shipping methods were the same cost so I did this:

else:
  print("Here are the prices of each shipping method: /n", cost_ground, "/n", cost_premium_ground, "/n", cost_drone_shipping)
