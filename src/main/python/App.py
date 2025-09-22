import sys
from antlr4 import *
from compiladorLexer  import compiladorLexer
from compiladorParser import compiladorParser

# En caso de no poder ejecutar el programa Python por
# problemas de version (error ATNdeserializer), se
# pueden generar los archivos a mano.
#
# Ir a la carpeta donde esta el archivo .g4 y ejecutar 
#     antlr4 -Dlanguage=Python3 -visitor compilador.g4 -o .

def main(argv):
    archivo = "input/programa.txt"
    if len(argv) > 1 :
        archivo = argv[1]
    input = FileStream(archivo)
    lexer = compiladorLexer(input)
    stream = CommonTokenStream(lexer)
    parser = compiladorParser(stream)
    tree = parser.programa()
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)