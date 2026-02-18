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

export function AuditForm({ onSubmit, loading }: AuditFormProps) {
  const [ingredients, setIngredients] = useState<string[]>([]);
  const [equipment, setEquipment] = useState<string[]>([]);
  const [skill, setSkill] = useState("Ambitious Amateur");
  const [timeLimit, setTimeLimit] = useState(90);
  const [guestCount, setGuestCount] = useState(4);
  const [intent, setIntent] = useState("");

  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    if (ingredients.length === 0) return;

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
      <IngredientInput ingredients={ingredients} onChange={setIngredients} />

      <EquipmentSelector selected={equipment} onChange={setEquipment} />

      <SkillSelector value={skill} onChange={setSkill} />

      <div className="grid gap-6 sm:grid-cols-2">
        <div>
          <label className="mb-2 block text-sm font-medium text-zinc-300">
            Time Budget (minutes)
          </label>
          <div className="flex items-center gap-4">
            <input
              type="range"
              min={15}
              max={480}
              step={15}
              value={timeLimit}
              onChange={(e) => setTimeLimit(Number(e.target.value))}
              className="h-2 w-full cursor-pointer appearance-none rounded-lg bg-zinc-700 accent-amber-500"
            />
            <span className="min-w-[4rem] text-right text-lg font-semibold text-amber-400">
              {timeLimit >= 60
                ? `${Math.floor(timeLimit / 60)}h${timeLimit % 60 ? ` ${timeLimit % 60}m` : ""}`
                : `${timeLimit}m`}
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

      <div>
        <label className="mb-2 block text-sm font-medium text-zinc-300">
          Intent (optional)
        </label>
        <Input
          value={intent}
          onChange={(e) => setIntent(e.target.value)}
          placeholder="e.g., 'Something elegant for a dinner party' or 'Comfort food, big flavors'"
        />
      </div>

      <Button type="submit" size="lg" disabled={loading || ingredients.length === 0}>
        {loading ? "Generating Plan..." : "Generate Execution Plan"}
      </Button>
    </form>
  );
}
