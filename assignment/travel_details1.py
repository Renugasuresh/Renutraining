class travel_details():
	customer_name=""
	origin=""
	destination=""
	bus_number=""
	no_of_passenger=""
	travel_date=""
	booking_number=""
	passengerlist=[]
	passengerage={}
	def __init__(self,booking_number,customer_name):
		self.booking_number=booking_number
		self.customer_name=customer_name
	def set_place(self,origin,destination):
		self.origin = origin
		self.destination=destination
	def set_tdate(self,travel_date):
		self.travel_date=travel_date
	def get_passengerdetails(self):
		n=raw_input("enter the number of passenger")
		x=int(n)
		print "Enter the name of passengers"
		for i in range(0,x):
			pl=raw_input()
			#age=raw_input("enter age of"+pl)
			self.passengerlist.append(pl)
			#self.passengerage[self.passengerlist]=age
		print self.passengerlist
		for j in range (0,len(self.passengerlist)):
			age=raw_input("Enter Age of"+self.passengerlist[j])
			self.passengerage[self.passengerlist[j]]=age
		
	def print_details(self,booking_number):
		print "Booking Number:" +self.booking_number
		print "Customer Name:"+self.customer_name
		print "Place of origin: "+self.origin
		print "Destination:"+self.destination
		print "Travel date:"+self.travel_date
		#print "Number of passenger:"+x
		print "Passengers travelling with their age"
		print self.passengerage
	