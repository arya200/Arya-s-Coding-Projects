
print("This program is to calculate the average length of an M/M/1 queue with given arrival and service rates.")

print("")

arrival_rate = float(input("Please enter the arrival rate: "))
service_rate = float(input("Please enter the service_rate: "))

length = float(((arrival_rate/service_rate)**2)/(1-(arrival_rate/service_rate)))

print("The average length of the M/M/1 queue is:", length)