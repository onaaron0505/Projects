#pragma once

#include "player.hpp"


class RealPlayer : public Player {
    public:
        RealPlayer() : Player(){};
        ~RealPlayer(){};
        void takeTurn() override;
};  