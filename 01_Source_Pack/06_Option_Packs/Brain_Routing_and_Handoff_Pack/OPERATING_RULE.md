# Operating Rule

## Step 1. Decide If Routing Is Needed

Do not route by habit.

```text
if one domain brain can finish:
  do not use this pack
```

## Step 2. Choose Mode

```text
same_thread_lens:
  current thread reads target brain entry files and works under that lens

separate_thread_handoff:
  current thread writes a launch prompt for another thread

integration_only:
  current thread reads existing outputs and integrates them
```

## Step 3. Declare Active Route

If routing is used, write or update:

```text
ACTIVE_BRAIN_ROUTE.md
```

It must show:

```text
target_brain:
mode:
entry_files:
task:
return_condition:
```

## Step 4. Work Or Handoff

Same-thread mode:

```text
read entry files
apply lens
produce scoped output
return to main integration
```

Separate-thread mode:

```text
write handoff prompt
include entry files to read
include task and expected output
wait for returned output
```

## Step 5. Integrate

The final answer must come from the main integration step.

Do not present a routed brain output as final unless the main thread has accepted it.
