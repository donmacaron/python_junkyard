from classes import *

class Character:
    def __init__(self, name='', char_class=TEMPLATE(), char_race='Человек', ab_scores={}):
        self.name = name
        self.char_class = char_class
        self.char_race = char_race
        self.level = 1
        self.hp_base = char_class.hp
        self.ab_scores = ab_scores
        self.main_stats = {'ac': 10+self.ab_scores['dex'], 'speed': 30,
                           'hitdice': char_class.hitdice, 'hp': self.hp_base + self.ab_scores_mod(self.ab_scores['con']),
                           'prof_bonus': 2}
        if char_class.spellcast_ab != 'none':
            self.spellcast_ab = {key:self.ab_scores[key] for key in [char_class.spellcast_ab]}
            self.spellcast_ab_name = list(self.spellcast_ab.keys())[0]
            self.spell_dc = 8 + self.main_stats['prof_bonus'] + self.spellcast_ab[self.spellcast_ab_name]
            self.spell_attk = self.ab_scores_mod(self.spellcast_ab[self.spellcast_ab_name]) + self.main_stats['prof_bonus']
            self.spells_known = round(self.level/2+.4) + self.spellcast_ab[self.spellcast_ab_name]
        else:
            self.spellcast_ab = 0
            self.spellcast_ab_name = 'none'
            self.spells_known = 0

        self.cantrips_known = char_class.cantrips_known

        self.spells_slots = char_class.spells_slots
        self.equipment = char_class.equipment
        self.profs = char_class.profs
        self.traits = char_class.traits


    def __str__(self):
        return self.char_race +', известный как ' + self.name + ',\nпо жизни тупо ' + self.char_class.name


    def ab_scores_mod(self, a=10):
        return round(((a-10)/2)-.4)


    def charsheet_init(self):
        charsheet = ''
        with open('charsheet.txt') as fp:
           line = fp.readline()
           cnt = 1
           while line:
               charsheet += line
               line = fp.readline()
               cnt += 1
        return charsheet


    def charsheet_fill(self):
        stats = (self.name, self.char_race, self.char_class, self.level)
        self.main_stats
        self.ab_scores
        spellcast = (self.spellcast_ab_name, self.spellcast_ab)
        spells = (self.cantrips_known, self.spells_known, self.spells_slots)
        charsheet = self.charsheet_init()
        stat_counter = 0
        mainstat_counter = 0
        abscore_counter = 0
        spellcast_counter = 0
        spells_counter = 0
        mod_counter = 0
        res = ''
        for line in charsheet.splitlines():
            if line.find('_value') is not -1:
                line = line.replace('_value', str(stats[stat_counter]))
                stat_counter += 1
            if line.find('_main_stats') is not -1:
                line = line.replace('_main_stats', str(list(self.main_stats.values())[mainstat_counter]))
                mainstat_counter += 1
            if line.find('_ab_score') is not -1:
                line = line.replace('_ab_score', str(list(self.ab_scores.values())[abscore_counter]))
                abscore_counter += 1
            if line.find('_mod') is not -1:
                line = line.replace('_mod', str(self.ab_scores_mod(list(self.ab_scores.values())[mod_counter])))
                mod_counter += 1
            if line.find('_spellcast') is not -1:
                line = line.replace('_spellcast', str(spellcast[spellcast_counter]).upper())
                spellcast_counter = 1
            if line.find('_profs') is not -1:
                line = line.replace('_profs', self.profs)
            if line.find('_traits') is not -1:
                line = line.replace('_traits', self.traits)
            if line.find('_equip') is not -1:
                line = line.replace('_equip', self.equipment)
            if line.find('_spells') is not -1:
                line = line.replace('_spells', str(spells[spells_counter]))
                spells_counter += 1
            res += line + '\n'
        return res
