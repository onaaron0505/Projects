#include "player.hpp"

botPlayer::botPlayer(int startingMoney, int difficulty) : Player{startingMoney}
{
    difficulty_ = difficulty;
}

void botPlayer::easyTurn()
{
    if(Table::getInstance().getCurrentBet() == 0)
    {
        Table::getInstance().manageCheck(this);
    }
    else{
        int bet = Table::getInstance().getCurrentBet();
        this->placeBet(bet);
    }
};

void botPlayer::hardTurn()
{
    if(this->cards[0].value != this->cards[1].value && (this->cards[0].value + 1 != this->cards[1].value) && (this->cards[0].value != this->cards[1].value + 1) && this->cards[0].suit != this->cards[1].suit)
    {
        this->fold = true;
    }
    else{
        if(Table::getInstance().getCurrentBet() == 0)
        {
            Table::getInstance().manageCheck(this);
        }
        else{
            int bet = Table::getInstance().getCurrentBet();
            this->placeBet(bet);
        }
    }
    if(Table::getInstance().river.suit != "")
    {
        if(this->findBestHand()[0] <= 2)
        {
            this->fold = true;
        }
    }
};

void botPlayer::takeTurn(int index)
{
    if(this->difficulty_ == 1)
    {
        easyTurn();
    }
    else if(this->difficulty_ == 2)
    {
        hardTurn();
    }
    else
    {

    }
};