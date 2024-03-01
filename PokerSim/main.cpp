#include "deck.hpp"
#include "playerFactory.hpp"
#include "dealer.hpp"
#include "table.hpp"


void bettingRound(Player* player, int i, int size){
    player = Table::getInstance().getPlayers().at(i);

    while(!Table::getInstance().checkEvenPot(player)){ //after the river
        player->takeTurn(i);
        
        if(i >= size - 1){
            i = 0;
        } else {
            i++;
        }
        player = Table::getInstance().getPlayers().at(i);
    }
}

int main(void){
    
    int real = 0;
    int bots = 0;
    int diff = 0;
    int startingMoney = 0;
    int minimumBet = 0;

    std::cout << "Please enter the number of real players you would like: " << std::endl;
    std::cin >> real;

    std::cout << "Please enter the number of bot players you would like: " << std::endl;
    std::cin >> bots;

    std::cout << "Please enter the difficuly of the bot players:\n1) Easy\n2) Hard" << std::endl;
    std::cin >> diff;

    std::cout << "Please enter starting money: " << std::endl;
    std::cin >> startingMoney;

    std::cout << "Please enter minimum bet: " << std::endl;
    std::cin >> minimumBet;
    Table::getInstance().setBlinds(minimumBet);

    Table::getInstance().addPlayers(real, bots, diff, startingMoney);
    Dealer dealer;
    Player* player;
    //int index;

    bool play = true;
    //bool fold = false;
    while(play){
        int size =  Table::getInstance().getPlayers().size();
        dealer.startRound();
        int i = Table::getInstance().getBigBlindPlayer() + 1;
        if(i >= size){
                i = 0;
        } 

        player = Table::getInstance().getPlayers().at(i);

        while(!Table::getInstance().checkEvenPot(player)){ //before the flop
            player->takeTurn(i);
            if(i >= size - 1){
                i = 0;
            } else {
                i++;
            }
            player = Table::getInstance().getPlayers().at(i);
        }
        if(Table::getInstance().playersRemaining() == 1){
           
        } else {
            dealer.dealFlop();

            int i = Table::getInstance().getSmallBlindPlayer();
            bettingRound(player, i, size);
            if(Table::getInstance().playersRemaining() == 1){
               
            } else {
                dealer.dealTurn();

                int i = Table::getInstance().getSmallBlindPlayer();
                bettingRound(player, i, size);

                if(Table::getInstance().playersRemaining() == 1){
                    
                } else {
                    dealer.dealRiver();

                    int i = Table::getInstance().getSmallBlindPlayer();
                    bettingRound(player, i, size);

                    if(Table::getInstance().playersRemaining() == 1){
                        
                    }
                }
            }
        }
        player = nullptr;
        i = 0;
        int index = 0;
        for(auto& p : Table::getInstance().getPlayers()){ //determining who has the best hand and giving them the money
            if(!p->fold){
                if(player == nullptr){
                    player = p;
                    index = i;
                    
                } else if (dealer.compareHands(p->findBestHand(), player->findBestHand())){
                    player = p;
                    index = i;
                }
            }
            i++;
        }

        std::cout << "Player " << index << " wins! They recieve " << Table::getInstance().getTotalMoney() << std::endl;
        player->addMoney(Table::getInstance().getTotalMoney());


         
        for(int i = 0; i < size;  i++){ //determining if any player is out of money and having them leave
            if(Table::getInstance().getPlayers().at(i)->getCurrentMoney() <= 0){
                std::cout <<"Player " << i << " is out of money. Please Leave the Table\n Everyone above player " << i << " will be moved down one index. (i.e. player "<< i+1<< " becomes "<< i << ")" << std::endl;
                Table::getInstance().removePlayer(i);
                i--;
                size--;
            }
        }

        Table::getInstance().moveBlinds();

        std::string selection;
        std::cout << "Would you like to continue playing? (Y/N) ";
        std::cin >> selection;

        if(selection != "Y" && selection != "y") play = false;

    }
};