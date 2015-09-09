class travel_details():
	customer_name=""
	origin=""
	destination=""
	bus_number=""
	no_of_passenger=""
	travel_date=""
	booking_number=""
	passengerdetails=[]
	def __init__(self,booking_number,customer_name):
		print "inside initmethod"
		self.booking_number=booking_number
		self.customer_name=customer_name
	def set_place(self,origin,destination):
		self.origin = origin
		self.destination=destination
	def set_tdate(self,travel_date):
		self.travel_date=travel_date
	def get_passengercount(self,no_of_passenger):
		self.no_of_passenger=no_of_passenger
	def get_passengerdetails(self,passengerdetails):
		self.passengerdetails=passengerdetails
		return self.passengerdetails
	def print_details(self,booking_number):
		print "Booking Number:" +self.booking_number
		print "Customer Name:"+self.customer_name
		print "Place of origin: "+self.origin
		print "Destination:"+self.destination
		print "Travel date:"+self.travel_date
		print "Number of passenger:"+self.no_of_passenger
		print "Passenger name:"+self.passengerdetails
	