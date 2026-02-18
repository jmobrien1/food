"""Recipe scaling with non-linear adjustments for potent ingredients.

RCF (Recipe Conversion Factor) = target_servings / base_servings

For most ingredients: scaled = base * RCF
For potent ingredients: scaled = base * RCF^scaling_exponent
Safety ceiling caps maximum amount regardless of scale.
"""

import math
from dataclasses import dataclass


@dataclass
class ScaledIngredient:
    name: str
    base_grams: float
    scaled_grams: float
    scaling_method: str  # "linear", "non-linear", "capped"


def compute_rcf(target_servings: int, base_servings: int = 4) -> float:
    if base_servings <= 0:
        raise ValueError("base_servings must be positive")
    return target_servings / base_servings


def scale_ingredient(
    name: str,
    base_grams: float,
    rcf: float,
    scaling_exponent: float = 1.0,
    is_potent: bool = False,
    safety_ceiling: float | None = None,
) -> ScaledIngredient:
    if is_potent and scaling_exponent != 1.0:
        scaled = base_grams * math.pow(rcf, scaling_exponent)
        method = "non-linear"
    else:
        scaled = base_grams * rcf
        method = "linear"

    if safety_ceiling is not None and scaled > safety_ceiling:
        scaled = safety_ceiling
        method = "capped"

    return ScaledIngredient(
        name=name,
        base_grams=base_grams,
        scaled_grams=round(scaled, 1),
        scaling_method=method,
    )


def scale_recipe(
    ingredients: list[dict],
    target_servings: int,
    base_servings: int = 4,
) -> list[ScaledIngredient]:
    """Scale a list of ingredient dicts.

    Each dict must have: name, base_grams.
    Optional: scaling_exponent (default 1.0), is_potent (default False), safety_ceiling.
    """
    rcf = compute_rcf(target_servings, base_servings)
    return [
        scale_ingredient(
            name=ing["name"],
            base_grams=ing["base_grams"],
            rcf=rcf,
            scaling_exponent=ing.get("scaling_exponent", 1.0),
            is_potent=ing.get("is_potent", False),
            safety_ceiling=ing.get("safety_ceiling"),
        )
        for ing in ingredients
    ]
