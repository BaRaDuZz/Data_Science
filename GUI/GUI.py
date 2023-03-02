import tkinter as Tk
from tkinter import ttk
from sklearn.neighbors import KNeighborsRegressor
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

from Persons import Persona3, Persona2, Persona1

# Laden der CSV-Datei in einen Pandas DataFrame
data = pd.read_csv('C:\\Users\Tobi\PycharmProjects\Data Science\dataframe backup\Affairs.csv')

# Definieren der Features (X) und des Labels (y)
X = data.drop('affairs', axis=1)
y = data['affairs']

# Aufteilen der Daten in Trainings- und Testdaten
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Skalieren der Daten auf einen gemeinsamen Wertebereich
# (damit alle Features gleich behandelt werden)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialisieren des k-NN Regressors und Trainieren auf den Trainingsdaten
k = 5
knn = KNeighborsRegressor(n_neighbors=k)
knn.fit(X_train, y_train)

# Vorhersage auf den Testdaten
y_pred = knn.predict(X_test)

# Ausgabe der Performance-Metrik (MSE)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

predicted_affairs = knn.predict(Persona3.Persona3)

# Drucke die Vorhersage aus
print('Die Vorhersage der Anzahl der Affären für diese Person beträgt:', predicted_affairs[0])

root = Tk()

# Adjust size
root.geometry("200x200")


# Change the label text
def show():
    label.config(text=clicked.get())


# Dropdown menu options
options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set("Monday")

# Create Dropdown menu
drop = OptionMenu(root, clicked, *options)
drop.pack()

# Create button, it will change label text
button = Button(root, text="click Me", command=show).pack()

# Create Label
label = Label(root, text=" ")
label.pack()

# Execute tkinter
root.mainloop()


