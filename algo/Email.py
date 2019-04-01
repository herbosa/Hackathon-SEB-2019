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

import sys, os

class Email:
    """Email is ..."""
    MESSAGE_ID = 0
    DATE = 1
    FROM = 2
    TO = 3
    SUBJECT = 4
    MIME_V = 5
    CONTENT_TYPE = 6
    CONTENT_TRANSFER_ENCODING = 7
    X_FROM = 8
    X_TO = 9
    X_CC = 10
    X_BCC = 11
    X_FOLDER = 12
    X_ORIGIN = 13
    X_FILENAME = 14

    def __init__(self, email_string: str) :
        """Initialize the email from string."""
        self._load(email_string)

    def _load(self, email_string : str) :
        """ Spliting email informations """
        self._lines = email_string.split('\n')

        """ Information """
        self.message_id = self._lines[self.MESSAGE_ID][12:]
        self.date = self._lines[self.DATE][6:]
        self.from_ = self._lines[self.FROM][6:]
        self.to_ = self._lines[self.TO][4:]
        self.subject = self._lines[self.SUBJECT][9:]
        self.mime_v = self._lines[self.MIME_V][14:]
        self.content_type = self._lines[self.CONTENT_TYPE][14:]
        self.content_transfer_encoding = self._lines[self.CONTENT_TRANSFER_ENCODING][27:]
        self.x_from = self._lines[self.X_FROM][8:]
        self.x_to = self._lines[self.X_TO][6:]
        self.xcc = self._lines[self.X_CC][6:]
        self.xbcc = self._lines[self.X_BCC][7:]
        self.xfolder = self._lines[self.X_FOLDER][10:]
        self.xorigin = self._lines[self.X_ORIGIN][10:]
        self.xfilename = self._lines[self.X_FILENAME][13:]
        self.content = self._get_content()

    def _get_content(self) :
        return_content = ""
        self._content = self._lines[self.X_FILENAME:]
        for e in self._content :
            return_content = return_content + e + '\n'
        return (return_content)

    def display(self):
        print("MESSAGE ID:", self.message_id)
        print("DATE:", self.date)
        print("FROM:", self.from_)
        print("TO:", self.to_)
        print("SUBJECT:", self.subject)
        print("MIME_V:", self.mime_v)
        print("CONTENT_TYPE:", self.content_type)
        print("CONTENT_TRANSFER_ENCODING:", self.content_transfer_encoding)
        print("X_FROM:", self.x_from)
        print("X_TO:", self.x_to)
        print("X_CC:", self.xcc)
        print("X_BCC:", self.xbcc)
        print("X_FOLDER:", self.xfolder)
        print("X_ORIGIN:", self.xorigin)
        print("X_FILENAME:", self.xfilename)
        print("CONTENT:", self.content)

if __name__ == '__main__' :
    f = open("../data/email_example")
    email_example = f.read()

    mail = Email(email_example)
    mail.display()
