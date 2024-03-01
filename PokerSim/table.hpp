#pragma once

#include <sstream>
#include "player.hpp"
#include "deck.hpp"
#include "playerFactory.hpp"

class Player;

struct Bet{
    Player* player;
    int money;
};

class Table{
    public: 
        std::vector<Card> flop;
        Card turn;
        Card river;
        
        
        static Table& getInstance(){
		    static Table instance;
		    return instance;
	    }
        Table(Table const& ) = delete; // copy constructor;
        Table& operator=(Table const&) = delete; // copy assignment
        Table(Table &&) = delete; // move constructor
        Table& operator = (Table &&) = delete; // move assignment
        ~Table();

        
        std::vector<Player*> getPlayers() const;
        void addPlayers(int nReal, int nBots, int difficulty, int startingMoney);
        void addBet(int newBet, int oldBet, Player* player);
        int getTotalMoney() const;
        void setBlinds(int minimumBet);
        int getBigBlind() const;
        int getSmallBlind() const;
        void moveBlinds();
        int getSmallBlindPlayer() const;
        int getBigBlindPlayer() const;
        bool checkEvenPot(Player* Player) const;  
        void freePlayers();
        int getCurrentBet();
        void printCards();
        void removePlayer(int index);
        void manageCheck(Player* player);
        void clearTotalMoney();
        void clearCurrentBet();
        int playersRemaining();
        void clearCards();
    
    private:
        Table(){}
        Bet currentBet;
        int smallBlind;
        int bigBlind;
        int totalMoney;
        int currentBigBlindIndex;
        int currentSmallBlindIndex;
        std::vector<Player*> players;
};