segundos_str = input("Por favor, entre com o numero de segundos que deseja converter:")
total_segs = int(segundos_str)

hora = total_segs // 3600
segs_restantes = total_segs % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

print("hora=", hora, "minutos=", minutos, "segs_restantes_final=", segs_restantes_final)
