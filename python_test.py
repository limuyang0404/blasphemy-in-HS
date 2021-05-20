# -*- coding: utf-8 -*-
class Card(object):
    def __init__(self, health=3):
        super(Card,self).__init__()
        self.health = health
    def __del__(self):
        print('ea!')
    def take_damage(self):
        self.health -= 1
        return
class Slaver(Card):
    def __init__(self):
        super(Slaver,self).__init__()
        self.health = 3
    def take_damage(self):
        if self.health >1:
            self.health -= 1
            return Slaver()
        elif self.health == 1:
            self.health = 0
            return
class BattleGround(object):
    def __init__(self):
        super(BattleGround, self).__init__()
        self.left_battle_ground = []
        self.right_battle_ground = []
        self.new_list = []
        self.left_new_list = []
        self.right_new_list = []
        self.left_new = None
        self.right_new = None
        self.time = 0
        self.left_HP = []
        self.right_HP = []
    def add_card(self, card, side):
        if side == 'left':
            if len(self.left_battle_ground)<7:
                self.left_battle_ground.append(card)
            else:
                pass
        elif side == 'right':
            if len(self.right_battle_ground)<7:
                self.right_battle_ground.append(card)
            else:
                pass
    def take_damage(self):
        if len(self.left_battle_ground)>0:
            for i in self.left_battle_ground:
                self.left_new = i.take_damage()
                if self.left_new:
                    self.left_new_list.append(self.left_new)
        if len(self.right_battle_ground)>0:
            for j in self.right_battle_ground:
                self.right_new = j.take_damage()
                if self.right_new:
                    self.right_new_list.append(self.right_new)
        if len(self.left_new_list)>0:
            for i in range(len(self.left_new_list)):
                self.add_card(Slaver(), 'left')
        if len(self.right_new_list)>0:
            for i in range(len(self.right_new_list)):
                self.add_card(Slaver(), 'right')
        self.left_new_list = []
        self.right_new_list = []
        self.remove_card()
    def health_check(self):
        self.left_HP = []
        self.right_HP = []
        if len(self.left_battle_ground)>0:
            for i in range(len(self.left_battle_ground)):
                self.left_HP.append(self.left_battle_ground[i].health)
        if len(self.right_battle_ground)>0:
            for i in range(len(self.right_battle_ground)):
                self.right_HP.append(self.right_battle_ground[i].health)
    def blasphemy(self):
        while self.time <8:
            self.take_damage()
            print('The' + str(self.time) + 'th blasphemy:')
            print('Left battle ground:', self.left_battle_ground, '\nRight battle ground:', self.right_battle_ground)
            self.health_check()
            print('Left HP:', self.left_HP, '\nRight HP:', self.right_HP)
            self.time += 1
            for i in self.left_battle_ground:
                if i.health == 1:
                    self.blasphemy()
            for j in self.right_battle_ground:
                if j.health ==1:
                    self.blasphemy()
    def remove_card(self):
        if len(self.left_battle_ground)>0:
            for i in range(len(self.left_battle_ground)):
                if self.left_battle_ground[i].health >0:
                    self.new_list.append(self.left_battle_ground[i])
            self.left_battle_ground = self.new_list
        self.new_list = []
        if len(self.right_battle_ground)>0:
            for i in range(len(self.right_battle_ground)):
                if self.right_battle_ground[i].health >0:
                    self.new_list.append(self.right_battle_ground[i])
            self.right_battle_ground = self.new_list
        self.new_list = []


if __name__=='__main__':
    desk = BattleGround()
    desk.add_card(Card(health=1), side='left')
    print(desk.left_battle_ground, '\n', desk.right_battle_ground)
    desk.add_card(Card(health=2), side='right')
    print(desk.left_battle_ground, '\n', desk.right_battle_ground)
    desk.add_card(Card(health=3), side='left')
    print(desk.left_battle_ground, '\n', desk.right_battle_ground)
    desk.add_card(Card(health=4), side='right')
    print(desk.left_battle_ground, '\n', desk.right_battle_ground)
    desk.add_card(Slaver(), side='left')
    print(desk.left_battle_ground, '\n', desk.right_battle_ground)
    print('_________________')
    desk.blasphemy()









