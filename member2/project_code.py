# Game Recommendation Program
# 다양한 게임을 장르별로 추천하는 프로그램

import random

action_games = [
    "Hollow Knight",
    "Cuphead",
    "Devil May Cry 5",
    "Sekiro: Shadows Die Twice",
    "Metal Gear Rising",
    "DOOM Eternal",
    "Bayonetta 2",
]

rpg_games = [
    "Elden Ring",
    "The Witcher 3",
    "Skyrim",
    "Cyberpunk 2077",
    "Dark Souls 3",
    "Monster Hunter World",
    "Persona 5 Royal",
]

casual_games = [
    "Stardew Valley",
    "Animal Crossing",
    "Terraria",
    "Slime Rancher",
    "Overcooked",
    "Among Us",
    "Loop Hero",
]

fps_games = [
    "Valorant",
    "Overwatch 2",
    "Apex Legends",
    "Counter-Strike 2",
    "Rainbow Six Siege",
    "Call of Duty: Warzone",
]

strategy_games = [
    "Civilization VI",
    "Starcraft 2",
    "Age of Empires IV",
    "XCOM 2",
    "Crusader Kings 3",
]

all_games = (
    action_games
    + rpg_games
    + casual_games
    + fps_games
    + strategy_games
)

def recommend_game():
    print("게임 추천 프로그램입니다.")
    print("아래 장르 중 하나를 선택하세요:")
    print("1. 액션")
    print("2. RPG")
    print("3. 캐주얼")
    print("4. FPS")
    print("5. 전략")
    print("6. 랜덤 추천")

    choice = input("번호 입력: ")

    if choice == "1":
        print("추천 게임:", random.choice(action_games))
    elif choice == "2":
        print("추천 게임:", random.choice(rpg_games))
    elif choice == "3":
        print("추천 게임:", random.choice(casual_games))
    elif choice == "4":
        print("추천 게임:", random.choice(fps_games))
    elif choice == "5":
        print("추천 게임:", random.choice(strategy_games))
    elif choice == "6":
        print("랜덤 추천:", random.choice(all_games))
    else:
        print("잘못된 입력입니다. 다시 실행해주세요.")

if __name__ == "__main__":
    recommend_game()
