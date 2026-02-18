"""Seed database with initial culinary data. Idempotent — skips if data exists."""

import asyncio
import json
import sys
from pathlib import Path

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import async_session, engine
from app.models.base import Base
from app.models.ingredient import Ingredient
from app.models.flavor_profile import FlavorProfile
from app.models.flavor_affinity import FlavorAffinity
from app.models.equipment import Equipment
from app.models.technique import Technique

SEED_DIR = Path(__file__).parent


def load_json(filename: str) -> list[dict]:
    with open(SEED_DIR / filename) as f:
        return json.load(f)


async def seed_ingredients(session: AsyncSession) -> dict[str, int]:
    count = await session.scalar(select(func.count()).select_from(Ingredient))
    if count and count > 0:
        print(f"  Ingredients already seeded ({count} rows), skipping")
        result = await session.execute(select(Ingredient.id, Ingredient.name))
        return {row.name.lower(): row.id for row in result.all()}

    data = load_json("ingredients.json")
    name_to_id: dict[str, int] = {}
    for item in data:
        ingredient = Ingredient(
            name=item["name"],
            category=item["category"],
            subcategory=item.get("subcategory"),
            is_potent=item.get("is_potent", False),
            scaling_exponent=item.get("scaling_exponent", 1.0),
            safety_ceiling=item.get("safety_ceiling"),
        )
        session.add(ingredient)
    await session.flush()

    result = await session.execute(select(Ingredient.id, Ingredient.name))
    name_to_id = {row.name.lower(): row.id for row in result.all()}
    print(f"  Seeded {len(data)} ingredients")
    return name_to_id


async def seed_flavor_profiles(session: AsyncSession, name_to_id: dict[str, int]):
    count = await session.scalar(select(func.count()).select_from(FlavorProfile))
    if count and count > 0:
        print(f"  Flavor profiles already seeded ({count} rows), skipping")
        return

    data = load_json("flavor_profiles.json")
    added = 0
    for item in data:
        ing_id = name_to_id.get(item["ingredient_name"].lower())
        if not ing_id:
            continue
        session.add(FlavorProfile(
            ingredient_id=ing_id,
            descriptor=item["descriptor"],
            intensity=item["intensity"],
        ))
        added += 1
    await session.flush()
    print(f"  Seeded {added} flavor profiles")


async def seed_flavor_affinities(session: AsyncSession, name_to_id: dict[str, int]):
    count = await session.scalar(select(func.count()).select_from(FlavorAffinity))
    if count and count > 0:
        print(f"  Flavor affinities already seeded ({count} rows), skipping")
        return

    data = load_json("flavor_affinities.json")
    added = 0
    for item in data:
        id_a = name_to_id.get(item["ingredient_a"].lower())
        id_b = name_to_id.get(item["ingredient_b"].lower())
        if not id_a or not id_b:
            continue
        # Enforce canonical ordering
        if id_a > id_b:
            id_a, id_b = id_b, id_a
        session.add(FlavorAffinity(
            ingredient_a_id=id_a,
            ingredient_b_id=id_b,
            affinity_score=item["affinity_score"],
            source=item.get("source"),
        ))
        added += 1
    await session.flush()
    print(f"  Seeded {added} flavor affinities")


async def seed_equipment(session: AsyncSession):
    count = await session.scalar(select(func.count()).select_from(Equipment))
    if count and count > 0:
        print(f"  Equipment already seeded ({count} rows), skipping")
        return

    data = load_json("equipment.json")
    for item in data:
        session.add(Equipment(
            name=item["name"],
            category=item["category"],
            is_professional=item.get("is_professional", False),
            capabilities=item.get("capabilities", []),
            home_alt=item.get("home_alt"),
        ))
    await session.flush()
    print(f"  Seeded {len(data)} equipment items")


async def seed_techniques(session: AsyncSession):
    count = await session.scalar(select(func.count()).select_from(Technique))
    if count and count > 0:
        print(f"  Techniques already seeded ({count} rows), skipping")
        return

    data = load_json("techniques.json")
    # First pass: insert without fallback references
    name_to_technique: dict[str, Technique] = {}
    for item in data:
        # Handle time_minutes as int or {min, max} object
        time_val = item["time_minutes"]
        if isinstance(time_val, dict):
            time_val = time_val.get("max", time_val.get("min", 30))

        # Handle required_equipment as string or list
        equip = item.get("required_equipment")
        if isinstance(equip, list):
            equip = ", ".join(equip) if equip else None

        technique = Technique(
            name=item["name"],
            category=item["category"],
            min_skill_level=item["min_skill_level"],
            required_equipment=equip,
            time_minutes=time_val,
            description=item["description"],
            pro_tip=item.get("pro_tip"),
        )
        session.add(technique)
        name_to_technique[item["name"].lower()] = technique
    await session.flush()

    # Second pass: set fallback references
    for item in data:
        fallback_name = item.get("fallback_technique_name")
        if fallback_name:
            technique = name_to_technique.get(item["name"].lower())
            fallback = name_to_technique.get(fallback_name.lower())
            if technique and fallback:
                technique.fallback_technique_id = fallback.id
    await session.flush()
    print(f"  Seeded {len(data)} techniques")


async def run_seed():
    print("Seeding database...")
    async with async_session() as session:
        async with session.begin():
            name_to_id = await seed_ingredients(session)
            await seed_flavor_profiles(session, name_to_id)
            await seed_flavor_affinities(session, name_to_id)
            await seed_equipment(session)
            await seed_techniques(session)
    print("Seeding complete!")


if __name__ == "__main__":
    asyncio.run(run_seed())
