"use client";

import { COMMON_EQUIPMENT } from "@/lib/constants";

interface EquipmentSelectorProps {
  selected: string[];
  onChange: (equipment: string[]) => void;
}

export function EquipmentSelector({ selected, onChange }: EquipmentSelectorProps) {
  function toggle(name: string) {
    if (selected.includes(name)) {
      onChange(selected.filter((e) => e !== name));
    } else {
      onChange([...selected, name]);
    }
  }

  const categories = [...new Set(COMMON_EQUIPMENT.map((e) => e.category))];

  return (
    <div>
      <label className="mb-2 block text-sm font-medium text-zinc-300">
        Equipment
      </label>

      {categories.map((category) => (
        <div key={category} className="mb-3">
          <p className="mb-1.5 text-xs font-medium uppercase tracking-wider text-zinc-500">
            {category}
          </p>
          <div className="flex flex-wrap gap-2">
            {COMMON_EQUIPMENT.filter((e) => e.category === category).map((equip) => (
              <button
                key={equip.name}
                type="button"
                onClick={() => toggle(equip.name)}
                className={`rounded-lg border px-3 py-1.5 text-sm transition ${
                  selected.includes(equip.name)
                    ? "border-amber-600 bg-amber-600/10 text-amber-400"
                    : "border-zinc-700 text-zinc-400 hover:border-zinc-500"
                }`}
              >
                {equip.name}
              </button>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
}
