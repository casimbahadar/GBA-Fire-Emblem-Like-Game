from app.data.components.base_components import SkillComponent
import app.data.components.component_catalog as cc

class LuckySeven(SkillComponent):
    nid = 'Lucky_Seven'
    desc = 'First 7 turns: +20 Hit and Avoid'
    tag = cc.SkillTags.COMBAT
    author = 'AshAndIron'

    def stat_change(self, unit):
        from app.engine import game_state
        try:
            if game_state.game.turncount <= 7:
                return {'HIT': 20, 'AVO': 20}
        except Exception:
            pass
        return {}
