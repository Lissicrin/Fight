class Character:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def be_attacked(self, enemy_damage):
        self.health = self.health - enemy_damage
        if self.health <= 0:
            print("Вы умерли, придется все по новой...")


win = False
hits = 0
player1 = Character(80, 10)
player2 = Character(80, 10)

while not win:
    player1.be_attacked(player2.damage)
    if player1.health <= 0:
        print("player2 победил")
        print(f"у него осталось {player2.health}")
        win = True
    player2.be_attacked(player1.damage)
    if player2.health <= 0:
        print("player1 победил")
        print(f"у него осталось {player1.health}")
        win = True
    hits += 1
    print(hits, player1.health, player2.health)





# player = Character(330, 10)
# print(player.health)
# player.be_attacked(329)
# print(player.health)
# player.be_attacked(2)



