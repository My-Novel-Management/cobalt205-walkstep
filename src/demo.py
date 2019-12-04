# -*- coding: utf-8 -*-
"""Demo story.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def sc_lastwalk(w: World):
    chisa, eisuke = w.chisa, w.eisuke
    return w.scene("最後の帰り路", "別れを予感しながらも追いつこうとした",
            w.move(chisa, "歩いている"),
            w.look("彼との距離が少しずつ開いていく"),
            w.look("話しかけても彼は振り返らず生返事"),
            w.look("スマホを見つめて"),
            w.look("一センチ、二センチ、そうやって開いていく距離"),
            w.talk(chisa, "ねえ。待ってよ"),
            w.talk(eisuke, "どうした？"),
            w.be(chisa, "声をかけてやっと立ち止まる"),
            w.talk("なんか最近すこし疲れちゃった"),
            w.talk(eisuke, "学校で何かあった？"),
            w.think(chisa, "分からないのだ"),
            w.talk("$meは何もないよ。何も"),
            w.move(eisuke, "歩き出す"),
            w.talk(chisa, "そんな早く帰りたい？"),
            w.talk(eisuke, "何か言いたいことがあるなら言えよ"),
            w.act(chisa, "走って追いつく"),
            w.talk("こうしなきゃ、並んで歩けない"),
            w.look("意味がわからないといった顔で見る"),
            w.think("最初からわかりあえていなかっただけかも知れない"),
            w.talk("付き合ってって言われた時、最初になんて言ったか覚えてる？"),
            w.talk(eisuke, "ああ"),
            w.think(chisa, "どっちかが無理と思ったら後腐れなく別れること"),
            w.talk("最初から別れるときのこと考えてたら駄目だったのかな"),
            w.talk(eisuke, "$n_chisaらしいって思ったけど"),
            w.talk(chisa, "別れる"),
            w.look("彼は慌てない。いつもそうだ"),
            w.talk(eisuke, "仕方ないよな"),
            w.move("歩いて離れていく"),
            w.look(chisa, "背中が遠ざかる"),
            w.think("涙のないお別れなのに、こんなにもどうしようもなく胸が苦しい"),
            w.think("でも、もう無理に同じ歩幅を保とうとはしない"),
            w.look("彼が消えてしまう"),
            w.hear("小さくなったころ、思い切り叫ぶのが聴こえた"),
            w.think("取り戻せない距離に、彼の声だけが響いていた"),
            )

## episode
def ep_demo(w: World):
    return w.episode("近づけない距離", "二人の歩幅はもう合わせられなくなった",
            )
