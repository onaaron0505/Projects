#include "player.hpp"

Player::Player(int startingMoney){
    this->totalMoney = startingMoney;
    this->fold = false;
};

void Player::addCard(Card card){
    this->cards.push_back(card);
};

int* Player::findBestHand(){ //to implement
    
    int highCard0 = 0;
    int highCard1 = 0;
    int highCard2 = 0;
    int highCard3 = 0;
    int highCard4 = 0;
    int highCard5 = 0;
    int highCard6 = 0;
    int highCard7 = 0;
    //bool royal_flush = false; score = 9
    bool straight_flush = false; // score = 8
    bool four = false; // score = 7
    bool full_house = false; // score = 6
    bool flush = false; // score = 5
    bool straight = false; // score = 4
    bool three = false; // score = 3
    bool two_pair = false; // score = 2
    bool pair = false; // score = 1
    // high card score = 0
    int numPairs = 0;
    std::vector<Card> fullHand;
    std::vector<int> valueHand;
    fullHand.push_back(this->cards[0]);
    fullHand.push_back(this->cards[1]);
    fullHand.push_back(Table::getInstance().flop[0]);
    fullHand.push_back(Table::getInstance().flop[1]);
    fullHand.push_back(Table::getInstance().flop[2]);
    fullHand.push_back(Table::getInstance().turn);
    fullHand.push_back(Table::getInstance().river);

    valueHand.push_back(this->cards[0].value);
    valueHand.push_back(this->cards[1].value);
    valueHand.push_back(Table::getInstance().flop[0].value);
    valueHand.push_back(Table::getInstance().flop[1].value);
    valueHand.push_back(Table::getInstance().flop[2].value);
    valueHand.push_back(Table::getInstance().turn.value);
    valueHand.push_back(Table::getInstance().river.value);

    std::sort(valueHand.begin(), valueHand.end());
    highCard0 = valueHand[6];
    
    int counter = 0;
    for(int x = (int)valueHand.size()-1; x > 0; x--)
    {
        counter = 1;

        for(int y = (int)valueHand.size()-1; y > 0; y--)
        {
            if(valueHand[y] == valueHand[y-1] + 1)
            {
                counter++;
            }
            else if(valueHand[y] == valueHand[y-1])
            {

            }
            else{
                break;
            }
        }
        if(counter == 5)
            {
                straight = true;
                highCard4 = x;
                break;
            }
    }


    std::map<int, int> valueMap;
    std::map<std::string, int> suitMap;

    for(int i = 2; i <= 14; i++)
    {
        valueMap[i] = 0;
    }

    suitMap["Spades"] = 0;
    suitMap["Clubs"] = 0;
    suitMap["Diamonds"] = 0;
    suitMap["Hearts"] = 0;

    for(long unsigned int j = 0; j < fullHand.size(); j++)
    {
        suitMap[fullHand[j].suit]++;
        valueMap[fullHand[j].value]++;
    }

    if(suitMap["Spades"] == 5 || suitMap["Clubs"] == 5 || suitMap["Diamonds"] == 5 || suitMap["Hearts"] == 5)
    {
        flush = true;
        highCard5 = valueHand[6];
    }
    for(int k = 2; k <= 14; k++)
    {
        if(valueMap[k] == 4)
        {
            four = true;
            highCard7 = k;
        }
        if(valueMap[k] == 3)
        {
            three = true;
            highCard3 = k;
        }
        if(valueMap[k] == 2)
        {
            pair = true;
            highCard1 = k;
            highCard2 = k;
            numPairs++;
        }
    }
    if(numPairs >= 2)
    {
        two_pair = true;
    }
    if(three == true && pair == true)
    {
        full_house = true;
    }
    if(straight == true && flush == true)
    {
        straight_flush = true;
    }


    // hand checks
    if(straight_flush == true)
    {
        static int array[] = {8, highCard4};
        return array;
    }
    else if(four == true)
    {
        static int array[] = {7, highCard7};
        return array;
    }
    else if(full_house == true)
    {
        static int array[] = {6, highCard6};
        return array;
    }
    else if(flush == true)
    {
        static int array[] = {5, highCard5};
        return array;
    }
    else if(straight == true)
    {
        static int array[] = {4, highCard4};
        return array;
    }
    else if(three == true)
    {
        static int array[] = {3, highCard3};
        return array;
    }
    else if(two_pair == true)
    {
        static int array[] = {2, highCard2};
        return array;
    }
    else if(pair == true)
    {
        static int array[] = {1, highCard1};
        return array;
    }
    else
    {
        static int array[] = {0, highCard0};
        return array;
    }
};

void Player::placeBet(int money){
    try{
        if(this->totalMoney < (this->currentBet + money)) throw std::runtime_error("Please enter an amount of money that you have"); //exception handling
        Table::getInstance().addBet(money, this->currentBet, this);
        this->currentBet += money;
        this->totalMoney -= money;
    } catch(std::runtime_error& error){ //this is technically only for real players, but a bot should never give less than the right amount
        std::cout << error.what() << std::endl;
        std::cin.clear(); 
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 
        std::cin >> money;
        placeBet(this->currentBet + money);
    }
};

void Player::printCards(){
    std::cout << "Current Hand: " << std::endl;
    std::cout <<"\tYour Cards: " << std::endl;
    for(auto& card : this->cards){
        std::cout << "\t\t" << card.getName() << std::endl;
    };

    std::cout << "\tPublic Cards: " << std::endl;
    Table::getInstance().printCards();

    std::cout << "End of Hand" << std::endl;
};

int Player::getCurrentMoney(){
    return this->totalMoney;
};

void Player::addMoney(int money){
    this->totalMoney += money;
};

void Player::clearCurrentBet(){
    this->currentBet = 0;
};

int Player::getCurrentBet() const{
    return this->currentBet;
}

void Player::clearCards(){
    this->cards.clear();
}