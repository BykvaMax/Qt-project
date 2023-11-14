import requests

from random import choice


class Receiving:
    def __init__(self, *args):
        super().__init__()
        self.get_info(args)

    def get_info(self, args):
        types = ['math', 'trivia', 'date', 'year']
        self.type = choice(types)
        self.requeast = args[1]

        if self.requeast == 'Получить факт о дате':
            url = f"https://numbersapi.p.rapidapi.com/{int(args[2])}/{int(args[3])}/date"

            querystring = {"fragment": "true", "json": "true"}

        elif self.requeast == 'Получить мудреный факт о числе':
            url = f"https://numbersapi.p.rapidapi.com/{int(args[2])}/math"

            querystring = {"fragment": "true", "json": "true"}

        elif self.requeast == 'Получить примитивный факт о числе':
            url = f"https://numbersapi.p.rapidapi.com/{int(args[2])}/trivia"

            querystring = {"fragment": "true", "notfound": "floor", "json": "true"}

        elif self.requeast == 'Получить факт о годе':
            url = f"https://numbersapi.p.rapidapi.com/{int(args[2])}/year"

            querystring = {"fragment": "true", "json": "true"}

        elif self.requeast == 'Получить рандомный факт':

            url = f"https://numbersapi.p.rapidapi.com/random/{self.type}"

            querystring = {
                "min": f"{args[2]}",
                "max": f"{args[3]}", "fragment": "true", "json": "true"}


        headers = {
            "X-RapidAPI-Key": "26d3b52910mshb55bda30b26bf08p178e07jsna560331e8b10",
            "X-RapidAPI-Host": "numbersapi.p.rapidapi.com"
        }

        try:
            self.response = requests.get(url, headers=headers, params=querystring)
            return (self.response.json(), self.type)
        except (TimeoutError, ConnectionError):
            return 'error'
