#include "table.hpp"

std::vector<Player*> Table::getPlayers() const{
    return this->players;
};

void Table::addPlayers(int nReal, int nBots, int difficulty, int startingMoney){
    for(int i = 0; i < nReal; i++){
        this->players.push_back(PlayerFactory::createReal(startingMoney));

    }
    for(int i = 0; i < nBots; i++){
        this->players.push_back(PlayerFactory::createBot(startingMoney, difficulty));
    }
};

void Table::manageCheck(Player* newPlayer){
    if(this->currentBet.player == nullptr){
        this->currentBet.player = newPlayer;
    }
};

void Table::addBet(int newBet, int oldBet, Player* player){
    int totalBet = newBet + oldBet;
    if(this->currentBet.money > totalBet && player->getCurrentMoney() != newBet){
        std::stringstream error;
        error << "Bet must be higher or equal than the current bet of " << this->currentBet.money;
        throw std::runtime_error(error.str());
    }
    if(this->currentBet.money < totalBet){
        this->currentBet.money = totalBet;
        this->currentBet.player = player;
    }
    this->totalMoney += newBet;
};

int Table::getTotalMoney() const{
    return this->totalMoney;
};

void Table::setBlinds(int minimumBet){
    this->smallBlind = minimumBet/2;
    this->bigBlind = minimumBet;
    this->currentBigBlindIndex = 1;
    this->currentSmallBlindIndex = 0;
};

int Table::getBigBlind() const{
    return this->bigBlind;
};

int Table::getSmallBlind() const{
    return this->smallBlind;
};

void Table::moveBlinds(){
    int size = this->players.size();
    if(this->currentSmallBlindIndex + 1 == size)
        this->currentSmallBlindIndex = 0;
    else
        this->currentSmallBlindIndex += 1;
    
    if(this->currentBigBlindIndex + 1 == size)
        this->currentBigBlindIndex = 0;
    else 
        this->currentBigBlindIndex += 1;
};

int Table::getSmallBlindPlayer() const{
    return this->currentSmallBlindIndex;
};

int Table::getBigBlindPlayer() const{
    return this->currentBigBlindIndex;
};  

bool Table::checkEvenPot(Player* Player) const{
    if(Player == this->currentBet.player) return true;
    return false;
};

void Table::freePlayers(){
    for (auto player : this->players) {
        PlayerFactory::deletePlayer(player);
    }
};

int Table::getCurrentBet(){
    return this->currentBet.money;
}

void Table::printCards(){
    std::cout << "\t\tFlop: " << std::endl;
    for(auto& card : this->flop){
        std::cout << "\t\t\t" << card.getName() << std::endl;
    }
    std::cout << "\t\tTurn: \n\t\t\t" << this->turn.getName() << std::endl;
    std::cout << "\t\tRiver: \n\t\t\t" << this->river.getName() << std::endl;
}

void Table::removePlayer(int index){
    delete this->players[index];
    this->players.erase(this->players.begin() + index);
}

void Table::clearTotalMoney(){
    this->totalMoney = 0;
};

void Table::clearCurrentBet(){
    this->currentBet.money = 0;
    this->currentBet.player = nullptr;
    for(auto& player : this->players){
        player->clearCurrentBet();
    }
};

int Table::playersRemaining(){
    int count = 0;
    for(auto& player : this->players){
        if(!player->fold) count++;
    }
    return count;
};

void Table::clearCards(){
    this->flop.clear();
    this->turn.face = "";
    this->turn.suit = "";
    this->turn.value = 0;
    this->river.face = "";
    this->river.suit = "";
    this->river.value = 0;
    for(auto& p : Table::getInstance().getPlayers()){
        p->clearCards();
    }
}

Table::~Table(){
    for(auto& player : this->players){
        PlayerFactory::deletePlayer(player);
    }
};