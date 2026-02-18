"""Unit tests for the scaling service."""

import pytest
from app.services.scaling import compute_rcf, scale_ingredient, scale_recipe


def test_compute_rcf_basic():
    assert compute_rcf(4, 4) == 1.0
    assert compute_rcf(8, 4) == 2.0
    assert compute_rcf(2, 4) == 0.5


def test_compute_rcf_invalid():
    with pytest.raises(ValueError):
        compute_rcf(4, 0)


def test_scale_ingredient_linear():
    result = scale_ingredient("chicken", 500, rcf=2.0)
    assert result.scaled_grams == 1000.0
    assert result.scaling_method == "linear"


def test_scale_ingredient_nonlinear():
    result = scale_ingredient(
        "saffron", 0.2, rcf=2.0,
        scaling_exponent=0.5, is_potent=True,
    )
    # 0.2 * 2.0^0.5 = 0.2 * 1.414 ≈ 0.3
    assert result.scaled_grams == pytest.approx(0.3, abs=0.05)
    assert result.scaling_method == "non-linear"


def test_scale_ingredient_capped():
    result = scale_ingredient(
        "saffron", 0.3, rcf=3.0,
        scaling_exponent=0.5, is_potent=True,
        safety_ceiling=0.5,
    )
    assert result.scaled_grams == 0.5
    assert result.scaling_method == "capped"


def test_scale_recipe():
    ingredients = [
        {"name": "chicken", "base_grams": 500},
        {"name": "salt", "base_grams": 5, "is_potent": True, "scaling_exponent": 0.7},
    ]
    results = scale_recipe(ingredients, target_servings=8, base_servings=4)
    assert len(results) == 2
    assert results[0].scaled_grams == 1000.0  # linear
    assert results[1].scaled_grams < 10.0  # non-linear, less than 2x
