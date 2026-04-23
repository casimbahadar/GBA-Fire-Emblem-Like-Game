from app.data.components.base_components import SkillComponent
import app.data.components.component_catalog as cc
import random

class Pavise(SkillComponent):
    nid = 'Pavise'
    desc = '30% chance to halve physical damage'
    tag = cc.SkillTags.COMBAT
    author = 'AshAndIron'

    def damage_formula_reduce(self, unit, item, damage):
        if random.randint(0, 99) < 30 and item and not getattr(item, 'magic', False):
            return damage // 2
        return damage
