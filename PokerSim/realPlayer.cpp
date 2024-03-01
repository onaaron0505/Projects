#include "player.hpp"

RealPlayer::RealPlayer(int startingMoney) : Player{startingMoney}{}; 

void RealPlayer::takeTurn(int index){
    if(this->fold) return;
    std::cout << "\n\nPlayer " << index << " take your turn" << std::endl;
    std::cout << "The current pot is: " << Table::getInstance().getTotalMoney() << std::endl;
    std::cout << "The current bet is: " << Table::getInstance().getCurrentBet() << std::endl;
    std::cout << "Your current bet is: " << this->getCurrentBet() << std::endl;
    std::cout << "Your current money is: " << this->getCurrentMoney() << std::endl;
    this->printCards();
    int option;
    std::cout << "Please select a number\n1) Bet\n2) Fold" << std::endl;
    if(Table::getInstance().getCurrentBet() == 0){
        std::cout << "3) Check" << std::endl; 
    } 
    std::cin >> option;
    while (std::cin.fail() || (!Table::getInstance().getCurrentBet() == 0 && option == 3) || option > 3 || option < 1) {
        std::cout << "Invalid Input. Please enter one of the options" << std::endl;
        std::cin.clear(); // clear the fail flag
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // discard the invalid input
        std::cin >> option;
    }
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    if (option == 1){
        std::cout << "How much would you like to bet?: ";
        int bet;
        std::cin >> bet;
        while(std::cin.fail()){
            std::cout << "Invalid Input. Please enter a number for the bet" << std::endl;
            std::cin.clear(); // clear the fail flag
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // discard the invalid input
            std::cin >> bet;
        }
        this->placeBet(bet);
    } else if (option == 2){
        this->fold = true;
    } else if (option == 3){
        Table::getInstance().manageCheck(this);
    }
};