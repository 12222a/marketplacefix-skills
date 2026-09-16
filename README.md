# MarketplaceFix skills

Installable skills for Amazon sellers who work with an AI assistant. Each one is a procedure with an order of work, rules for what to do when information is missing, and a way to check the result.

These are the same files published on [marketplacefix.com/skills](https://marketplacefix.com/skills/), where each skill has a page explaining what it does and how it was built.

## Skills

| Skill | What it does |
| --- | --- |
| [amazon-listing-writing](amazon-listing-writing/) | Writes Amazon listing copy from product facts: title, bullets, description, A+ modules, backend search terms, with a length and policy-word checker. |

## Install

Clone the repo and copy the skill folder into the skills directory of whichever assistant you use:

```bash
git clone https://github.com/12222a/marketplacefix-skills.git

# Claude Code
cp -r marketplacefix-skills/amazon-listing-writing ~/.claude/skills/

# Codex
cp -r marketplacefix-skills/amazon-listing-writing ~/.codex/skills/
```

On Windows, copy the folder into `%USERPROFILE%\.claude\skills\` or `%USERPROFILE%\.codex\skills\` instead.

For ChatGPT or Claude in a browser, create a Project, paste the contents of `SKILL.md` into its instructions, and attach the reference files.

## What is in a skill

```
SKILL.md                 the procedure the assistant follows
references/*.md          detail the assistant reads on demand
scripts/*.py             checks that can be run rather than guessed at
README.md                install notes and limits for that skill
```

## How these are built

Each skill starts from work that has actually been done: community methods, official platform documentation, and our own testing. Where a method comes from somewhere else, the skill credits it and says what we added. Every skill carries a version and a last-verified date, because model behaviour and platform rules both move.

A skill here states what it refuses to do. For listing copy, that means it will not invent specifications, certifications or test data, and it will not use competitor names or absolutes. A skill that makes things up is worse than no skill, because you cannot tell which sentence was invented.

## Issues and corrections

If a skill gives you a wrong or outdated answer, open an issue with the input you gave it and what came back. Corrections go into the existing skill as a new version rather than into the comments.
