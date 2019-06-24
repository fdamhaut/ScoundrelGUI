from Scoundrel import settings as s


class Player:
    life = s.MAX_LIFE
    weaponAtk = s.STARTING_WPN[0]
    weaponDur = s.STARTING_WPN[1]

    def heal(self, amount):
        self.life = min(self.life+amount, s.MAX_LIFE)
        return True

    def fight(self, amount):
        if self.weaponDur > amount:
            self.weaponDur = amount
        else:
            self.weaponAtk = 0
            self.weaponDur = -1

        self.life -= max(amount-self.weaponAtk, 0)
        return self.life > 0

    def equip(self, amount):
        self.weaponAtk = amount
        self.weaponDur = 15
        return True

    def score(self):
        return self.life

    def __repr__(self):
        return 'You have ' + str(self.life) + ' health and are equipped with a lvl ' + str(self.weaponAtk) + \
                ' weapon, which you just used to slay a lvl ' + str(self.weaponDur) + ' monster'
