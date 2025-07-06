import time
from random import uniform  # Simula valores reales

def mover_a_angulo(logger, angulo_obj, sentido, microstepping):
    inicio = time.time()
    logger.info(f"Moviendo a {angulo_obj:.2f}° ({sentido})")

    time.sleep(uniform(0.8, 1.5))  # Simula viaje
    angulo_real = angulo_obj + uniform(-0.04, 0.04)

    tiempo_ms = int((time.time() - inicio) * 1000)
    acc_ini = round(uniform(30, 40), 2)
    acc_viaje = round(uniform(20, 30), 2)
    acc_fin = round(uniform(10, 20), 2)
    temperatura = round(uniform(40, 50), 1)
    corriente = round(uniform(750, 850), 1)

    logger.info(f"Llegó a {angulo_real:.2f}° en {tiempo_ms} ms")

    return {
        "programado": angulo_obj,
        "real": angulo_real,
        "tiempo_ms": tiempo_ms,
        "acc_ini": acc_ini,
        "acc_viaje": acc_viaje,
        "acc_fin": acc_fin,
        "temperatura": temperatura,
        "corriente": corriente
    }