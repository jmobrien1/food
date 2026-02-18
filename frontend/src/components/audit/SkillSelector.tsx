"use client";

import { SKILL_LEVELS } from "@/lib/constants";

interface SkillSelectorProps {
  value: string;
  onChange: (skill: string) => void;
}

export function SkillSelector({ value, onChange }: SkillSelectorProps) {
  return (
    <div>
      <label className="mb-2 block text-sm font-medium text-zinc-300">
        Skill Level
      </label>

      <div className="grid gap-3 sm:grid-cols-3">
        {SKILL_LEVELS.map((level) => (
          <button
            key={level.value}
            type="button"
            onClick={() => onChange(level.value)}
            className={`rounded-xl border p-4 text-left transition ${
              value === level.value
                ? "border-amber-600 bg-amber-600/10"
                : "border-zinc-700 hover:border-zinc-500"
            }`}
          >
            <p
              className={`font-medium ${
                value === level.value ? "text-amber-400" : "text-zinc-200"
              }`}
            >
              {level.label}
            </p>
            <p className="mt-1 text-xs text-zinc-500">{level.description}</p>
          </button>
        ))}
      </div>
    </div>
  );
}
