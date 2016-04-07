# Code: Translates Hack assembly language mnemonics into binary codes

class Code:
        
    def dest(self, current):
        dest_mnemonic = current.split('=')[0]
        
        dest_bin = {
            ''    : '000',
            'M'   : '001',
            'D'   : '010',
            'MD'  : '011',
            'A'   : '100',
            'AM'  : '101',
            'AD'  : '110',
            'AMD' : '111'
        }
        
        return dest_bin[dest_mnemonic]
        
    def comp(self, current):
        comp_mnemonic = current.split('=')[1]
        
        comp_bin = {
            '0'  : '0101010',
            'A'  : '0110000',
            'M'  : '1110000',
            'D'  : '0001100',
            'D+A': '0000010',
            'D-M': '1010011'
        }
        
        return comp_bin[comp_mnemonic]

    def jump(self, current):
        return '000'
