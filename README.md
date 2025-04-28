# Mini Cedar Policy Engine

## Summary
You will build a mini authorization engine inspired by AWS Cedar.

Given a set of policies and access requests, your program must decide whether to ALLOW or DENY the action, correctly handle wildcard matching, evaluate logical conditions, and generate a clear explanation for each decision.

---

## Files
- `models.py`: Defines the Policy and Request classes. **(provided)**
- `evaluator.py`: Core logic you must implement.
- `sample_policies.json`: Example policies. **(provided)**
- `sample_requests.json`: Example requests. **(provided)**
- `run_engine.py`: Script to run your evaluator. **(provided)**

---

## Requirements
1. Match principal, action, and resource (support wildcards).
2. Support conditions (`==`, `&&`) inside policies.
3. Apply deny-overrides: if any deny matches, the result must be DENY.
4. Output human-readable explanations for each decision.

---

## Stretch Goals (Optional)
- Support OR (`||`) in conditions.
- Suggest minimal policy changes if a request is denied.
- Build a REPL (read-eval-print loop) for dynamic policy testing.

---

## Run Instructions
```bash
python run_engine.py
```

---

## Deliverables
- Completed `evaluator.py`.
- If stretch goals are completed, a short note describing your extension.

---

## Good luck, and think carefully about your matching and condition evaluation logic!
