

//could not get gtest to install on my laptop
#include <iostream>
#include <string>
#include <vector>
#include "../player.hpp"
#include "../dealer.hpp"
#include "../table.hpp"

template <typename T>
void assert_eq(const T& expected, const T& actual, const std::string name) {
    if (expected == actual) {
        std::cout << "PASSED: " << name << std::endl;
    } else {
        std::cout << "FAIL: " << name << std::endl;
        std::cout << "\tExpected: " << expected << std::endl;
        std::cout << "\tActual  : " << actual << std::endl;
    }
};

template <typename T>
void assert_ne(const T& expected, const T& actual, const std::string name) {
    if (expected != actual) {
        std::cout << "PASSED: " << name << std::endl;
    } else {
        std::cout << "FAIL: " << name << std::endl;
    }
};

void betTest(){
    std::cout << "BET TEST" << std::endl;
    int startingMoney = 500;
    int bet = 20;
    Player* player = new RealPlayer(startingMoney);
    player->placeBet(bet);
    assert_eq(bet, player->getCurrentBet(), "getCurrentBet");
    assert_eq(startingMoney - bet, player->getCurrentMoney(), "getCurrentMoney");
    assert_eq(Table::getInstance().getTotalMoney(), bet, "Table Get Money");
    assert_eq(Table::getInstance().getCurrentBet(), bet, "Table Get Current Bet");

    delete player;
    std::cout << std::endl;
};

void dealerTest(){
    std::cout << "Dealer Test" << std::endl;
    Dealer dealer;
    Table::getInstance().addPlayers(2, 0, 0, 500);
    dealer.startRound();
    dealer.dealFlop();
    int size = Table::getInstance().flop.size();
    assert_eq(3, size, "Flop");
    
    dealer.dealRiver();
    std::string empty = "";
    assert_ne(empty, Table::getInstance().river.face, "River");

    dealer.dealTurn();
    assert_ne(empty, Table::getInstance().turn.face, "Turn");

    dealer.startRound();
    size = Table::getInstance().flop.size();
    assert_eq(0, size, "Flop After Start Round");
    assert_eq(empty, Table::getInstance().river.face, "River After Start Round");
    assert_eq(empty, Table::getInstance().turn.face, "Turn After Start Round");

    std::cout << std::endl;
}



int main(void){
    betTest();
    dealerTest();
};
