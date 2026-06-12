# Router and Input Gate

Use this file when the user asks which divination method to use, combines multiple systems, asks for "strict single reading", or repeats questions.

## Intent Router

| User intent | Best system | Why |
| --- | --- | --- |
| Lifelong pattern, decade luck, broad career/wealth/marriage/health | BaZi | It reads structural tendencies and time bands. |
| Sudden event, omen, timestamp, direction, "what is moving now" | Meihua Yishu | It is strongest for near-term movement and external signs. |
| Promotion, contract, boss, salary, product traction, specific outcome | Liuyao | It handles roles, process, obstacles, and concrete yes/no. |
| Seat, direction, office layout, leader position, door/window/traffic | Feng Shui | It maps space, flow, visibility, and directional symbolism. |
| Relationship dynamics, psychology, choice, emotional texture | Tarot | It reads symbolic and psychological patterns better than hard outcomes. |

## Input Requirements

### BaZi

Need calendar type, birth date, birth time, birthplace/time zone if available, gender if the method uses it, and whether the time is exact.

If the user gives lunar date, do not silently convert unless conversion data is available. State the assumption.

### Meihua Yishu

Need one casting source:

- timestamp and location/time zone,
- two or three numbers,
- object/image/outer omen,
- or a clear event moment.

If using `scripts/meihua_calc.py`, state whether the script used solar `time`, classic lunar `classic`, or number `num` mode.

### Liuyao

Need the exact question and six line inputs from bottom to top. If numbers are provided, state the mapping rule before reading. If the mapping is unknown, read only structure-level signals and say the detailed Najia layer is limited.

### Feng Shui

Need facing direction, sitting direction if known, relative positions, doors/windows, traffic flow, and who sits where.

### Tarot

Need cards and positions if already drawn. If cards are not provided and the user asks the assistant to draw, make clear it is a simulated draw for reflection.

## Repeat Reading Policy

Do not recast the same unchanged question repeatedly. Use this rule:

1. If the question, target, and time window are unchanged, synthesize previous readings instead of casting again.
2. If a new event, new outer omen, new time, or new input appears, it may be a new reading.
3. If the user asks "不要串联记忆", perform only the current reading and do not reconcile with prior readings.
4. If the user asks "串联全部卦", list each reading, preserve its original scope, then synthesize only overlapping signals.

## Precision Rules

- Near-term process timing can be narrow.
- Far-future biography should be broad.
- Exact numeric predictions should be a symbolic range, not measurement-grade certainty.
- Physical traits, wealth level, family structure, and exact relationship labels are low-confidence unless multiple systems and real facts converge.

## Conflict Resolution

When systems conflict:

1. Direct facts win.
2. The system best suited to the question wins.
3. Complete structure wins over isolated signs.
4. Repeated independent signals win over one dramatic omen.
5. State what new event would flip the verdict.
