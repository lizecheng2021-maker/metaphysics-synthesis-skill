# Skill de Síntesis Metafísica

Un skill para Codex y AI Agent enfocado en BaZi, Meihua Yishu, Liuyao, análisis direccional de Feng Shui y lectura de Tarot.

Este repositorio no es solo un prompt de adivinación. Es un método reutilizable para que un asistente de IA elija el sistema correcto, dé un veredicto, muestre evidencia, estime el tiempo, proponga acciones y defina señales de verificación.

> Uso cultural, reflexivo y estratégico únicamente. Este skill no sustituye consejos médicos, legales, financieros, psicológicos, de emergencia o de seguridad.

## Búsquedas objetivo

- skill de adivinación con IA
- skill Codex para BaZi
- asistente IA de astrología china
- lectura BaZi cuatro pilares
- calculadora Meihua Yishu
- I Ching presagio Meihua
- flujo Liuyao para IA
- seis líneas Najia
- análisis Feng Shui de direcciones
- Feng Shui oficina puesto de trabajo
- prompt de Tarot con IA
- tirada de tarot carta invertida
- skill de metafísica china para agentes IA

## Sistemas compatibles

| Sistema | Mejor para | Archivo |
| --- | --- | --- |
| BaZi / Zi Ping | Estructura de vida, ciclos de diez años, carrera, riqueza, matrimonio, salud | `references/bazi.md` |
| Meihua Yishu | Presagios, horarios, eventos repentinos, movimiento de corto plazo | `references/meihua.md` |
| Liuyao / Najia | Contratos, puesto, jefe, salario, tracción de producto, resultado concreto | `references/liuyao.md` |
| Feng Shui / Dirección | Puesto de trabajo, orientación, puertas, ventanas, flujo, visibilidad | `references/fengshui.md` |
| Tarot | Dinámica relacional, psicología, decisiones, punto de giro simbólico | `references/tarot.md` |

## Funciones principales

- Separa veredicto, evidencia, tiempo, acción y puntos de verificación.
- Distingue conclusiones de alta confianza de inferencias de baja confianza.
- Analiza cada sistema por separado antes de sintetizar.
- Marca cada método como `runnable`, `partial` o `blocked`.
- Separa los datos calculables de BaZi de la interpretación.
- Fija las entradas de Meihua Yishu: hora, números y presagio externo.
- Mantiene las seis líneas Liuyao en orden de abajo hacia arriba.
- Lee Feng Shui por forma y entorno antes de fórmulas direccionales.
- Proporciona tiradas de Tarot reproducibles con spread, seed y cartas derechas/invertidas.
- Incluye un script para calcular la estructura de Meihua Yishu.
- Incluye un script de tirada Tarot y un control de privacidad antes de publicar.
- Define límites de seguridad para temas sensibles.

## Instalación

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill.git ~/.codex/skills/metaphysics-synthesis
```

Reinicia Codex o recarga los skills si tu entorno lo requiere.

## Ejemplos en español

### Ejemplo BaZi

```text
Analiza esta carta BaZi para carrera y riqueza entre 2026 y 2036. Separa estructura natal, suerte decenal, activadores anuales, conclusiones de alta confianza e inferencias de baja confianza.
```

### Ejemplo Meihua Yishu

```text
Usa Meihua Yishu para leer si este lanzamiento de producto puede crear un avance visible en mi carrera. La pregunta surgió el 2026-06-12 a las 10:36, y el presagio externo fue un gerente hablando de planificación al noroeste.
```

### Ejemplo Liuyao

```text
Usa Liuyao para juzgar si este proyecto puede convertirse en la evidencia principal para una promoción. Las seis líneas de abajo hacia arriba son 5 / 4 / 25 / 12 / 22 / 17.
```

### Ejemplo Feng Shui

```text
Analiza mi puesto de trabajo con lógica de direcciones Feng Shui. Estoy mirando al sureste, mi gerente directo está al noroeste, el líder principal está al sur y otro gerente está al este.
```

### Ejemplo Tarot

```text
Usa una tirada de siete cartas de Tarot para leer solo la dinámica de la relación. Da la carta central, el obstáculo, el punto de giro, la acción probable y las señales de verificación.
```
