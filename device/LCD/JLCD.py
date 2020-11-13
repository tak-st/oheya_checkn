import mojimoji
from LCD import LCD

class JLCD(LCD):
    
    # message method override
    def message(self, string, line = 1):
        
        #文字コードnの文字 ＝ n番目の文字
        codes = u'線線線線線線線線線線線線線線線線　　　　　　　　　　　　　　　　!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}→←　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　。「」、・ヲァィゥェォャュョッーアイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワン゛゜αäβεμσρq√陰ι×￠￡nöpqθ∞ΩüΣπxν千万円÷　塗'
        #変換する文字の辞書(ex.「バ」＝「ハ」「゛」)
        dic ={u'ガ':u'カ゛',u'ギ':u'キ゛',u'グ':u'ク゛',u'ゲ':u'ケ゛',u'ゴ':u'コ゛',u'ザ':u'サ゛',u'ジ':u'シ゛',u'ズ':u'ス゛',u'ゼ':u'セ゛',u'ゾ':u'ソ゛',u'ダ':u'タ゛',u'ヂ':u'チ゛',u'ヅ':u'ツ゛',u'デ':u'テ゛',u'ド':u'ト゛',u'バ':u'ハ゛',u'ビ':u'ヒ゛',u'ブ':u'フ゛',u'ベ':u'ヘ゛',u'ボ':u'ホ゛',u'パ':u'ハ゜',u'ピ':u'ヒ゜',u'プ':u'フ゜',u'ペ':u'ヘ゜',u'ポ':u'ホ゜',u'℃':u'゜C'}
        
        # display message string on LCD line 1 or 2
        if line == 1:
            lcd_line = self.LCD_LINE_1
        elif line == 2:
            lcd_line = self.LCD_LINE_2
        else:
            raise ValueError('line number must be 1 or 2')

        string = string.ljust(self.LCD_WIDTH," ")

        self.lcd_byte(lcd_line, self.LCD_CMD)

                
        # 半角カナのみ全角へ
        string = mojimoji.han_to_zen(string, ascii=False, digit=False)
        # 全角数字のみ半角へ
        string = mojimoji.zen_to_han(string, ascii=False, kana=False)

        # for i in range(self.LCD_WIDTH):
        #     self.lcd_byte(ord(string[i]), self.LCD_CHR)
        #濁音など、文字の変換        
        string2 = ""
        for i in range(self.LCD_WIDTH):
            if ( string[i] in dic.keys() ):
                string2 += dic[string[i]]
            else:
                string2 += string[i]
        
        #文字コードのリストにある文字なら表示、それ以外は表示しない
        for i in range(self.LCD_WIDTH):
            if (codes.find(string2[i]) >= 0):
                self.lcd_byte(codes.find(string2[i])+1,self.LCD_CHR)
            elif (string2[i] == u' '):
                self.lcd_byte(0x10,self.LCD_CHR)
            else:
                self.lcd_byte(0xFF,self.LCD_CHR)