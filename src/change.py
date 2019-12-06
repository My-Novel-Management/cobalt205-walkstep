# -*- coding: utf-8 -*-
"""Episode: change ours
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer

W = Writer


## scenes
def sc_rainy(w: World):
    chi, ei = W(w.chisa), W(w.eisuke)
    return w.scene("嵐の日に", "雨の日には相合い傘をするような関係だったのに",
            chi.isa("雨降り"),
            chi.look("彼の背中を"),
            chi.look("小さな傘で背中が濡れているのを"),
            chi.remember("雨の日に傘を貸してあげた時には右肩が濡れていたことを"),
            chi.talk("ねえ"),
            ei.talk("何？"),
            chi.talk("背中、濡れてるよ"),
            chi.do("拭いてあげる"),
            ei.talk("おう。サンキューな"),
            chi.talk("地区大会どう？　いいとこまでいけそう？"),
            ei.talk("今度はスタメンで出られるかもって言われた。もっとがんばんなきゃな"),
            ei.talk("$n_chisaは進学どうすんだ？"),
            chi.talk("うん"),
            chi.be(doing="雨が酷くなってくる"),
            )

def sc_apart(w: World):
    chi, ei = W(w.chisa), W(w.eisuke)
    return w.scene("離れる距離", "立ち止まらなくなった彼",
            chi.talk("ねえ"),
            chi.look("彼は振り返らないのを"),
            chi.talk("ねえってば"),
            ei.talk("ん？"),
            chi.talk("最近スマホばかり見てる"),
            ei.talk("そうか？"),
            chi.talk("やっぱ変。なんかあった？"),
            ei.talk("なんもないよ"),
            chi.talk("キスの一つもしてないから？"),
            ei.talk("ちげーよ。そういうんじゃない"),
            chi.talk("だったら何？"),
            ei.look("じっと"),
            chi.talk("もうちょっと、話してほしい"),
            ei.talk("何話せばいいんだよ"),
            chi.talk("なんでもいい。ゲームでもバスケでも何でも"),
            ei.talk("お前としても楽しくないだろ？"),
            chi.talk("会話がしたいんじゃない"),
            ei.talk("わかんねーな"),
            chi.think("彼の歩く速度が早いと"),
            )

## episode
def ep_change_our(w: World):
    return w.episode("変わる二人", "少しずつ変わっていく二人",
            sc_rainy(w),
            sc_apart(w),
            )
