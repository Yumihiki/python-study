# coding: utf-8
"""機種依存文字かどうかを判定する"""


def is_platform_dependent_character(characters):
    """機種依存文字かどうかを判定する

    UTF-8で扱えるが、SHIFT-JISで扱えない文字（UnicodeEncodeErrorが発生する文字）を
    機種依存文字として返却する

    :param characters: 判定対象の文字列
    :return:
    """
    for character in characters:
        try:
            print(character)
            print(not bool(character.encode('shift-jis')))
        except UnicodeEncodeError as e:
            print(e)
            print(True)


if __name__ == "__main__":
    is_platform_dependent_character('①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑯⑰⑱⑲⑳ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩ㍉㌔㌢㍍㌘㌧㌃㌶㍑㍗㌍㌦㌣㌫㍊㌻㎜㎝㎞㎎㎏㏄㎡㍻〝〟№㏍℡㊤㊥㊦㊧㊨㈱㈲㈹㍾㍽㍼∮∟⊿纊褜鍈銈蓜俉炻昱棈鋹曻彅丨仡仼伀伃伹佖侒侊侚侔俍偀倢俿倞偆偰偂傔僴僘兊兤冝冾凬刕劜劦勀勛匀匇匤卲厓厲叝﨎咜咊咩哿喆坙坥垬埈埇﨏塚增墲夋奓奛奝奣妤妺孖寀甯寘寬尞岦岺峵崧嵓﨑嵂嵭嶸嶹巐弡弴彧德忞恝悅悊惞惕愠惲愑愷愰憘戓抦揵摠撝擎敎昀昕昻昉昮昞昤晥晗晙晴晳暙暠暲暿曺朎朗杦枻桒柀栁桄棏﨓楨﨔榘槢樰橫橆橳橾櫢櫤毖氿汜沆汯泚洄涇浯涖涬淏淸淲淼渹湜渧渼溿澈澵濵瀅瀇瀨炅炫焏焄煜煆煇凞燁燾犱犾猤猪獷玽珉珖珣珒琇珵琦琪琩琮瑢璉璟甁畯皂皜皞皛皦益睆劯砡硎硤礰礼神祥禔福禛竑竧靖竫箞精絈絜綷綠緖繒罇羡羽茁荢荿菇菶葈蒴蕓蕙蕫﨟薰蘒﨡蠇裵訒訷詹誧誾諟諸諶譓譿賰賴贒赶﨣軏﨤逸遧郞都鄕鄧釚釗釞釭釮釤釥鈆鈐鈊鈺鉀鈼鉎鉙鉑鈹鉧銧鉷鉸鋧鋗鋙鋐﨧鋕鋠鋓錥錡鋻﨨錞鋿錝錂鍰鍗鎤鏆鏞鏸鐱鑅鑈閒隆﨩隝隯霳霻靃靍靏靑靕顗顥飼餧館馞驎髙髜魵魲鮏鮱鮻鰀鵰鵫鶴鸙黑ⅰⅱⅲⅳⅴⅵⅶⅷⅸⅹ￢￤＇＂')
    # is_platform_dependent_character('a')
    # is_platform_dependent_character('ａ')
    # is_platform_dependent_character('A')
    # is_platform_dependent_character('ｱ')
    # is_platform_dependent_character('ア')
    # is_platform_dependent_character('あ')
    # is_platform_dependent_character('№')
    # is_platform_dependent_character('①')
    # is_platform_dependent_character('?')
    # is_platform_dependent_character('¥')
    # is_platform_dependent_character("'")
    # is_platform_dependent_character("～")
    # is_platform_dependent_character("〜")
