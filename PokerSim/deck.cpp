#include "deck.hpp"

void Deck::generateDeck(){
    for(std::string suit : this->suits){
        for(int i = 2; i <= 14; i++){
            Card card;
            card.suit = suit;
            card.value = i;
            card.face = this->faces[i-2];
            this->cards.push_back(card);
        }
    }
};

void Deck::shuffle(){
    int size = this->cards.size();
    std::srand(std::time(nullptr)); //have to seed ran or else it gives same values every time. 

    for(int i = 0; i < size; i++){
        int rand =  std::rand() % size;
        std::swap(this->cards[i], this->cards[rand]);
    }
};

Card Deck::removeTopCard(){
    Card card = this->cards.back();
    this->cards.pop_back();
    return card;
};

void Deck::showDeck(){
    for(Card card : this->cards){
        std::cout << card.face << " of " << card.suit << std::endl;
    } 
};

void Deck::clearDeck(){
    this->cards.clear();
}

std::string Card::getName(){
    std::stringstream card;
    if(this->value > 0)
        card << this->face << " of " << this->suit;
    return card.str();
};