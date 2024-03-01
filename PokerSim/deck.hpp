#pragma once

#include<iostream>
#include<vector>
#include<algorithm>
#include <cstdlib>
#include <ctime>
#include <sstream>

struct Card {
    std::string suit;
    std::string face;
    int value; //face cards will take their value (i.e. jack-11, queen-12, king-13, ace-14)
    std::string getName();
};

class Deck {
    private:
        std::vector<Card> cards;
        std::string suits[4] = {"Spades" , "Clubs", "Diamonds", "Hearts"};
        std::string faces[13] = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"};
    public:
        void generateDeck();
        void shuffle();
        Card removeTopCard();
        void clearDeck();

        void showDeck(); //testing function should be deleted before "release" of game
};  