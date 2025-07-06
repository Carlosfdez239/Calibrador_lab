PROYECTO: Calibrador_lab — Sistema técnico de control de noria

FUNCIONES PRINCIPALES:
- Interfaz gráfica con definición de paradas angulares
- Simulación visual técnica en tiempo real
- Sensor físico para posición cero
- Registro Excel por cada parada angular (con datos técnicos)
- Selector de modo log: Debug / Producción

DIAGRAMA LOGICO
┌────────────────────┐
│    Inicio sistema  │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│  Cargar GUI Tkinter│
│  (selección modo,  │
│  paradas, sentidos)│
└─────────┬──────────┘
          │
          ▼
┌─────────────────────────┐
│ Detectar posición cero  │
│ (sensor físico)         │
└─────────┬───────────────┘
          │
          ▼
┌─────────────────────────┐
│ Leer lista de paradas   │
│ desde `paradas.json`    │
└─────────┬───────────────┘
          │
          ▼
┌─────────────────────────┐
│ Bucle por cada parada   │
│ ┌─────────────────────┐ │
│ │ Calcular desplaz.   │ │
│ │ Leer configurac. UART│ │
│ │ Mover motor (STEP)  │ │
│ │ Registrar datos     │ │
│ └─────────────────────┘ │
└─────────┬───────────────┘
          │
          ▼
┌───────────────────────────┐
│  Guardar en Excel .xlsx   │
│  (ángulo, tiempo, corriente│
│   temperatura, timestamp) │
└─────────┬─────────────────┘
          │
          ▼
┌──────────────────────┐
│     Fin del proceso  │
└──────────────────────┘