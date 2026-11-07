import re
from fe10_script_parser import Fe10ScriptParser
sample = r'''$(5)FL|TIAMAT||$(4)R背景上下会話|$(4)B301-戦いとメダリオン|$(7)05$(8)5D"Chaos is born of strife."$(17)$(16)"If the land is covered in war, the dark\ngod will break free of the medallion $(2)w2\nand destroy the world."$(17)$(16)This war could easily spread across\nTellius, and the dark god could be\nawakened.$(17)$(16)We were very fortunate during the\nMad King's War, $(2)w2but it was a close call.$(2)w3\nCan we count on being lucky again?$(17)$(16)Already, we're talking about a war\nbetween Begnion, the largest nation on\nTellius, and three laguz countries.$(17)$(16)That's half the known world, and it's not\nover yet. Have they all forgotten about\nthe possibility of the dark god's rebirth?$(17)\n$(4)FT1000|'''

sample2 = r'''$(5)FL|L_MICAIAH_B|L_SOTHE|L_LAURA||$(4)R背景会話|$(12)03$(8)3D$(4)FT500|$(4)Bデイン-領主館-木陰|$(12)11$(8)1D$(7)03Sothe, do you know the layout of the manor?$(17)\n$(7)11I was here years ago. As I remember, there's a\nlarge armory tucked deep inside the building.$(17)$(16)And if I understand correctly, Begnion soldiers\nguard valuables they've stolen--from rare\nobjects to necessary supplies--in that armory.$(17)\n$(7)03Then$(2)w2 the medicine will be there, too.$(17)\n$(9)$(16)$(2)w4$(12)00$(8)0D$(2)w4$(7)23$(8)3DAre you sure you don't mind?$(17)\n$(7)00$(1)sOf course not!$(2)w2 Danger is part of our\nwork.$(2)w4 Leave everything to us!$(17)\n$(7)11Your abbot will have his medicine.$(17)\n$(7)23$(1)sOh,$(2)w1 thank you so much!$(2)w4 Good luck!$(17)\n$(4)FT1000|'''

sample3 = r'''$(5)FL|L_NUMIDA|L_JELD||$(4)R背景会話|$(12)01$(8)1D$(7)13$(8)3D$(4)Bデイン-城内-部屋|Which leaves us but one recourse$(2)mc...$(2)md$(2)w4\nCrush the rebel faction before it grows larger.$(17)$(16)Exterminate them.$(2)w2 Then the commoners,\nbereft of all hope, will turn their sheep eyes\nback to us and beg to rejoin the flock.$(17)\n$(7)01I see.$(2)w4 Well, I leave the matter in your\nhands.$(2)w4 What funding you need is yours.$(17)\n$(7)13$(1)sI'm glad we agree on this.$(2)w4 Well then,$(2)w2\npardon me, sir, while I tend to our little lambs\non the loose.$(17)'''

sample4 = r'''$(2)BO$(4)RGMAP会話|$(1)g$(4)V0VOICE_GMAP1_05_05_01|辛くも帝国軍の手を逃がれた若者たちによって
組織される義賊【暁の団】は、$(1)G$(2)VW$(1)P$(4)V0VOICE_GMAP1_05_05_02|デインの民を救うために戦っていた。$(1)G$(2)VW$(1)P$(4)V0VOICE_GMAP1_05_06_01|しかし、強大な駐屯軍の力により、国情は悪化の一途を
たどるのみであった。$(1)G$(2)VW$(1)P$(4)V0VOICE_GMAP1_05_07_01|そんな折、
【暁の団】の少女ミカヤは$(1)G$(2)VW$(1)P$(1)*$(1)H$(4)V0VOICE_GMAP1_05_07_02|先のデイン国王アシュナードの遺児がいるという
情報を手に入れる。$(1)G$(2)VW$(1)P$(4)V0VOICE_GMAP1_05_08_01|治めるべき王族を中心に国がまとまれば
再び祖国を解放することができるかもしれない。$(1)G$(2)VW$(1)P$(4)V0VOICE_GMAP1_05_08_02|ミカヤと仲間たちは希望の糸口を求め
死の砂漠へと足を踏み入れた。$(1)G$(2)VW$(1)P'''


def compare_text(sample):
    sample = sample.replace("\n", "\\n")
    print(sample)
    print("---")
    converted = Fe10ScriptParser().convert_raw_message_to_pretty(sample)

    print(converted)

    reconstructed = Fe10ScriptParser().convert_pretty_to_raw_message(converted)
    print("---")
    print("SAMPLE:")
    print(sample)
    print("=")
    print("RECONSTRUCTED:")
    print(reconstructed)
    print(f"Is reconstructed correctly: {sample == reconstructed}")


sample_list = [sample4]

for i in sample_list:
    compare_text(i)
    print("======")

    print(Fe10ScriptParser().convert_pretty_to_raw_message("[invalid function test]"))
    print("|".join(Fe10ScriptParser().function_dict.keys()))
