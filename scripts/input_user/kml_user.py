import simplekml

def coordinates(latitude, longitude):
    kml = simplekml.Kml()
    kml.newpoint(name="Sample", coords=[(latitude, longitude)])
    kml.save("/home/www/python-studies/scripts/input_user/kml_test_input.kml")
    print("File created, input in google earth for view point.")


lat = input("Please enter latitude: ")
lng = input("Please enter longitude: ")
coordinates(lat, lng)

