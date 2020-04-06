# -*- coding: utf-8 -*-
"""Episode: first step
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
def sc_confession(w: World):
    chi, ei = W(w.chisa), W(w.eisuke)
    return w.scene("告白の鼓動", "最初の瞬間から、その不安は過っていた",
            chi.be("じっとして"),
            ei.be(),
            ei.do("緊張して"),
            ei.talk("あの、それで先週の返事なんだけど"),
            chi.do(),
            ei.talk("$me、$ln_chisaさんだけだから。こんな風に思うの"),
            chi.do("大きな彼を"),
            chi.do("呼び出しの手紙を見つけたことを"),
            chi.talk("じゃあ、一つだけ約束"),
            ei.do(),
            chi.talk("もしどっちかが駄目ってなったら、その時は後腐れなく、別れるって約束してください"),
            ei.do("考え込んで"),
            ei.do("小さく"),
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
            stage=w.on_crossroad,
            day=w.in_first, time=w.at_afternoon,
            )

def sc_samestep(w: World):
    chi, ei = Writer(w.chisa), Writer(w.eisuke)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("歩幅を合わせて", "違う歩幅を合わせて互いに寄り添って帰る",
            w.comment("告白を終えて、一緒に初めて帰った時の歩幅。合わせようとしていた。どちらからともなく"),
            outside.look("夕暮れの河川敷の情景"),
            _.look("人はあまりいない", "まばらで、友だちと帰る小学生の集団が走り抜けていく"),
            chi.come("歩いている"),
            ei.come("前を歩いている"),
            chi.do("二人は縦に並んで歩いている", "その歩幅の違いが、距離をすぐに離してしまう"),
            _.do("だから必死に追いつこうと早歩きをして"),
            chi.do("$Sは追いついてその背中に当たって、彼を見上げた"),
            ei.do("彼は振り返り「ごめん」と言って、少しゆっくりと歩き出す"),
            chi.talk("あの、さ"),
            ei.talk("ん？"),
            chi.hear("彼の低い声が、響く"),
            chi.do("間が持たなくて、でも何も言葉を見つけられない"),
            chi.talk("何でもない"),
            ei.talk("$ln_chisaさんはさ、やっぱ本とか読んだりするタイプなの？"),
            chi.think("質問の意図が読めなかった"),
            chi.talk("本、読むよ", "$ln_eisuke君はやっぱり漫画？"),
            ei.talk("教科書もろくに読まないけど、漫画だと読みやすい", "兄貴が勉強になるからって日本の歴史とか三国志とかやたら貸してくれる"),
            chi.talk("そっか"),
            chi.do("気を遣って話題を作ろうとしているのだろう",
                "息苦しい", "けどその苦しさが恋なのか何なのか、よく分からなかった",
                "でも気遣いが嬉しい"),
            chi.do("彼のゆったりとした歩調、でも大きな歩幅はすぐに$Sを置いていく",
                "それに必死で追いついて、でもまた離れて、それを繰り返す"),
            outside.look(""),# TODO
            chi.think("そんなささいな笑顔のやり取りが嬉しかったと"),
            chi.do("少しだけ開き始める歩幅を"),
            chi.think("歩幅の違いを"),
            # NOTE:
            #   歩幅を合わせようと、千紗が急ぎ足で追いつこうとするところ
            #   そこで背中を見つめて、思うこと
            stage=w.on_riverbed,
            day=w.in_first, time=w.at_evening,
            )

## episode
def ep_firststep(w: World):
    return w.episode("最初の帰り路", "一番最初から、その予感があったことを思い出す",
            sc_confession(w),
            sc_samestep(w),
            )
