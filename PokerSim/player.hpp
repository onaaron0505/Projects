#pragma once

#include <iostream>
#include <vector>
#include <map>
#include <stdexcept>
#include "deck.hpp"
#include "table.hpp"

class Player { 
    protected:
        std::vector<Card> cards;
    private:
        int totalMoney;
        int currentBet;

    public:
        virtual ~Player(){};
        Player(int startingMoney);
        void addCard(Card card);
        int* findBestHand();
        virtual void takeTurn(int index) = 0; //abstract class
        void placeBet(int money);
        void printCards();
        int getCurrentMoney();
        void addMoney(int money);
        bool fold; //state design pattern
        void clearCurrentBet();
        int getCurrentBet() const;
        void clearCards();
    
};  

class RealPlayer : public Player {
    public:
        RealPlayer(int startingMoney);
        ~RealPlayer(){};
        void takeTurn(int index) override;
};  

class botPlayer : public Player {
    private:
        int difficulty_;
    public:
        botPlayer(int startingMoney, int difficulty);
        ~botPlayer(){};
        void easyTurn();
        void hardTurn();
        void takeTurn(int index) override;
};  