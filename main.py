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

    # cont = 0
    # for regex in resultado:
    #     cont+=1
    #     nombre = 'afn_'+str(cont)
    #     ejecutar(regex, nombre)

if __name__ == "__main__":
    main()
