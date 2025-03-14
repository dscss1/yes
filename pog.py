import random

def select_card():
    """Функція для отримання випадкової карти."""
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return random.choice(cards)

def calculate_hand_value(hand):
    """Функція для розрахунку значення руки."""
    value = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    hand_value = 0
    number_of_aces = 0

    for card in hand:
        hand_value += value[card]
        if card == 'A':
            number_of_aces += 1

    while number_of_aces > 0 and hand_value > 21:
        hand_value -= 10
        number_of_aces -= 1

    return hand_value

def main():
    player_hand = []
    while True:
        choice = input("Бажаєте взяти карту? (так/ні): ").lower()

        if choice != 'так':
            break

        card = select_card()
        player_hand.append(card)
        print(f"Ваша рука: {', '.join(player_hand)}")
        hand_value = calculate_hand_value(player_hand)
        print(f"Сума ваших карт: {hand_value}")

        if hand_value > 21:
            print("Перебір! Ви програли.")
            break

    print("Гра завершена.")

if __name__ == "__main__":
    main()
