# -*- coding: utf-8 -*-
"""Main story.
"""
## path setting
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
## public libs
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
## assets
from storybuilder.assets import basic, accessory
## settings
from config import PERSONS, AREAS, STAGES, DAYS, TIMES, ITEMS, WORDS, RUBIS, LAYERS
## local files
from src.episodes.e1_lastwalk import ep_lastwalk
from src.episodes.e2_change import ep_change_our
from src.episodes.e3_enjoy import ep_enjoytime
from src.episodes.e4_firststep import ep_firststep


## define alias
W = Writer
_ = Writer.getWho()

################################################################
#
#   1. 別れの幅
#   2. 陰りの幅
#   3. 楽しみの幅
#   4. 告白の幅
#
################################################################


## main
def ch_main(w: World):
    return w.chapter("main",
            ep_lastwalk(w),
            ep_change_our(w),
            ep_enjoytime(w),
            ep_firststep(w),
            )

def create_world():
    """Create a world.
    """
    w = World("歩幅")
    w.setCommonData()
    w.setAssets(basic.ASSET)
    w.setAssets(accessory.ASSET)
    w.buildDB(PERSONS,
            AREAS, STAGES, DAYS, TIMES, ITEMS, WORDS,
            RUBIS, LAYERS)
    w.setBaseDate(2020)
    w.setBaseArea("Tokyo")
    # set textures
    # w.entryBlock()
    # w.entryHistory()
    # w.entryLifeNote()
    w.setOutline("高校生の二人は別れの時を迎える。何故そうなったのか、自分たちの歩幅の違いがすれ違いを生み出していたのだと気づく")
    return w


def main(): # pragma: no cover
    w = create_world()
    return w.build(
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

