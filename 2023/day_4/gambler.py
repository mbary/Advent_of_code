import re
from collections import OrderedDict
from pprint import pprint


class Gambler:
    def __init__(self, file_path) -> None:
        self._raw_cards = open(file_path, 'r', encoding='utf-8').read().splitlines()
        self._parse_cards(self._raw_cards)
        


    def _parse_cards(self, card_list):
        """
        Create an ordered dict of key-value pairs
        Where the key is the card number and tuple containing 
        (winning numbers, selected numbers)
        """
        self.cards = OrderedDict()

        for card in card_list:
            card = re.sub("  ", " ", card)
            card_no = int(re.findall(r"\d+", card.split(":")[0])[0])
            winning_no = tuple([int(x) for x in re.findall(r":\s(.*)\s\|",card)[0].split(" ")])
            selected_no = tuple([int(x) for x in re.findall(r"\|\s(.*)", card)[0].split(" ")])
            self.cards[card_no] = tuple([winning_no, selected_no])


    def calc_card_points(self):
        point_count = 0

        for card_no in self.cards.keys():
            winning_no = set(self.cards[card_no][0])
            selected_no = set(self.cards[card_no][1])
            print('winning ', winning_no)
            print('sel ', selected_no)
            print(winning_no.intersection(selected_no))
            matching_numbers = len(winning_no.intersection(selected_no))
            print(matching_numbers)

            if matching_numbers:
                card_value = 1
                for _ in range(matching_numbers-1):
                    card_value = card_value*2
                
                point_count += card_value

        return point_count



a = Gambler("input.csv")
point_count = a.calc_card_points()
pprint(point_count)