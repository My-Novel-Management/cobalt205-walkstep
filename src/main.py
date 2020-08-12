#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Story: "title"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.assets import basic
from storybuilder.assets import common_rubi
from config import ASSET
# import scenes
from scenes import Riverbed


################################################################
#
#   1. Initialize
#   2. Story memo
#   3. Structure    - 1/8: 1K
#   4. Spec
#   5. Plot         - 1/4: 2K
#   6. Scenes
#   7. Conte        - 1/2: 4K
#   8. Layout
#   9. Draft        - 1/1: 8K
#
################################################################


# Constant
TITLE = "歩幅"
MAJOR, MINOR, MICRO = 1, 1, 0
COPY = "その瞬間だけ、君に会える"
ONELINE = "高校生の二人は初めて付き合い、そして別れた。それだけの物語"
OUTLINE = "約8000字の恋愛短編。別れることになってしまった高校生の二人。何故そうなったのかを振り返ってみた"
THEME = "思いのすれ違い"
GENRE = "恋愛／青春"
TARGET = "10-30years"
SIZE = "8K"
CONTEST_INFO = "コバルト短編小説新人賞第204回応募作"
CAUTION = ""
NOTE = ""
SITES = ["エブリスタ", "小説家になろう", "ノベルアッププラス", "カクヨム"]
TAGS = ["恋愛", "女主人公", "青春", "高校生"]
RELEASED = (8, 1, 2020)


# episodes
def ep1(w: World):
    return w.episode("１",
            Riverbed.sc_lastwalk(w),
            )

def ep2(w: World):
    return w.episode("２",
            Riverbed.sc_rainy(w),
            Riverbed.sc_apart(w),
            )

def ep3(w: World):
    return w.episode("３",
            Riverbed.sc_handdistance(w),
            )

def ep4(w: World):
    return w.episode("４",
            Riverbed.sc_confession(w),
            Riverbed.sc_samestep(w),
            Riverbed.sc_samestep2(w),
            Riverbed.sc_samestep3(w),
            )


# chapters
def ch_main(w: World):
    return w.chapter("main",
            ep1(w),
            ep2(w),
            ep3(w),
            ep4(w),
            )


# main
def main(): # pragma: no cover
    w = World.create_world(f"{TITLE}")
    w.config.set_version(MAJOR, MINOR, MICRO)
    w.db.set_from_asset(basic.ASSET)
    w.db.set_from_asset(common_rubi.ASSET)
    w.db.set_from_asset(ASSET)
    # spec
    w.config.set_copy(f"{COPY}")
    w.config.set_oneline(f"{ONELINE}")
    w.config.set_outline(f"{OUTLINE}")
    w.config.set_theme(f"{THEME}")
    w.config.set_genre(f"{GENRE}")
    w.config.set_target(f"{TARGET}")
    w.config.set_size(f"{SIZE}")
    w.config.set_contest_info(f"{CONTEST_INFO}")
    w.config.set_caution(f"{CAUTION}")
    w.config.set_note(f"{NOTE}")
    w.config.set_sites(*SITES)
    w.config.set_taginfos(*TAGS)
    w.config.set_released(*RELEASED)
    return w.run(
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

