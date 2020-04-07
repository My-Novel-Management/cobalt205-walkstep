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
    outside = W(w.outside)
    return w.scene("嵐の日に", "雨の日には相合い傘をするような関係だったのに",
            w.comment("季節は秋", "雨が多い"),
            w.comment("呼び名は進展しているものの、彼の態度が、気持ちが離れつつある。ギクシャク感"),
            outside.look("雨が降っている",
                "誰もが傘を差して歩いていく"),
            chi.be("傘を差しながら待っている"),
            chi.do("携帯電話で彼からの連絡を見る"),
            _.do("先生に呼び出し受けて、遅くなりそう、と"),
            chi.do("待っている"),
            chi.think("秋の大会に向けて懸命に練習する彼を、そっと覗きに行ったことを思い出す",
                "ちらりとも見てくれなかった", "ただバスケットボールにだけ、仲間にだけ、視線を向けていた",
                "その必死さが素敵だと思った", "でも寂しさも同時にあった"),
            chi.do("彼との少ないメッセージのやり取りを振り返る"),
            chi.do("最初の頃は何気ない、おはよう、や、おやすみ、のメッセージが並ぶ",
                "彼はバスケの話で、練習でよく決まったとか、練習試合でどうだったとか",
                "それを$Sが褒めたり、すごいと言ったり",
                "ときどき、彼が好きそうな漫画やアニメの話題を振ってみる",
                "でも「読んどく」「見てみるわ」だけ"),
            chi.think("彼から告白してきたのに、何だか一方通行みたい"),
            chi.do("もう先に帰ろうか、と思った時"),
            ei.come("彼が走ってきた"),
            ei.talk("遅れて悪い", "ちょっと説教くらっちまって"),
            chi.talk("今日は部活、いいの？"),
            ei.talk("休養日だって", "試合後だからそういう方針",
                "練習しすぎても駄目だって今のコーチがさ"),
            ei.do("自転車を押して、雨に濡れている"),
            chi.talk("これ"),
            chi.do("傘を差し出す", "でも背が高くてうまく差せない",
                "彼との身長差を感じて、何だか情けなくなる"),
            chi.talk("ごめん"),
            chi.do("彼の肩に雨が沢山かかる", "びしょ濡れになっている彼"),
            ei.talk("ああ、$meが持つわ"),
            ei.do("傘を持ってくれる"),
            chi.do("でも今度は$Sに雫がかかる", "右側に立ったけれど右肩があぶれた"),
            ei.talk("傘ぱくってくればよかったな", "悪い"),
            chi.talk("盗むのは駄目だよ", "$meがもっと大きな傘持ってくればよかっただけ", "ごめん"),
            _.think("最近ごめん、と口癖のように謝っている", "彼もよく悪いって",
                "なんだかギクシャクの居心地の悪さ"),
            chi.talk("なんか、ごめん"),
            ei.talk("青だぞ、渡ろ"),
            chi.talk("うん"),
            ei.talk("なんで、泣いてんの？", "$me、また何か言ったか？"),
            ei.do("ばつが悪そうな顔で"),
            chi.talk("ううん。傘が、小さかったから"),
            ei.talk("別にいいよ"),
            chi.talk("けど"),
            ei.talk("ああ、もう分かったよ"),
            ei.do("傘を$CSに押し付け、先に歩いて行ってしまう"),
            chi.talk("待って！"),
            chi.do("追いかける"),
            chi.talk("濡れてるよ"),
            ei.talk("別にいいよ。これくらい", "$chisaが泣くよりずっとマシだ"),
            chi.talk("ごめん"),
            ei.do("先に歩き出す"),
            chi.do("ついていく"),
            outside.look("誰もいない河川敷", "雨は酷くなる"),
            chi.do("自分だけ傘", "離れて歩く二人"),
            chi.talk("地区大会どう？　いいとこまでいけそう？"),
            ei.talk("今度はスタメンで出られるかもって言われた。もっとがんばんなきゃな"),
            ei.talk("$chisaは進学どうすんだ？"),
            chi.talk("まだ、よく分からなくて"),
            ei.talk("まあ$meは大学難しそうだからなあ"),
            outside.look("雨が酷くなっていく"),
            ei.talk("わるい。先、帰るわ。流石に"),
            chi.talk("うん"),
            ei.do("自転車に乗りいってしまう"),
            chi.do("一人残されて"),
            # NOTE:
            #   雨の中、秋になっている
            #   傘を使って互いに近寄れない、心の距離が離れていっていることを見せる
            camera=w.chisa,
            stage=w.on_crossroad,
            day=w.in_disquiet1, time=w.at_evening,
            )

def sc_apart(w: World):
    chi, ei = W(w.chisa), W(w.eisuke)
    outside = W(w.outside)
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
