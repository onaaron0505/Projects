#pragma once

#include<iostream>
#include "deck.hpp"
#include "table.hpp"

class Dealer {
    private:
        Deck deck;

    public:
        void dealCardToPlayer(Player* Player);
        void startRound();
        void dealFlop();
        void dealTurn();
        void dealRiver();
        bool compareHands(int p1[2], int p2[2]);
         //testing function should be deleted before "release" of game
};  
