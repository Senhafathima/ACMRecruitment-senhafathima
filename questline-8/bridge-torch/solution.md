# Bridge and Torch Problem - Optimal Solution 

## Problem Restatement
Four people need to cross a narrow bridge at night with one torch.
- Crossing times: **1 min, 2 min, 7 min, 10 min**.
- The bridge can hold at most **two people** at once.
- The torch is required for crossing.
- When two cross together, they move at the **slower person's pace**.
- Someone must always bring the torch back if people remain on the original sid>

## Optimal Strategy
The key is to minimize the use of the two slowest people (7 and 10) while ensur>

### Step-by-step Sequence
1. **1 and 2 cross** = 2 minutes (torch moves forward).
   - Left: 7, 10
   - Right: 1, 2

2. **1 returns** = 1 minute.
   - Left: 1, 7, 10
   - Right: 1, 2

 3. **7 and 10 cross** = 10 minutes.
    - Left: 1
    -   Right: 2, 7, 10

4. **2 returns** = 2 minutes.
   - Left: 1, 2
   - Right: 7, 10

5. **1 and 2 cross again** = 2 minutes.
   - Left: (none)
   -Right: 1, 2, 7, 10

### Total Time
- Step 1: 2
- Step 2: 1
- Step 3: 10
- Step 4: 2
- Step 5: 2
**Total = 17 minutes**

## Reasoning
- If 1 always escorts, the total time increases because 1 keeps returning.
- If 2 helps with returns, the strategy balances crossings so that the 7 and 10>
- This results in the optimal **minimum total time of 17 minutes**.
