
def in2cm(inches):
    return inches * 2.54

def mToKm(miles):
    return miles * 1.60934
    
if __name__=="__main__":
  for i in range(1,11):
    print(i, " inches is ", in2cm(i), " centimeters")
