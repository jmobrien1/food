"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { IngredientInput } from "./IngredientInput";
import { EquipmentSelector } from "./EquipmentSelector";
import { SkillSelector } from "./SkillSelector";
import type { PlanGenerateRequest } from "@/lib/types";

interface AuditFormProps {
  onSubmit: (request: PlanGenerateRequest) => void;
  loading?: boolean;
}

const TIME_STOPS = [
  15, 30, 45, 60, 90, 120, 180, 240, 360, 480, 720, 1440, 2880, 0,
] as const;

function formatTime(minutes: number): string {
  if (minutes === 0) return "Unlimited";
  if (minutes < 60) return `${minutes}m`;
  if (minutes < 1440) {
    const h = Math.floor(minutes / 60);
    const m = minutes % 60;
    return m ? `${h}h ${m}m` : `${h}h`;
  }
  const d = Math.floor(minutes / 1440);
  const rem = minutes % 1440;
  if (!rem) return `${d}d`;
  const h = Math.floor(rem / 60);
  return h ? `${d}d ${h}h` : `${d}d`;
}

export function AuditForm({ onSubmit, loading }: AuditFormProps) {
  const [ingredients, setIngredients] = useState<string[]>([]);
  const [equipment, setEquipment] = useState<string[]>([]);
  const [skill, setSkill] = useState("Ambitious Amateur");
  const [timeIndex, setTimeIndex] = useState(4); // default 90 min
  const [guestCount, setGuestCount] = useState(4);
  const [intent, setIntent] = useState("");

  const timeLimit = TIME_STOPS[timeIndex];

  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();

    onSubmit({
      ingredients,
      equipment,
      time_limit_minutes: timeLimit,
      user_skill: skill,
      guest_count: guestCount,
      intent: intent || undefined,
    });
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-8">
      <div>
        <label className="mb-2 block text-sm font-medium text-zinc-300">
          What delicious meal do you want to make?
        </label>
        <Input
          value={intent}
          onChange={(e) => setIntent(e.target.value)}
          placeholder="e.g., 'Something elegant for a dinner party' or 'Comfort food, big flavors'"
        />
      </div>

      <IngredientInput ingredients={ingredients} onChange={setIngredients} />

      <EquipmentSelector selected={equipment} onChange={setEquipment} />

      <SkillSelector value={skill} onChange={setSkill} />

      <div className="grid gap-6 sm:grid-cols-2">
        <div>
          <label className="mb-2 block text-sm font-medium text-zinc-300">
            Time Budget
          </label>
          <div className="flex items-center gap-4">
            <input
              type="range"
              min={0}
              max={TIME_STOPS.length - 1}
              step={1}
              value={timeIndex}
              onChange={(e) => setTimeIndex(Number(e.target.value))}
              className="h-2 w-full cursor-pointer appearance-none rounded-lg bg-zinc-700 accent-amber-500"
            />
            <span className="min-w-[5rem] text-right text-lg font-semibold text-amber-400">
              {formatTime(timeLimit)}
            </span>
          </div>
        </div>

        <div>
          <label className="mb-2 block text-sm font-medium text-zinc-300">
            Guest Count
          </label>
          <div className="flex items-center gap-3">
            <Button
              type="button"
              variant="outline"
              size="sm"
              onClick={() => setGuestCount(Math.max(1, guestCount - 1))}
            >
              -
            </Button>
            <span className="min-w-[3rem] text-center text-2xl font-bold text-zinc-100">
              {guestCount}
            </span>
            <Button
              type="button"
              variant="outline"
              size="sm"
              onClick={() => setGuestCount(Math.min(20, guestCount + 1))}
            >
              +
            </Button>
          </div>
        </div>
      </div>

      <Button type="submit" size="lg" disabled={loading}>
        {loading ? "Generating Plan..." : "Generate Execution Plan"}
      </Button>
    </form>
  );
}
