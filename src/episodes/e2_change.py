# -*- coding: utf-8 -*-
"""Episode: change ours
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer

## alias
W = Writer
_ = W.getWho()


## scenes
def sc_rainy(w: World):
    chi, ei = W(w.chisa), W(w.eisuke)
    return w.scene("嵐の日に", "雨の日には相合い傘をするような関係だったのに",
            chi.do("雨降り"),
            chi.do("彼の背中を"),
            chi.do("小さな傘で背中が濡れているのを"),
            chi.do("雨の日に傘を貸してあげた時には右肩が濡れていたことを"),
            chi.talk("ねえ"),
            ei.talk("何？"),
            chi.talk("背中、濡れてるよ"),
            chi.do("拭いてあげる"),
            ei.talk("おう。サンキューな"),
            chi.talk("地区大会どう？　いいとこまでいけそう？"),
            ei.talk("今度はスタメンで出られるかもって言われた。もっとがんばんなきゃな"),
            ei.talk("$n_chisaは進学どうすんだ？"),
            chi.talk("うん"),
            chi.be("雨が酷くなってくる"),
            # NOTE:
            #   雨の中、秋になっている
            #   傘を使って互いに近寄れない、心の距離が離れていっていることを見せる
            camera=w.chisa,
            stage=w.on_crossroad,
            day=w.in_disquiet1, time=w.at_evening,
            )

def sc_apart(w: World):
    chi, ei = W(w.chisa), W(w.eisuke)
    return w.scene("離れる距離", "立ち止まらなくなった彼",
            chi.talk("ねえ"),
            chi.do("彼は振り返らないのを"),
            chi.talk("ねえってば"),
            ei.talk("ん？"),
            chi.talk("最近スマホばかり見てる"),
            ei.talk("そうか？"),
            chi.talk("やっぱ変。なんかあった？"),
            ei.talk("なんもないよ"),
            chi.talk("キスの一つもしてないから？"),
            ei.talk("ちげーよ。そういうんじゃない"),
            chi.talk("だったら何？"),
            ei.do("じっと"),
            chi.talk("もうちょっと、話してほしい"),
            ei.talk("何話せばいいんだよ"),
            chi.talk("なんでもいい。ゲームでもバスケでも何でも"),
            ei.talk("お前としても楽しくないだろ？"),
            chi.talk("会話がしたいんじゃない"),
            ei.talk("わかんねーな"),
            chi.think("彼の歩く速度が早いと"),
            # NOTE:
            #   別日。秋風が冷たくて。コート
            #   最初から距離が離れている
            #   少し大きな声で呼び止めて、バスケにたとえられる
            #   不和。話が噛み合わない
            #   なんで、をスルーされる
            stage=w.on_riverbed,
            day=w.in_disquiet2, time=w.at_evening,
            )

## episode
def ep_change_our(w: World):
    return w.episode("変わる二人", "少しずつ変わっていく二人",
            sc_rainy(w),
            sc_apart(w),
            )
