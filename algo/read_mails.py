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

from Email import *

def read_mails_array(filename : str) :
    mails_array = []
    f = open(filename)
    content = f.read().split('"')
    for e in content :
        if e.startswith('Message-ID:') :
            try :
                my_mail = Email(e)
                mails_array.append(my_mail)
            except :
                continue
    return (mails_array)

def append_if_dont_exists(array : list, name : str) :
    for e in array :
        if e == name :
            return
    array.append(name)
    return (array)

def create_emails_addresses_array(mails_array : list) :
    array = []
    for e in mails_array :
        append_if_dont_exists(array, e.to_)
    print(len(array))
    return (array)

if __name__ == '__main__' :
    mails_array = read_mails_array("../data/500000_first-lines_email.csv")
    print(len(mails_array))
    create_emails_addresses_array(mails_array)
