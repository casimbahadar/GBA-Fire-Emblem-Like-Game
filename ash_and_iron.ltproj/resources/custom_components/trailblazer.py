from app.data.components.base_components import SkillComponent
import app.data.components.component_catalog as cc

ROUGH = {'Forest', 'Hill', 'Mountain'}

class Trailblazer(SkillComponent):
    nid = 'Trailblazer'
    desc = 'Move +1 on Forest, Hill, Mountain terrain'
    tag = cc.SkillTags.MOVEMENT
    author = 'AshAndIron'

    def movement_cost(self, unit, terrain_nid):
        if terrain_nid in ROUGH:
            return 1
        return None
