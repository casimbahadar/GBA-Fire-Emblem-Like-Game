from app.data.components.base_components import SkillComponent
import app.data.components.component_catalog as cc

class NobleCause(SkillComponent):
    nid = 'Noble_Cause'
    desc = 'Adjacent allies gain +2 DEF and RES'
    tag = cc.SkillTags.PASSIVE
    author = 'AshAndIron'

    def aura_stat_change(self, unit, target):
        return {'DEF': 2, 'RES': 2}

    def aura_range(self, unit):
        return 1

    def aura_target(self, unit, target):
        return target.team == unit.team and target is not unit
