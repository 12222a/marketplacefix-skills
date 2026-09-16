# amazon-listing-writing

A skill for writing Amazon listing copy: title, bullet points, description, A+ content, and backend search terms. It turns product facts into claims a buyer understands and acts on, and it refuses to fill gaps with adjectives.

## What is in the folder

```
SKILL.md                          the skill itself
references/fab-translation.md     feature -> advantage -> benefit, with worked examples
references/amazon-fields.md       per-field rules, limits, and policy red lines
references/message-metrics.md     attention, clarity, and effect
scripts/check_listing.py          length and policy-word checker
```

## Install

**Claude Code**: copy the folder to `~/.claude/skills/amazon-listing-writing/`, or into `.claude/skills/` inside a project. Invoke it with `/amazon-listing-writing`.

**Codex**: copy the folder to `~/.codex/skills/amazon-listing-writing/`. It is picked up automatically.

**ChatGPT or Claude in the browser**: open a Project, paste the contents of `SKILL.md` into the project instructions, and attach the reference files to the project so the model can read them on demand.

**Anywhere else**: paste `SKILL.md` as a system prompt. The references are optional reading for the model; add them if you have room.

## Use

Give it the product facts, the marketplace, the category, and the keywords you can use. It will produce a feature-to-benefit table, the list of facts you still need to supply, and finished copy for each field.

Check the result before publishing:

```bash
python scripts/check_listing.py listing.md
```

The file needs one `field: value` pair per line:

```
Title: Nordic Ware Cast Iron Skillet, 10 Inch, Pre-Seasoned
Bullet 1: Even heat across the pan, so the middle of the pancake is not pale
Search Terms: cast iron pan skillet fry pan
```

## Limits

- It does not do keyword research, product research, or advertising. Feed those in as inputs.
- It will refuse to invent specifications, certifications, or test data, and it will say which facts are missing instead.
- Character limits vary by marketplace and category. The numbers in `references/amazon-fields.md` are common ranges, not guarantees: confirm in Seller Central or with the script.

## Version

1.0, last verified 2026-09-17. The method was distilled from a wearesellers.com community article; the field rules, workflow order, and checker script are ours.
