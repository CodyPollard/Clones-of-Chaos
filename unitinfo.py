# Unit info file to hold various stats about unit types in CoC

# Army Units
# Soldier
class Soldier():
    description = "Standard offensive army unit available to all players from the start. The soldier has the \n" \
                  "lowest base strength of all offensive units but is also the cheapest. Can be equiped with \n" \
                  "all standard weapons with a limit of one. Soldiers only contribute towards your army's offensive \n" \
                  "strength and do not aid in the defense of your castle."
    strength = 5
    hp = 20

# Guard
class Guard():
    description = "Standard defensive army unit available to all players from the start. The guard has the \n" \
                  "lowest base strength of all defensive units but is also the cheapest. Can be equiped with \n" \
                  "all standard weapons with a limit of one. Guards only contribute towards your army's defense \n" \
                  "strength and do not aid in attacking other players."
    strength = 5
    hp = 20

# Spy
class Spy():
    description = "Standard offensive espionage unit available to all players from the start. Spies are used \n" \
                  "to gain intelligence on an enemy and in some cases can sabotage enemy Guard's weapons. A \n" \
                  "sabotaged weapon will break when used giving the guard no bonus damage. It will not show \n" \
                  "up as broken until the unit uses it in battle giving you an offensive edge."
    strength = 5
    hp = 20

# Sentry
class Sentry():
    description = "Standard defensive espionage unit available to all players from the start. Sentries are used \n" \
                  "to defend against enemy spies and can sometimes capture multiple spies given a large enough \n" \
                  "strength advantage."
    strength = 5
    hp = 20








# Run unitinfo.py to run these tests
if __name__ == "__main__":
    s = Soldier()
    print(s.description)