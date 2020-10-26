print("Algoritmo de planificación FCFS")
tiempo_proceso = input("Ingrese los tiempos de procesamiento separados por un espacio: ").split()
tiempo_proceso = [int(x) for x in tiempo_proceso]
longitud = len(tiempo_proceso)
tiempo_espera, tiempo_respuesta = [0], [tiempo_proceso[0]]
tiempo_espera_promedio, tiempo_respuesta_promedio = 0, tiempo_respuesta[0]

for i in range(1,longitud):
  tiempo_espera.append(tiempo_espera[i-1] + tiempo_proceso[i-1])
  tiempo_respuesta.append(tiempo_espera[i] + tiempo_proceso[i])
  tiempo_espera_promedio+=tiempo_espera[i]
  tiempo_respuesta_promedio+=tiempo_respuesta[i]

print("PR\tTP\tTE\tTR")

[print(i,tiempo_proceso[i],tiempo_espera[i],tiempo_respuesta[i],sep="\t") for i in range(longitud)]

print("Tiempo de espera promedio: {:.2f} \nTiempo de respuesta promedio: {:.2f}".format(tiempo_espera_promedio/longitud, tiempo_respuesta_promedio/longitud))