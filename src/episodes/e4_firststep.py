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
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("告白の鼓動", "最初の瞬間から、その不安は過っていた",
            w.comment("告白される", "場所は学校を少し離れたところがいい"),
            w.comment("季節は春から初夏くらいが良い。最終的に冬に別れるから"),
            w.comment("$eisukeだけは自転車を引っ張っている。通学が異なる"),
            chi.be("信号待ちで立っている"),
            _.think("授業中、何度か目が合ったことを思い出して、少し嬉しい"),
            _.think("そんな些細なことが幸せで、でもこのままでいいのかな、という思いがあった"),
            outside.look("目の前を車が走り抜けていく"),
            chi.hear("駆けてくる足音と、その荒い息",
                "そのリズムに何だか聞いたことあるなって"),
            chi.do("振り返る"),
            ei.come("そこに$Sが立っていた"),
            ei.do("緊張気味に見える", "息が荒くて、バスケの試合の時にも見せたことのないような何だか気まずい顔"),
            ei.talk("あの"),
            chi.talk("は、はい"),
            chi.do("声が裏返る"),
            chi.think("恥ずかしい", "自分のあまり好きじゃない声が恥ずかしい"),
            ei.talk("今、付き合ってる人とか、その、彼氏とか、いる？"),
            chi.talk("え？"),
            ei.talk("だから、そのさ……恋人、いるのかなって"),
            chi.talk("いない、けど"),
            chi.think("心臓がどうにかなってしまいそう",
                "何を言おうとしているのだろう", "言わないで欲しいと言って欲しいが同居している"),
            ei.talk("$meと、付き合って下さい", "お願いします"),
            chi.do("慌てて周囲を見る"),
            outside.look("車は信号の切り替わりで止まり、横断歩道に人が待っている",
                "$CSたちから少し離れて、知らないおばさんが立っていた"),
            chi.do("どうすればいいのだろうかと、逡巡する",
                "考え込み、じっと立ち止まったまま"),
            chi.hear("歩行者信号が青になり、他の人たちは渡り始める",
                "メロディだけが奇妙に響く"),
            chi.talk("なんで、$me？"),
            chi.do("彼の目が見られない"),
            ei.talk("なんでって、その、好きだけじゃ駄目だろうか"),
            chi.think("真面目な声", "からかったりしているんじゃないと分かる"),
            chi.talk("分からない", "どうして$meなのか"),
            ei.talk("じゃあ駄目か？"),
            chi.talk("分からないけど、嬉しい"),
            chi.do("涙が溢れる"),
            ei.talk("あの、泣かせるつもりはなかったんだ", "その、突然こんなこと言って、ごめんかった"),
            chi.talk("ごめん、くない", "ごめんくないよ"),
            ei.talk("え？"),
            chi.talk("嬉しいって言ったの", "嬉しいんだよ？"),
            ei.look("呆気にとられた顔"),
            ei.talk("じゃあ"),
            chi.do("頷くと、彼は顔が明るくなった"),
            ei.talk("そっか。そっかよ"),
            chi.do("彼は背を向けて、ポケットに突っ込んだままの手"),
            outside.look("信号はまた赤に変わっている"),
            ei.talk("えっと、これから、宜しくお願いします"),
            chi.talk("こ、こちらこそ", "お願いします"),
            chi.think("カップルになった、という感動よりも、ただただ顔が熱くて仕方ない"),
            ei.talk("その、えっと、一緒に帰ったりとか"),
            chi.talk("え？"),
            ei.talk("あ、いや、嫌なら別に"),
            chi.talk("いいです", "大丈夫"),
            ei.talk("そっか"),
            chi.talk("そうじゃなくて、帰ります"),
            ei.talk("え？　いいの？　ほんとに？"),
            chi.do("声も出せずに頷く"),
            ei.talk("やった"),
            ei.do("笑顔の彼"),
            w.comment("ある橋まで、で分かれていることを示す"),
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
            w.comment("季節は２学期が始まりで、秋。まだ残暑"),
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
            outside.look("周囲に人がいなくなる"),
            chi.think("抜けていく風を感じる"),
            chi.talk("少し涼しくなってきたね"),
            ei.talk("そうか？"),
            chi.look("着ている制服はまだ夏服", "袖から腕が出ている"),
            _.think("それをじっと見られているみたいで恥ずかしい"),
            chi.talk("短い方がよかった？"),
            ei.talk("なんで？"),
            chi.talk("なんと、なく"),
            chi.do("恥ずかしさを隠すように先に歩き出す",
                "彼はすぐ追いつき、それから歩幅を揃えてくれた"),
            chi.do("顔を見て、互いに照れる"),
            chi.do("同じ歩調で、でも違う歩幅で、歩いていく"),
            chi.talk("あのね……もしどっちかが駄目ってなったら、その時は後腐れなく、別れるって約束してください"),
            ei.talk("分かった"),
            outside.look("夕日が落ちてきている",
                "二人の影が長く伸びて、でも徐々に離れていく"),
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
