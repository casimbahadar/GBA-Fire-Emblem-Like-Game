from app.data.components.base_components import SkillComponent
import app.data.components.component_catalog as cc

class Renewal(SkillComponent):
    nid = 'Renewal'
    desc = 'Restore 20% max HP each player phase'
    tag = cc.SkillTags.PASSIVE
    author = 'AshAndIron'

    def on_upkeep(self, actions, playback, unit):
        heal = max(1, unit.stats['HP'] // 5)
        if unit.get_hp() < unit.stats['HP']:
            actions.append(('change_hp', unit, heal))
