# Root Cause DB Migration - TODO

## Status: In Progress

### Step 1: [✅ COMPLETE] Add get_root_causes() to database.py
### Step 2: [✅ COMPLETE] Update app.py index() route
- New function to query root_cause table.

### Step 2: [PENDING] Update app.py index() route
- Fetch root_causes and pass to template.

### Step 3: [PENDING] Replace hardcoded options in templates/index.html
- Use Jinja {% for %} loop.

### Step 4: [PENDING] Migrate data to root_cause table
- Create INSERT script with ~120 root causes.

### Step 5: [PENDING] Test
- Restart app.py, verify dropdown populates from DB, form submits.

### Step 6: [PENDING] Complete
- Update this TODO, attempt_completion.

Updated after each step.

