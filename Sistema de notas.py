# notas = [
#     4.5, 3.2, 1.5, 4.8, 2.9, 3.7, 5.0, 4.1, 2.3, 3.6,
#     3.9, 4.7, 2.0, 3.1, 4.4, 1.2, 3.5, 4.2, 2.8, 4.9,
#     2.6, 3.8, 4.3, 1.9, 3.0, 4.6, 3.3, 2.5, 4.0, 1.7,
#     3.4, 4.8, 2.2, 3.7, 4.5, 2.1, 3.9, 4.3, 1.0, 3.2,
#     4.1, 2.7, 3.6, 4.9, 1.8, 3.3, 4.4, 2.4, 3.8, 4.6,
#     5.0, 3.1, 2.9, 4.2, 1.4, 3.5, 4.7, 2.3, 3.9, 4.0,
#     1.6, 3.2, 4.5, 2.8, 3.7, 4.3, 2.0, 3.4, 4.8, 1.1,
#     3.6, 4.2, 2.5, 3.8, 4.6, 1.3, 3.0, 4.4, 2.7, 4.1,
#     3.3, 4.9, 2.2, 3.5, 4.7, 1.9, 3.9, 4.0, 2.6, 3.2,
#     4.5, 1.5, 3.7, 4.4, 2.1, 3.8, 4.8, 2.9, 3.4, 4.2
# ]
# aprobados = 0
# reprobados = 0
# for nota in notas:
#     if nota >= 3.0:
#         aprobados = aprobados+1
#         print(f"{nota} Aprobo")
#     else:
#         reprobados = reprobados+1
#         print(f"{nota} tontos")

# print(aprobados)
# print(reprobados)

notassalones = [[[3.8,3.0],2.0,1.0],[2.1,3.2],[1.0,5.0,4.3],[5.0,3.5]]
aprobado = 0
for salon in notassalones:
    for nota in salon:
        if isinstance(nota, list):
            for n in nota:
                if n > 3.0:
                    aprobado = aprobado+1
        else:
            if nota > 3.0:
                aprobado = aprobado+1
    print(f"El salon {notassalones.index(salon)+1} aprobaron {aprobado}")
    aprobado = 0
        

