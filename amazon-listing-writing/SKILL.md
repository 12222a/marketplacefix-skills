---
name: amazon-listing-writing
description: Use when writing or rewriting Amazon listing copy - title, bullet points, product description, A+ content, backend search terms - to turn product facts into claims a buyer understands and acts on. Does not cover advertising, product research, or keyword research; those are inputs.
metadata:
  short-description: Write Amazon listings by translating features into benefits
---

# Amazon listing writing

## The position this takes

Buyers do not care what your product has. They care what it does for them.

Almost everyone writing a listing suffers from the curse of knowledge. You know the product too well, so you write "fourth-generation nano coating", "PCM phase-change material", "Q-Max 0.38". Buyers do not recognise those words, and they will not research them to understand you. They scroll.

The rule that makes this executable: **every feature must be followed by a benefit. If you cannot find the benefit, delete the feature.**

Twenty specifications will not make someone buy. "Your ears do not get hot when you sleep on your side" will. There is not a single number in that sentence.

## Confirm the inputs first

You need: product facts (materials, measurements, process, test data), the target marketplace and language, the category, the target buyer, and the keywords you are allowed to use.

**When product facts are missing, do not fill the gap with adjectives.** List the questions to put to whoever knows the product, and wait for answers. It is better to publish one fewer claim than to invent a number: buyers check, and platforms take listings down.

Talk to the user in their language; deliver the copy in the target marketplace's language (US marketplace means English).

## Workflow

1. **Read the inputs as a buyer who knows nothing.** Note every place you cannot follow, are unsure about, or think "that sounds interesting but I do not know why".
2. **Chase the facts.** Turn each doubt into a question for the people who know the product, and keep going until the answer is physical: a number, a test count, a measured result, the gap versus the usual approach. Opinions are not answers ("our quality is very good" means keep asking).
3. **Translate feature to benefit.** Fact, then what it does, then what the buyer gets. See [references/fab-translation.md](references/fab-translation.md).
4. **Order the information.** Three measures decide this: attention, effort, effect. See [references/message-metrics.md](references/message-metrics.md).
5. **Fill the fields.** Title, bullets, description, A+, backend search terms each behave differently. See [references/amazon-fields.md](references/amazon-fields.md).
6. **Check your own work.** Save the copy to a file and run `python scripts/check_listing.py <file>`; fix the length and policy problems it reports.

## What to deliver

A Markdown file by default:

- **Feature-to-benefit table** - fact | what it does | what the buyer gets | which field it belongs in. Any row with a fact but no benefit, or an adjective but no fact, is unfinished.
- **Open questions** - the facts the product side has not supplied, written as "benefit we want -> fact we need".
- **Field copy** - ready to paste, with no Markdown decoration and no emoji.
- **Check output** - the script's result.

Do the steps that are needed, not all of them every time. If the user only wants the title rewritten, rewrite the title.

## Hard limits

- Never invent specifications, certifications, test data, sales figures, or reviews.
- No competitor brand names, no disparaging comparisons.
- No promotional language and no absolutes (best, number one, 100%). These trigger takedowns in most categories.
- No medical, curative, or safety guarantees.
- Character limits vary by marketplace and category and change over time. Confirm in Seller Central or with the script before you finalise; do not rely on memory.

## Where the method comes from

The method was distilled from a community article on wearesellers.com, "你真的会写 listing 吗?" (Do you actually know how to write a listing?). This package adds the field-level rules, the working order, and the checker script that the article does not provide.
