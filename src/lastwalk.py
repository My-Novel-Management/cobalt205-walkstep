# -*- coding: utf-8 -*-
"""Episode: last walk
"""
## import libraries
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer

## alias
W = Writer


## scenes
def sc_lastwalk(w: World):
    chi, ei = W(w.chisa), W(w.eisuke)
    return w.scene("最後の帰り路", "二人の歩幅はどんどん離れていく。そして",
            chi.walk(),
            ei.walk(),
            chi.be("黙って"),
            ei.be("黙って"),
            chi.talk("あの"),
            ei.talk("あのさ"),
            chi.gaze("互いを"),
            chi.talk("なんでこうなっちゃったんだろうね"),
            ei.talk("最初から合わなかっただけなんじゃないかな"),
            ei.talk("最初から、どこか窮屈な関係だったんじゃないか"),
            chi.talk("あれって、窮屈だったの？"),
            chi.think("意外なことを言うと"),
            chi.talk("$meは合わせるのが愛だと思ってた"),
            ei.talk("バスケも同じでさ、相手に合わせてパスを出す"),
            ei.talk("でもそれじゃあ相手のレベルに合わせるだけで決してチームは上手くならない"),
            chi.talk("バスケ？"),
            ei.talk("これだけ離れてるだろ？"),
            chi.look("二人の間の距離を"),
            ei.talk("ゆっくりしたパスは敵に取られるからって強くパスすると相手が下手なら受け取れない。そういうことなんだよ"),
            chi.talk("わかんないよ、バスケ"),
            ei.talk("悪かった"),
            chi.talk("やっぱり、終わりなんだね"),
            chi.talk("覚えてる？　最初に約束したこと"),
            ei.nod(),
            # NOTE:
            #   最後の帰り道は無言のまま、何故か歩幅が揃っている
            #   どちらからも「別れよう」が出てくる
            #   それを聞いて、ああ、やっぱり、と互いに思う
            #   珍しく英輔は饒舌に語る
            #   自分の知らない彼。でも最初の頃はこんなだった（あとで読者が気づく）
            #   最初の約束、にフォーカスさせる
            camera=w.chisa,
            stage=w.stage.riverbed,
            day=w.day.depart, time=w.time.evening,
            )


## episode
def ep_lastwalk(w: World):
    return w.episode("最後の帰り路", "いつの間にか歩幅は埋められなくなっていた",
            sc_lastwalk(w),
            )
