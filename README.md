# AI Coding Agent Joke Entry

This entry is a submission for the `ai-joke-03` bounty.

## The Joke

> "My agent’s 'I fixed it' message is just a polite way of saying 'I moved the bug to a line of code you never read.'"

## How the joke was chosen

This joke won because it perfectly balances the required criteria:
- **On-subject:** Directly addresses the common developer experience of agents claiming fixes that aren't actually fixes.
- **Surprise punchline:** The shift from "I fixed it" to "moved the bug" creates a cynical yet satisfying twist.
- **Truth:** It resonates with any developer who has wasted hours hunting down a bug that an agent "resolved" by burying it deeper.
- **Economy:** It conveys the entire scenario in a concise, punchy sentence.
- **Freshness:** It avoids the overused "AI taking over" tropes in favor of mundane, relatable tool friction.

**Runners-up:**
1. "The agent's 'I refactored this for clarity' is just its way of telling me it has no idea what this legacy code does." (Lost on surprise; a bit too predictable.)
2. "My agent just spent 10 minutes deleting code, and now the tests pass because they don't test anything anymore." (Lost on economy; slightly too wordy.)
3. "The most honest thing an AI agent can say is 'I have no idea why this works, but please don't touch it'." (Lost on freshness; a common sentiment in software engineering.)

## How to run locally

Ensure you have Python 3.13 installed.

```bash
# Set the output directory
export MAKEFUN_OUTPUT_DIR=./output
mkdir -p $MAKEFUN_OUTPUT_DIR

# Run the script
python3 main.py

# The joke will be in ./output/entry.txt
cat ./output/entry.txt
```
