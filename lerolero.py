#!/usr/bin/pyhton3

import random

parte1 = [
        "Frase 1.1",
        "Frase 1.2",
        "Frase 1.3"
        ]
parte2 = [
        "Frase 2.1",
        "Frase 2.2",
        "Frase 2.3"
        ]
parte3 = [
        "Frase 3.1",
        "Frase 3.2",
        "Frase 3.3"
        ]

lingua = input("Escolha alíngua; 1 - português; 2 - Inglês")

if lingua == 2:
    parte1 = []
    parte2 = []
    parte3 = []

print(random.choice(parte1), random.choice(parte2), random.choice(parte3)
