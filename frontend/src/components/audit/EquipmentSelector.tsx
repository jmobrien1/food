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

  function selectAll() {
    onChange(COMMON_EQUIPMENT.map((e) => e.name));
  }

  function clearAll() {
    onChange([]);
  }

  const categories = [...new Set(COMMON_EQUIPMENT.map((e) => e.category))];

  return (
    <div>
      <div className="mb-2 flex items-center justify-between">
        <label className="text-sm font-medium text-zinc-300">Equipment</label>
        <div className="flex gap-3 text-xs">
          <button
            type="button"
            onClick={selectAll}
            className="text-amber-500 hover:text-amber-400"
          >
            Select All
          </button>
          <button
            type="button"
            onClick={clearAll}
            className="text-zinc-500 hover:text-zinc-400"
          >
            Clear
          </button>
        </div>
      </div>

      {categories.map((category) => (
        <div key={category} className="mb-3">
          <p className="mb-1.5 text-xs font-medium uppercase tracking-wider text-zinc-500">
            {category}
          </p>
          <div className="flex flex-wrap gap-x-4 gap-y-1">
            {COMMON_EQUIPMENT.filter((e) => e.category === category).map((equip) => (
              <label
                key={equip.name}
                className="flex cursor-pointer items-center gap-2 py-1 text-sm"
              >
                <input
                  type="checkbox"
                  checked={selected.includes(equip.name)}
                  onChange={() => toggle(equip.name)}
                  className="h-4 w-4 rounded border-zinc-600 bg-zinc-800 text-amber-500 accent-amber-500 focus:ring-amber-600"
                />
                <span
                  className={
                    selected.includes(equip.name) ? "text-zinc-200" : "text-zinc-400"
                  }
                >
                  {equip.name}
                </span>
              </label>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
}
