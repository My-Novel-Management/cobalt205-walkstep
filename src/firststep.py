# -*- coding: utf-8 -*-
"""Episode: first step
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer


## scenes
def sc_confession(w: World):
    chi, ei = Writer(w.chisa), Writer(w.eisuke)
    return w.scene("告白の鼓動", "最初の瞬間から、その不安は過っていた",
            chi.be("じっとしている"),
            ei.be(),
            )

def sc_samestep(w: World):
    return w.scene("歩幅を合わせて", "違う歩幅を合わせて互いに寄り添って帰る",
            )

## episode
def ep_firststep(w: World):
    return w.episode("最初の帰り路", "一番最初から、その予感があったことを思い出す",
            sc_confession(w),
            sc_samestep(w),
            )
