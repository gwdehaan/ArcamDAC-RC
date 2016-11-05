L1= Pin('X1', Pin.OUT_PP)
L2= Pin('X2', Pin.OUT_PP)
L3= Pin('X3', Pin.OUT_PP)
	
# ingebouwde usr switch
sw = pyb.Switch()

looplicht=[L1,L2,L3] #list met alle poorten die het looplicht vormen.
c=0 # Counter voor looplicht, welke LED brandt
def SwitchPressed():
	global looplicht
	global c
	for i, led in enumerate(looplicht): # is de index, led de feitelijke led.
		if c==i:
			led.high()
		else:
			led.low()
		if c==len(looplicht)-1: #herstart het looplicht
			c=0
		else:
			c+=1
			
# test het looplicht

sw.callback(SwitchPressed)

while true:
	pass
