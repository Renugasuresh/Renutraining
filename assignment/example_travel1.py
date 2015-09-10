from travel_details import travel_details
booking1=travel_details("234","mohit")
print "Travel Booking Application"
print "****************************************"
print "Do you want to book tickets Y/N"
choice=raw_input()
if (choice == 'Y'):
	print "Enter the place of origin"
	o=raw_input()
	print "Enter the Destination place"
	d=raw_input()
	booking1.set_place(o,d)
	print "Enter the date of travel"
	date=raw_input()
	booking1.set_tdate(date)
	print "Are you travelling as group Y/N"
	choice1=raw_input()
	if (choice1=='Y'):
		booking1.get_passengerdetails()
	else:
		print "Booked tickets with following details" 
		booking1.print_details("234")
	print "Booked tickets with following details"
	booking1.print_details("234")
else:
	print "Exit the application"
	
