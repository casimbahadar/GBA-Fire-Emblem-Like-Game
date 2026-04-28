from app.data.components.base_components import SkillComponent
import app.data.components.component_catalog as cc

class Resolve(SkillComponent):
    nid = 'Resolve'
    desc = 'When HP <= 50%, +4 STR and SKL'
    tag = cc.SkillTags.COMBAT
    author = 'AshAndIron'

    def stat_change(self, unit):
        if unit.get_hp() / unit.stats['HP'] <= 0.5:
            return {'STR': 4, 'SKL': 4}
        return {}
