#include "dealer.hpp"

void Dealer::dealCardToPlayer(Player* Player){
    Card card = this->deck.removeTopCard();
    Player->addCard(card);
}

void Dealer::startRound(){
    if(std::cin.eof() != 0) { //clear input stream
        if(std::cin.peek() != -1){
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max()); 
        }
    }

   
    this->deck.clearDeck();
    this->deck.generateDeck();
    this->deck.shuffle();
    Table::getInstance().clearTotalMoney();
    Table::getInstance().clearCurrentBet();
    Table::getInstance().clearCards();

    std::vector<Player*> players = Table::getInstance().getPlayers();
    for(int i = 0; i<2; i++){
        for(Player* player : players){
            player->fold = false;
            this->dealCardToPlayer(player);
        }
    }
    
    players.at(Table::getInstance().getSmallBlindPlayer())->placeBet(Table::getInstance().getSmallBlind());
    players.at(Table::getInstance().getBigBlindPlayer())->placeBet(Table::getInstance().getBigBlind());

};

void Dealer::dealFlop(){
    Table::getInstance().clearCurrentBet();
    this->deck.removeTopCard(); //burn top card
    for(int i = 0; i < 3; i++){
        Table::getInstance().flop.push_back(this->deck.removeTopCard());
    }
};

void Dealer::dealTurn(){
    Table::getInstance().clearCurrentBet();
    this->deck.removeTopCard(); //burn top card
    Table::getInstance().turn = this->deck.removeTopCard();
};

void Dealer::dealRiver(){
    Table::getInstance().clearCurrentBet();
    this->deck.removeTopCard(); //burn top card
    Table::getInstance().river = this->deck.removeTopCard();
};

bool Dealer::compareHands(int p1[2], int p2[2])
{
    if(p1[0] > p2[0])
    {
        return true;
    }
    else if(p1[0] < p2[0])
    {
        return false;
    }
    else if(p1[0] == p2[0])
    {
        if(p1[1] > p2[1])
        {
            return true;
        }
        else if(p1[1] < p2[1])
        {
            return false;
        }
        else{
            return true;
        }
    }
    else{
        return true;
    }
}