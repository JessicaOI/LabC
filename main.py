from funciones import reescribir_archivo, get_values_list
from Postfix_AFN import ejecutar

def main():
    file_name = "EjemploBasico.txt"

    with open(file_name, "r") as file:
        input_text = file.read()

    rewritten_text = reescribir_archivo(input_text)
    print("Yalex nuevo\n"+rewritten_text)
    
    resultado = get_values_list(rewritten_text)
    print("Resultados:")
    print(resultado)

    for regex in resultado:
        ejecutar(regex)

if __name__ == "__main__":
    main()
