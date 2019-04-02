#!/usr/bin/env python3
"""Mail generator program.

generate appointement mail templated on that kind of syntax:

I want an appointment monday 29 April at 6:45 a.m to talk about the MazalTov project.
Are you open on March 21 at 7:45 a.m for a meeting concerning ICT project.
Can you accept the invitation for the DevScope project on April 23 at 4h30 p.m ?
Can we discuss the 17 March at 2:50 a.m about Prastiva client ?
I invited you at 4:15 p.m Tuesday 21 March, are you open ?
Let meet us at 5 p.m Monday 25 April.
I organized a meeting for the project ErasmaShit the 7 March at 6 a.m, are you agree with that ?
"""

import random as rand;
import sys

TASKS_TYPE = {
    "Backend": [
        "Server",
        "Node",
        "NodeJS",
        "PHP",
        "Django",
        "Python",
        "Flask"
    ],
    "Frontend": [
        "HTML",
        "CSS",
        "Web",
        "Site",
        "Website",
        "Javascript",
        "ReactJS",
        "VueJS"
    ],
    "SystemProgramming": [
        "C",
        "C++",
        "Cpp",
        "Rust",
        "ASM",
        "Intel"
    ],
    "GameDevelopment": [
        "Game",
        "Unity",
        "Unreal Engine",
        "Godot",
        "SFML"
    ],
    "SystemAdministration": [
        "Apache",
        "Nginx",
        "Haproxy",
        "Proxy",
        "Reverse proxy",
        "DNS",
        "Firewall",
        "SSL",
        "Certificate"
    ],
    "Scripting": [
        "Bash",
        "Python",
        "PowerShell",
        "Lisp"
    ],
    "DevOps": [
        "Gitlab",
        "CI",
        "UnitTest",
        "Pipeline",
        "Integration",
        "Pull Request",
        "Code Review"
    ],
    "Mobile": [
        "ReactNative",
        "Java",
        "Android",
        "Kotlin",
        "Swift",
        "Xamarin"
    ]
}

SENTENCES = {
    "begin": [
        "I want an appointment",
        "Are you open",
        "Can you accept the invitation",
        "Can we discuss",
        "I invited you",
        "Let meet us",
        "I organized a meeting",
    ],
    "date": " on {} the {} at {}:{:02}{} ",
    "end": [
        "to talk about {}.",
        "for a meeting concerning {}.",
        "for the {} project.",
        "about {} client ?",
        "about {}, are you open ?",
        "for the project {}, are you agree with that ?"
    ]
}

MONTHS = [
    "January",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

class MailGenerator(object):
    """Docstring for MailGenerator. """

    def __init__(self, nbr: int):
        """Initialize Mail generator."""
        self.nbr = nbr;

    def generate(self):
        """Generate self.nbr sentences."""
        sentences = []

        for i in range(0, self.nbr):
            line = SENTENCES['begin'][rand.randrange(0, len(SENTENCES['begin']))]
            line += SENTENCES['date'].format(
                MONTHS[rand.randrange(0, 11)],
                rand.randrange(1, 30),
                rand.randrange(6, 12),
                rand.randrange(0, 59),
                "a.m" if rand.randrange(0, 2) % 2 == 0 else "p.m"
            )
            task_entry = rand.choice(list(TASKS_TYPE.keys()))
            task_type = TASKS_TYPE[task_entry][rand.randrange(0, len(TASKS_TYPE[task_entry]))]
            line += SENTENCES["end"][rand.randrange(0, len(SENTENCES["end"]))].format(task_type)
            sentences.append(line)
        return sentences

if __name__ == "__main__":
    try:
        nb_mail: int = int(sys.argv[1])
    except Exception:
        nb_mail: int = 1000
    mail_generator = MailGenerator(nb_mail)
    mails = mail_generator.generate()
    for elem in mails:
        print(elem)
