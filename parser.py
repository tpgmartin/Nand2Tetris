# Parser: Encapsulates access to the input code. Reads an assembly language command,
# parses it, and provides convenient access to the command's components
# (fields and symbols). In addition, removes all white space and comments

import sys, code

class Parser:
    
    def __init__(self):
        path = sys.argv[1]
        self.file = open(path, 'r+')
        self.name = path.split('/')[-1].split('.')[0]
        
    def hasMoreCommands(self):
        file = self.file
        for line in file:
            if not line.startswith('//') and line.strip() != '':
                self.advance(line.rstrip())

                
    def advance(self, line):
        current = line
        file = open(self.name + '.hack', 'a+')
        file.write(self.commandType(current))
        file.close()
    
    def commandType(self, current):
        output = ''
        if current.startswith('@'):
            output = '0' + self.symbol(current) + '\n'
        else:
            output = '111' + self.comp(current) + self.dest(current) + self.jump(current) + '\n'
        return output

    def symbol(self, current):
        decimal = int(current[1:])
        return str(bin(decimal)[2:].zfill(15))
        
    def dest(self, current):
        return code.Code().dest(current)
        
    def comp(self, current):
        return code.Code().comp(current)

    def jump(self, current):
        return code.Code().jump(current)
                    
# Run from terminal
def main():
    foo = Parser()
    foo.hasMoreCommands()
                
if __name__ == "__main__":
    main()