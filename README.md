Interfaz gráfica desarrollada en Python (Tkinter + Matplotlib) para el monitoreo y control de un sistema de tanque con control PID, comunicándose con un ESP32 vía UDP, el cual a su vez se enlaza con una STM32 por UART.
Este repositorio contiene exclusivamente la GUI, pensada como HMI/SCADA ligero para sistemas embebidos.
Características principales:

- Visualización en tiempo real del nivel del tanque
- Visualización de la señal de control (u) con signo
- Indicador de estado del setpoint (±0.5 cm)
- Interfaz multipantalla:
-- Inicio (monitoreo)
-- Control (operación)
-- Diagnóstico (logs)
- Comunicación UDP con ESP32
- Arquitectura no bloqueante (threads)
- Estética industrial y moderna
