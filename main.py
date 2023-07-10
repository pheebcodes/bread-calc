#!/usr/bin/env python3

import argparse
import decimal

import recipes
import shapes


def args():
	parser = argparse.ArgumentParser(
	    description='Calculate batch bread recipe')
	parser.add_argument('shape', type=str, help='Shape of bread')
	parser.add_argument('recipe', type=str, help='Recipe of bread')
	parser.add_argument('count',
	                    type=int,
	                    help='Total count',
	                    nargs='?',
	                    default=1)
	args = parser.parse_args()
	return (args.shape, args.recipe, args.count)


def getRecipe(recipeName):
	recipe = {
	    k: decimal.Decimal(v)
	    for k, v in getattr(recipes, recipeName).items()
	}
	total = sum(recipe.values())
	return {k: v / total for k, v in recipe.items()}


def getShapeWeight(shapeName):
	return decimal.Decimal(getattr(shapes, shapeName))


def calculateBatch(recipe, weight):
	ROUGH_WEIGHT_LOSS = decimal.Decimal("0.03")
	adjustedWeight = weight * (
	    ROUGH_WEIGHT_LOSS + 1
	)  # accounting for a bit of weight loss in the dough
	return {k: v * adjustedWeight for k, v in recipe.items()}


def main():
	shapeName, recipeName, count = args()
	recipe = getRecipe(recipeName)
	shapeWeight = getShapeWeight(shapeName)
	batchWeight = shapeWeight * count
	batch = calculateBatch(recipe, batchWeight)
	for ingredient, weight in batch.items():
		print(f"{ingredient}: {int(round(weight))}g")


if __name__ == "__main__":
	main()
