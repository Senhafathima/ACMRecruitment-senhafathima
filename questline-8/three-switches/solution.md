# Three Switches Puzzle - Optimal Strategy

## Problem Restatement
You are in a room with **three switches**. Each switch controls a single **light**.
The challenge: **Determine exactly which switch controls the bulb, but you may only enter the bulb's room once.**
___

## Strategy
The trick is to use not only whether the bulb is **on or off**, but also whether it is **warm or cold** to the touch.
___

## Step-by-Step Sequence
1. **Switch 1 on for a few minutes**= bulb (if connected) heats up.
2. **Turn Switch 1 off, turn Switch 2 on** immediately.
3. **Leave Switch 3 off** the entire time.
4. Enter the bulb room once:
   - Bulb **on** = Switch 2.
   - Bulb **off but warm** = Switch 1.
   - Bulb **off and cold** = Switch 3.
___

## Logic
- Light = tells you the bulb's current state.
- Heat = tells you the bulb was recently powered.
- Together, these signals guarantee identification with only one visit.
___

## Final Answer
- **Switch 2** = bulb is lit.
- **Switch 1** = bulb is off but warm.
- **Switch 3** = bulb is off and cold.  
