print("Algoritmo de planificación RR")
tiempo_proceso = input("Ingrese los tiempos de procesamiento separados por un espacio: ").split()
tiempo_proceso = [int(x) for x in tiempo_proceso]
longitud = len(tiempo_proceso)
quantum = int(input("Ingrese el tamaño del quantum: "))
tiempo_espera, tiempo_respuesta = [0], [tiempo_proceso[0]]
tiempo_espera_promedio, tiempo_respuesta_promedio, numero_quantums = 0, 0, 0
procesos_atentidos = 0;
while(procesos_atentidos == 0):
  procesos_atentidos = 1
  for i in range(len(tiempo_proceso)):
    if(tiempo_proceso[i]>0):
      tiempo_proceso[i] -=quantum
      if(tiempo_proceso[i]<0): tiempo_proceso[i] = 0
      numero_quantums+=1
      print("\nQuantum número {:d}, proceso número {:d}".format(numero_quantums, i))
      print("Cantidad de tiempo del proceso luego de utilizar su quantum: {:d}".format(tiempo_proceso[i]))
      if(tiempo_proceso[i]>0):
        procesos_atentidos = 0
      else:
        tiempo_respuesta_promedio += (numero_quantums * quantum)

print("\nTotal de Quantums utilizados: {:d}\nTiempo de respuesta promedio: {:.2f}".format( numero_quantums, tiempo_respuesta_promedio/longitud))