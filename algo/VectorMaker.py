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

import numpy as np

class VectorMaker :
    def __init__(self) :
        self.init = True

    def VectorFromChars(self, content : str, size : int, step : int) :
        vector = []
        i = 0
        step_len = int(size / step)
        my_step = -1

        while my_step < step :
            if i % step_len == 0 :
                my_step = my_step + 1 
                if my_step == step :
                    break
                vector.append([])
            if i < len(content) :
                vector[-1].append(ord(content[i]))
            else :
                vector[-1].append(0)
            i = i + 1

        """ Make Numpy Array """
        array = np.array(vector)
        """ Normalize vector """
        normalize = array / 127
        return (normalize)


if __name__ == '__main__' :
    vect = VectorMaker()
    mat = vect.VectorFromChars("abcdefghi123456789", 12, 3)
    print(mat)

