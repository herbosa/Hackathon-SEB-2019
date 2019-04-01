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
        lines = email_string.split('\n')
        print(lines)
        self.message_id = lines[self.MESSAGE_ID][12:]
        self.date = lines[self.DATE][6:]
        self.from_ = lines[self.FROM][6:]
        self.to_ = lines[self.TO][4:]
        self.subject = lines[self.SUBJECT][9:]
        self.mime_v = lines[self.MIME_V][14:]
        self.content_type = lines[self.CONTENT_TYPE][14:]
        self.content_transfer_encoding = lines[self.CONTENT_TRANSFER_ENCODING][27:]
        self.x_from = lines[self.X_FROM][8:]
        self.x_to = lines[self.X_TO][6:]
        self.xcc = lines[self.X_CC][6:]
        self.xbcc = lines[self.X_BCC][7:]
        self.xfolder = lines[self.X_FOLDER][10:]
        self.xorigin = lines[self.X_ORIGIN][10:]
        self.xfilename = lines[self.X_FILENAME][13:]


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

if __name__ == '__main__' :
    f = open("../data/email_example")
    email_example = f.read()

    mail = Email(email_example)
    mail.display()
