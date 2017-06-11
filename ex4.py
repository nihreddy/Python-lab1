customer_name = raw_input("Please enter customer name: ")

labor_hours = float(raw_input("Please enter labor hours: "))

cost_of_parts_and_supplies = float(raw_input("Please enter cost of parts and supplies: "))

labor_cost = 3.5 * labor_hours

parts_cost =  cost_of_parts_and_supplies + (cost_of_parts_and_supplies * 0.07)
 
total_cost = labor_cost + parts_cost

print "Customer: %s" % (customer_name)
print "Labor cost: {0:.2f}".format(labor_cost)
print "Parts cost: {0:.2f}".format(parts_cost)
print "Total cost: {0:.2f}".format(total_cost)