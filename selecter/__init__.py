#!/usr/bin/env python
import re


def selecter(List, Greeting="Select from: ", prompt=": "):
    """
        A very simple class to facilitate ease of selecting from a list of
        choices, assigning a number to each choice, and requiring the user to
        make a selection before letting them go

    Usage::

        >>> from selecter import selecter
        >>> selecter(['First', 'Second', 'Third'])
        Select from: 1:First, 2:Second, 3:Third : 2
        'Second'
        >>>

    """
    DList = {}
    for index, val in enumerate(List, 1):
        DList[index] = val
    prompt_string = Greeting
    for index, value in enumerate(List, 1):
        if index < len(List):
            comma = ','
        else:
            comma = ''
        prompt_string += "%s:%s%s " % (index, value, comma)
    prompt_string += prompt
    final_choice = ''
    while final_choice is '':
        choice = raw_input(prompt_string)
        if re.search("^[0-9]+$", choice):
            # good they selected a number
            final_choice = DList[int(choice)]
        else:
            # they may have entered the actual choice.
            if choice in List:
                final_choice = choice
        print chr(13),
    return final_choice
