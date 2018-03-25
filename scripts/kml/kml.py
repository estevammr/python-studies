import simplekml

kml = simplekml.Kml()

kml.newpoint(name="Sample", coords=[(10, 10)])
kml.newpoint(name="Sample2", coords=[(100, 105)])
kml.save("/home/www/python-studies/scripts/kml/kml_test.kml")
