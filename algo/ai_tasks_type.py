"""
Hackathon-SEB-2019
Copyright (C) 2019 EPITARQUES

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from keras.models import Sequential
from keras.layers import GRU, Dense, Dropout
from Email import *
f = open("../data/email_example")
email_example = f.read()
mail = Email(email_example)
matrix = mail.toMatrix()
print(matrix)


model = Sequential()

model.add(GRU(128, activation='relu', return_sequences=True, input_shape=(11, 100,)))
model.add(GRU(128, activation='relu', return_sequences=True))
model.add(GRU(64, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(6, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(np.array([matrix]), np.array([[0, 1, 0, 0, 0, 0]]))
