import simplekml


def coordinates(latitude, longitude):
    kml = simplekml.Kml()
    kml.newpoint(name="Sample", coords=[(longitude, latitude)])
    kml.save("/home/www/python-studies/scripts/input_user/kml_test_input.kml")
    print("File created, input in google earth for view point.")


lng = input("Please enter longitude: ")
lat = input("Please enter latitude: ")
coordinates(lng, lat)

