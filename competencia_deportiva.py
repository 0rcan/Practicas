
def categorias():
    if i == 0:
        if grupo_a1 >= grupo_a2:
            print(f"{grupo_a} Participante1 {grupo_a1}")
        elif grupo_a2 >= grupo_a1:
            print(f"{grupo_a} Participante2 {grupo_a2}")
        else:
            print("Error")
        print(f"\n Puntos totales {grupo_a}: {grupo_a1 + grupo_a2}")
            
        if grupo_b1 >= grupo_b2:
            print(f"{grupo_b} Participante1 {grupo_b1}")
        elif grupo_b2 >= grupo_b1:
            print(f"{grupo_b} Participante2 {grupo_b2}")
        else:
            print("Error")
        print(f"\n Puntos totales {grupo_b}: {grupo_b1 + grupo_b2}")
            
        if grupo_c1 >= grupo_c2:
            print(f"{grupo_c} Participante1 {grupo_c1}")
        elif grupo_c2 >= grupo_c1:
            print(f"{grupo_c} Participante2 {grupo_c2}")
        else:
            print("Error")
        print(f"\n Puntos totales {grupo_c}: {grupo_c1 + grupo_c2}")
    
    
if __name__ == '__main__':
    for i in range(0,3):
        grupo_a = input("ingrese nombre del equipo A:")
        grupo_a1 = int(input(f"\n Puntos del primer participante GrupoA: "))
        grupo_a2 = int(input(f"\n Puntos del primer segundo GrupoA: "))
        
        grupo_b = input("ingrese nombre del equipo B:")
        grupo_b1 = int(input(f"\n Puntos del primer participante GrupoB: "))
        grupo_b2 = int(input(f"\n Puntos del primer segundo GrupoB: "))
        
        grupo_c = input("ingrese nombre del equipo C:")
        grupo_c1 = int(input(f"\n Puntos del primer participante GrupoC: "))
        grupo_c2 = int(input(f"\n Puntos del primer segundo GrupoC: "))
        print(f"\n Categoria {i}")
    categorias()