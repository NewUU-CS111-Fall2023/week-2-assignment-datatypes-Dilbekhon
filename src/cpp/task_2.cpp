/*
 * Author: Dilbekkhon
 * Date: 25-10-2023
 * Name: Guess the Number
 */



#include <iostream>
#include <cstdlib>
#include <ctime>

int main() {
    srand(time(0)); 
    int secretNumber = rand() % 100 + 1;

    std::cout << "Welcome to the Guess the Number game!" << std::endl;
    std::cout << "Try to guess the number between 1 and 100." << std::endl;

    int guess, attempts = 0;

    while (true) {
        std::cout << "Enter your guess: ";
        std::cin >> guess;
        attempts++;

        if (guess == secretNumber) {
            std::cout << "Congratulations! You guessed the number " << secretNumber << " in " << attempts << " attempts." << std::endl;
            break;
        } else if (guess < secretNumber) {
            std::cout << "Too low! Try again." << std::endl;
        } else {
            std::cout << "Too high! Try again." << std::endl;
        }
    }

    return 0;
}
