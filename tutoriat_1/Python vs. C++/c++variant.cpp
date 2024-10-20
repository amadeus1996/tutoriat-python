#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <sstream>

int countDistinctDigits(int num) {
    std::set<int> digits;
    num = std::abs(num);
    while (num) {
        digits.insert(num % 10);
        num /= 10;
    }
    return digits.size();
}

// ---------------------------------------------------

bool isPunctuation(const char c) {
    return c == ',' || c == '.' || c == '?' || c == '!' || c == ' ';
}

std::string processSentence(const std::string& sentence) {
    std::string removedPunctuation, word, result;
    for (const char& c : sentence) {
        if (!isPunctuation(c)) removedPunctuation += c;
        else if (c == ' ') removedPunctuation += ' ';
    }
    std::stringstream aux(removedPunctuation);
    bool firstWord = true;
    while (aux >> word) {
        if (word.length() > 2)
            std::ranges::reverse(word);
        if (!firstWord)
            result += "-";  // Add hyphen between words
        result += word;
        firstWord = false;
    }
    return result;
}

int main() {
    // SORTARE
    std::vector<int> t = {122, 45, 111, 67, 321, 12, 8, 9, 100};
    std::ranges::sort(t, [](const int a, const int b) {
        const int digits_a = countDistinctDigits(a);
        const int digits_b = countDistinctDigits(b);
        return (digits_a == digits_b) ? (b < a) : (digits_a < digits_b);
    });
    for (const auto &x: t)
        std::cout << x << " ";
    std::cout<<"\n";


    // SIRURI DE CARACTERE
    const std::string sentence = "This!!!! .Is a,,,!? test sentence?..  ";
    std::cout<<processSentence(sentence);
    return 0;
}