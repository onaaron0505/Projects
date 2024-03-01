#pragma once

#include "player.hpp"


class Player;
class RealPlayer;
class botPlayer;

class PlayerFactory{ //factory design
    public:
        static RealPlayer* createReal(int startingMoney);
        static botPlayer* createBot(int startingMoney, int difficulty); //command design
        static void deletePlayer(Player* player);
};