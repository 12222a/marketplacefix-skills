# Field rules and limits

Character limits vary by marketplace and category, and they change. The ranges below are common ones. **Confirm against Seller Central or `scripts/check_listing.py` before you finalise.**

## Title

- Commonly up to 200 characters, lower in some categories; mobile usually shows only the first 70-80.
- Order: brand + what the product is and its main keyword + the key difference + specification or quantity + where it is used.
- The first 70 characters must stand on their own. That is all most buyers see.
- One word of tension is allowed. One. More than that reads as clickbait.
- No promotional language, no full caps, no keyword repeated more than twice.

## Bullet points

- Five bullets, commonly up to 200-250 characters each, 500 in some marketplaces.
- One claim per bullet, written as benefit plus the fact that supports it, never as a specification list.
- The first sentence, roughly the first 80 characters, has to land the benefit; mobile truncates.
- No overlap between bullets, ordered by how buyers decide: the pain they most want solved, the key difference, the experience of using it, materials and durability, size and fit.

## Description and A+

- The description is where you persuade, not where you document. Tell a story, give scenes, give comparisons.
- Allocate A+ modules with attention, interest, desire, trust, action: the first screen catches attention, the middle builds interest and desire, the later screens carry proof, the last screen gives the reason to act now.
- A+ copy must not repeat the bullets word for word.

## Backend search terms

- Commonly around 250 bytes, no punctuation, and no words already used in the title or bullets.
- Use spelling variants, synonyms, material names, occasion words, and model compatibility.
- No competitor brands, and no words like best or cheap.

## Policy red lines

These trigger takedowns or review in most categories:

- Promotion and price: free shipping, on sale, discount, coupon, limited time, buy one get one
- Absolutes and rankings: best seller, number one, top rated, 100%, guaranteed
- Medical and safety claims: cure, treat, FDA approved, non-toxic, 100% safe
- Environmental claims: eco-friendly, biodegradable - most categories require certification to support them
- Competitor brand names, disparaging comparisons
- Contact details, URLs, social handles, QR codes
- Emoji, special symbols, words in full capitals (brand names excepted)

## Self-check

```bash
python scripts/check_listing.py listing.md
```

The script reads one `field: value` pair per line for title, bullets, description, A+, and search terms, then reports the character count of each field and where it hit a red line. Clear every red line before you deliver.
