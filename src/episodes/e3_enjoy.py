# -*- coding: utf-8 -*-
"""Episode: enjoy
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
def sc_handdistance(w: World):
    chi, ei = W(w.chisa), W(w.eisuke)
    outside = W(w.outside)
    return w.scene("手の届く距離で", "まだ二人は手の届く距離を歩いていた",
            w.comment("少し季節が動く"),
            outside.look("夏の暑さを感じる",
                "河川敷を二人で帰る"),
            chi.come("歩いている"),
            ei.come("歩いている"),
            chi.do("二人の距離は開いていく",
                "それを$Sは追いかけて縮める",
                "二人で帰る時はいつもこんな感じになってしまっていた"),
            chi.talk("県大会、残念だったね"),
            ei.talk("まあ、がんばるさ",
                "それより試験が頭痛いわ"),
            ei.do("笑う","&"),
            chi.think("それがずっと欲しかったものだった",
                "彼の笑顔", "日陰にいるみたいな自分を照らしてくれそうな、優しい、歯並びが少し悪い、でもとても好きな笑顔"),
            chi.do("隣に出て、歩く"),
            ei.talk("あ、悪い", "また知らない間に早くなってたわ"),
            chi.talk("ううん、いいよ", "$meが合わせるし"),
            ei.talk("いや、$meが合わせるよ", "バスケやってるとさ、チームが大事だって思うんだ"),
            chi.talk("またバスケの話？"),
            chi.think("彼の話の大半はバスケだった", "漫画も、見るテレビも、ゲームも、何もかもバスケ",
                "友だちも男ばかりで、遊びに行くよりも練習していたいって"),
            ei.talk("いや、バスケの話ってか、バスケの話じゃないけど、",
                "一人上手い奴がいてもさ、バスケって一人じゃできないから、結局周りの奴と協力しなくちゃいけなくて",
                "二人とか三人とか、チームっていうのが大事でさ、",
                "結局それって自分のことだけじゃなくて相手がどう動くか、どうパスするのか、どこにポジショニングするのかとか、",
                "注意深く見て理解してなきゃいけなくてさ、",
                "$meと$ln_chisaもそんな関係なんじゃないかなって"),
            chi.talk("チームってこと？"),
            chi.think("カップルじゃなくて"),
            ei.talk("何が言いたいか上手く言えないけど、なるべく一緒に帰れるようにする"),
            chi.talk("ありがとう"),
            chi.think("彼はよく分からないことを言う",
                "でもそういう部分まで含めて、好きな気持ちがある"),
            outside.look("河川敷の公園ではサッカーをしている小学生がいる",
                "楽しそうな笑い声をあげている"),
            chi.do("歩くと会話がなくなる",
                "でもそんなぎこちなさが心地良い",
                "それを恋だと思っていた"),
            chi.do("やがて別れの時が近づく"),
            outside.look("河川敷の向こう側、橋が伸びている",
                "そこで分岐", "$CSは降りて、彼は橋の向こう側"),
            chi.explain("自転車通学の境界線だった"),
            ei.talk("もうすぐだな"),
            chi.talk("うん"),
            chi.do("いつも繰り返される、確認のようなそれ"),
            _.think("ちょっと彼が落ち着かないのは別れを惜しんでくれているからだろうか"),
            ei.talk("な、ちょっと聞きたいんだが"),
            chi.do("彼は立ち止まりながら振り返り$meを見て"),
            ei.talk("好きな食べ物ってあるか"),
            chi.talk("好きは特別ないけど嫌いなら結構ある"),
            ei.talk("$meはグリンピースが駄目でさ、カレーとかピラフとかオムライスとかさ"),
            chi.talk("うんうん。わかる"),
            chi.think("同じポイントを見つけて喜ぶ姿が、愛おしい",
                    "もっと一緒にいたいと思う"),
            ei.do("でも彼は先に歩き出す"),
            chi.do("慌ててついていく"),
            chi.think("もっと一緒にいたい、と言いたい"),
            ei.talk("それじゃあな"),
            ei.do("彼は小さく頭を下げ、自転車に跨る"),
            chi.talk("うん", "また明日……ばいばい"),
            ei.talk("おう"),
            chi.do("彼の自転車が橋を渡り切るまでじっと見つめてしまう",
                    "彼は振り返らない"),
            chi.think("この時には既に心の歩幅が違っていたのだろう"),
            # NOTE:
            #   手を繋げないまま、歩くが、互いに目を合わせたり、彼の話に適当に頷くのすら楽しい日々
            #   好きな食べ物の話なんかでも楽しい
            #   けれど尽く「合わない」
            camera=w.chisa,
            stage=w.on_riverbed,
            day=w.in_enjoy1, time=w.at_afternoon,
            )

## episode
def ep_enjoytime(w: World):
    return w.episode("楽しかった頃", "まだあの頃は一緒に帰る道が楽しいばかりだった",
            sc_handdistance(w),
            )
