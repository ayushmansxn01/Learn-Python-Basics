class ElectronicDevice:
    battery="12V"
class PocketDevice(ElectronicDevice):
    size="12inch"
class Phone(PocketDevice):
    number_Of_Call=12
    def call():
        print("Calling")

nokia=(Phone)
print(nokia.battery)
print(Phone.call())