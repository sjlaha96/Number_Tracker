import phonenumbers
from phonenumbers import timezone, geocoder, carrier
#timezone for time, geocoder for loaction, carrier for sim card

number=input("Enter the number: ")
phone=phonenumbers.parse(number) #parse will provide the number details
time=timezone.time_zones_for_number(phone)
sim=carrier.name_for_number(phone,"en") #"en" means phone number should be in english
reg=geocoder.description_for_number(phone, "en")

print(phone)
print(time)
print(sim)
print(reg)
