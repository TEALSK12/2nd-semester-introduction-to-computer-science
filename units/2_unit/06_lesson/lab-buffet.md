# Buffet Table

You're ordering food for three people at a buffet, and you can each get only a few things.

## Requirements

* There must be at least 10 food items at the buffet.
* Each item is a single serving, so selecting an item must remove it from the buffet.
* A full order contains three food items.
* Ask for a name for each order.
* Loop over the buffet, selecting one item for each order, until all orders are full.

## Example output (incomplete)

```
Welcome to the buffet!
Who is receiving the first plate? Todd
Who is receiving the second plate? Copper
Who is receiving the third plate? Vixen

You may choose three items per plate. Here are your choices: mashed potatoes, fried rice, pot roast, bourbon chicken, General Tso's chicken, spanakopita, Thai yellow curry, fried tofu, bratwurst, salad.
What is Todd's first choice? mashed potatoes
Todd's plate now has: mashed potatoes.

The buffet now has: fried rice, pot roast, bourbon chicken, General Tso's chicken, spanakopita, Thai yellow curry, fried tofu, bratwurst, salad.
What is Copper's first choice? bratwurst
Copper's plate now has: bratwurst.

The buffet now has: fried rice, pot roast, bourbon chicken, General Tso's chicken, spanakopita, Thai yellow curry, fried tofu, salad.
What is Vixen's first choice? bourbon chicken
Vixen's plate now has: bourbon chicken.

The buffet now has: fried rice, pot roast, General Tso's chicken, spanakopita, Thai yellow curry, fried tofu, salad.
What is Todd's second choice? pot roast
Todd's plate now has: mashed potatoes, pot roast.
The buffet now has: fried rice, General Tso's chicken, spanakopita, Thai yellow curry, fried tofu, salad.

What is Copper's second choice? fried tofu
Copper's plate now has: bratwurst, fried tofu.
The buffet now has: fried rice, General Tso's chicken, spanakopita, Thai yellow curry, salad.
```