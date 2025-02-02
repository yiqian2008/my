type(-37)
varforsunday = "sunday"
dailycal = ["mon","tue","wed"]
print(varforsunday)
print(type((1)))
type((1,))
days = [ "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun" ]
days[2:3] = [ "TUESDAY", "WEDNESDAY" ]
print(days)

days = [ "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun" ]
days[2:3] = [ "TUESDAY", "moon-eclipse-night!!!", "WEDNESDAY" ]
print(days)

v = [ 1, 2, 3 ]               
w = v          
v[0] = 100        
print(v)

v = [ 1, 2, 3 ]
w = v.copy()
v[0] = 100
v