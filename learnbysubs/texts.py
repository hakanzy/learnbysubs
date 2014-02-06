help_text = """
LbS - Learn by Subs

-t|--top     Mandotary    Top file name(with full path)
-s|--sub     Mandotary    Sub file name(with full path)
-n|--new     Mandotary    New/Output file name(with full path)
-j|--join    Optional     Join given subtitles on sub position of screen
                          (Different languages will appear in different colors)
-h|--help    Optional     Show help(this screen)

Example Usage:
$ lbs -t turkish.srt -s english.srt -n newfile.ssa
"""

ssa_header = """[Script Info]
Title: Merged Files -> %s
Original Script: LbS - Learn by Subs (by Hakan OZAY)
ScriptType: v4.00+
Timer: 100,0000

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, TertiaryColour, BackColour, Bold, Italic, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: top, Arial,14,16777215,11861244,11861244,-2147483640,0,0,1,1,2,8,10,10,10,0
Style: banner, Arial,18,101010101,11861244,11861244,-2147483640,-1,0,1,1,2,5,10,10,10,0
Style: sub, Arial,14,11861244,11861244,11861244,-2147483640,0,0,1,1,2,2,10,10,10,0
Style: sub_, Arial,14,111111111,11861244,11861244,-2147483640,0,0,1,1,2,2,10,10,10,0

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:0:0.00,0:0:10.00,banner,,0000,0000,0000,Scroll up;y1;y2;30[;fadeawayheight],{\\b1}[ CREATED WITH LbS ]{\\b0}\Nhttp://github.com/hakanzy/lbs\NHave a good time!

"""

ssa_line = "Dialogue: 1,%s,%s,%s,,0000,0000,0000,,%s"
