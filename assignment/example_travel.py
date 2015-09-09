from travel_details import travel_details
passengerdetails=[]
booking1=travel_details("234","mohit")
print "Enter the place of origin and destination"
o=raw_input()
d=raw_input()
booking1.set_place(o,d)
print "Enter the number of passenger"
print "Enter the name of passenger"
n=raw_input()
booking1.get_passengercount(n)
for i in range(0,int(n)):
	pn=raw_input()
	passengerdetails.append(pn)
print passengerdetails
booking1.get_passengerdetails(pn)
print "Enter the date of travel"
date=raw_input()
booking1.set_tdate(date)
booking1.print_details("234")
print passengerdetails

