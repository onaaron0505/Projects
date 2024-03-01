#include "playerFactory.hpp"

RealPlayer* PlayerFactory::createReal(int startingMoney){
    return new RealPlayer(startingMoney);
};

botPlayer* PlayerFactory::createBot(int startingMoney, int difficulty){
    return new botPlayer(startingMoney, difficulty);
};

void PlayerFactory::deletePlayer(Player* player){
    delete player;
};