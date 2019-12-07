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
            chi.be("じっとして"),
            ei.be(),
            ei.be("緊張して"),
            ei.talk("あの、それで先週の返事なんだけど"),
            chi.nod(),
            ei.talk("$me、$ln_chisaさんだけだから。こんな風に思うの"),
            chi.look("大きな彼を"),
            chi.remember("呼び出しの手紙を見つけたことを"),
            chi.talk("じゃあ、一つだけ約束"),
            ei.nod(),
            chi.talk("もしどっちかが駄目ってなったら、その時は後腐れなく、別れるって約束してください"),
            ei.be("考え込んで"),
            ei.nod("小さく"),
            chi.talk("じゃあ"),
            chi.do("いってしまおうとする"),
            ei.talk("あの！"),
            ei.talk("一緒に、帰ろうか"),
            # NOTE:
            #   告白の返事をした後の、ぎこちなさから開始
            #   一緒に帰ろうか、のところ
            #   まだ春の残り香が街にある
            #   爽やかな空とかの情景
            camera=w.chisa,
            stage=w.stage.crossroad,
            day=w.day.first, time=w.time.afternoon,
            )

def sc_samestep(w: World):
    chi, ei = Writer(w.chisa), Writer(w.eisuke)
    return w.scene("歩幅を合わせて", "違う歩幅を合わせて互いに寄り添って帰る",
            chi.move("歩いて"),
            ei.move("隣を歩いて"),
            chi.look(doing="彼を見上げて"),
            ei.look(doing="彼女を見下ろして"),
            chi.laugh(),
            ei.laugh(),
            chi.remember("そんなささいな笑顔のやり取りが嬉しかったと"),
            chi.look("少しだけ開き始める歩幅を"),
            chi.attention("歩幅の違いを"),
            # NOTE:
            #   歩幅を合わせようと、千紗が急ぎ足で追いつこうとするところ
            #   そこで背中を見つめて、思うこと
            camera=w.chisa,
            stage=w.stage.riverbed,
            day=w.day.first, time=w.time.evening,
            )

## episode
def ep_firststep(w: World):
    return w.episode("最初の帰り路", "一番最初から、その予感があったことを思い出す",
            sc_confession(w),
            sc_samestep(w),
            )
