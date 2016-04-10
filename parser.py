# Parser: Encapsulates access to the input code. Reads an assembly language command,
# parses it, and provides convenient access to the command's components
# (fields and symbols). In addition, removes all white space and comments

import sys, code, symbolTable

class Parser:
    
    def __init__(self):
        path = sys.argv[1]
        ############
        self.code = code.Code()
        self.symbolTable = symbolTable.SymbolTable()
        ###########
        self.varSymIndex = 16
        self.line = 0
        self.run = 0
        self.file = open(path, 'r+')
        self.name = path.split('/')[-1].split('.')[0]
        
    def hasMoreCommands(self):
        file = self.file
        
        while self.run < 2:
            for current in file:
                if not current.startswith('//') and current.strip() != '':

                    if '//' in current:
                        current = current.split('//')[0]
                    
                    self.advance(current.strip())
                    self.line += 1
            file.seek(0)
            self.line += 0
            self.run += 1
            self.hasMoreCommands()
                
    def advance(self, current):
        file = open(self.name + '.hack', 'a+')
        file.write(self.commandType(current))
        file.close()
    
    def commandType(self, current):
        output = ''
        if current.startswith('@'):
            output = self.symbol(current) + '\n'
        elif current.startswith('('):
            self.symbol(current)
        else:
            output = '111' + self.comp(current) + self.dest(current) + self.jump(current) + '\n'
        return output

    def symbol(self, current):
        
        symbol_to_bin = ''
        
        if current[1:].isdigit():
            decimal = int(current[1:])
            symbol_to_bin = '0' + str(bin(decimal)[2:].zfill(15))
        elif current.startswith('@'):
            
            varOrPredefinedSymbol = current[1:]
            
            try:
                # symbolTable.SymbolTable().contains(varOrPredefinedSymbol)
                symbol_to_bin = self.symbolTable.getAddress(varOrPredefinedSymbol)
            except KeyError, e:
                pass
            
            # if not symbolTable.SymbolTable().contains(varOrPredefinedSymbol):
            #     pass
            
            # symbol_to_bin = self.symbolTable.getAddress(varOrPredefinedSymbol)
            
        elif current.startswith('('):
            
            labelSymbol = current[1:-1]
            
            if not self.symbolTable.contains(labelSymbol):
                self.symbolTable.addEntry(labelSymbol, self.line)
                self.line -= 1
            
            symbol_to_bin = self.symbolTable.getAddress(labelSymbol)
            
        return symbol_to_bin
        
    def dest(self, current):
        return self.code.dest(current)
        
    def comp(self, current):
        return self.code.comp(current)

    def jump(self, current):
        return self.code.jump(current)
                    
# Run from terminal
def main():
    foo = Parser()
    foo.hasMoreCommands()
                
if __name__ == "__main__":
    main()