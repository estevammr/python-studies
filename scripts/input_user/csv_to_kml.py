import simplekml
import pandas
import tkinter
from tkinter.filedialog import askopenfilename


def browse():
    global infile
    infile = askopenfilename()


def kml_gui(outfile='/home/www/python-studies'
                    '/scripts/input_user'
                    '/kml_test_input_2.kml'):
    df = pandas.read_csv(infile)
    kml = simplekml.Kml()

    for lon, lat in zip(df["Longitude"], df["Latitude"]):
        kml.newpoint(coords=[(lon, lat)])
    kml.save(outfile)
    print("File created, input in google earth for view point.")


root = tkinter.Tk()
root.title("Kml generator")
label = tkinter.Label(root, text="This program generate a KML file")
label.pack()
browseButton = tkinter.Button(root, text="Browse", command=browse)
browseButton.pack()
kmlButton = tkinter.Button(root, text="Generate KML", command=kml_gui)
kmlButton.pack()
root.mainloop()



