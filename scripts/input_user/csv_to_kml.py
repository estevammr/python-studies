import simplekml
import pandas


df = pandas.read_csv("/home/www/python-studies/scripts/input_user/coordinates.csv")
kml = simplekml.Kml()

for lon, lat in zip(df["Longitude"], df["Latitude"]):

    kml.newpoint(coords=[(lon, lat)])
kml.save("/home/www/python-studies/scripts/input_user/kml_test_input_2.kml")
print("File created, input in google earth for view point.")




