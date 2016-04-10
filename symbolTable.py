# SymbolTable: Keeps a correspondence between symbolic labels and numeric
# addresses.

class SymbolTable:
        
    def __init__(self):
        # initialize with predefined symbols
        self.symbol_table = {
            'SP'     : '0000000000000000',
            'LCL'    : '0000000000000001',
            'ARG'    : '0000000000000010',
            'THIS'   : '0000000000000011',
            'THAT'   : '0000000000000100',
            'R0'     : '0000000000000000',
            'R1'     : '0000000000000001',
            'R2'     : '0000000000000010',
            'R3'     : '0000000000000011',
            'R4'     : '0000000000000100',
            'R5'     : '0000000000000101',
            'R6'     : '0000000000000110',
            'R7'     : '0000000000000111',
            'R8'     : '0000000000001000',
            'R9'     : '0000000000001001',
            'R10'    : '0000000000001010',
            'R11'    : '0000000000001011',
            'R12'    : '0000000000001100',
            'R13'    : '0000000000001101',
            'R14'    : '0000000000001110',
            'R15'    : '0000000000001111',
            'SCREEN' : '1000000000000000',
            'KBD'    : '1100000000000000'
        }
        
    def addEntry(self, symbol, address):
        
        address_to_bin = str(bin(address)[2:].zfill(16))
        self.symbol_table[symbol] = address_to_bin
        
    def contains(self, symbol):
        return symbol in self.symbol_table
        
    def getAddress(self, symbol):
        return self.symbol_table[symbol]