from __future__ import print_function, unicode_literals
import inquirer
from pprint import pprint
questions = [
    {
        'type': 'input',
        'name': 'first_name',
        'message': 'What\'s your first name',
     }
]
answers = inquirer.prompt(questions)
pprint(answers)