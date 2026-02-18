"use client";

import { Badge } from "@/components/ui/badge";
import type { TimelineTask } from "@/lib/types";

interface TaskCardProps {
  task: TimelineTask;
  checked: boolean;
  onToggle: () => void;
}

export function TaskCard({ task, checked, onToggle }: TaskCardProps) {
  return (
    <div
      className={`rounded-lg border p-4 transition ${
        checked
          ? "border-zinc-700 bg-zinc-900/30 opacity-60"
          : task.is_active
            ? "border-amber-800/50 bg-amber-950/20"
            : "border-zinc-800 bg-zinc-900/50"
      }`}
    >
      <div className="flex items-start gap-3">
        <button
          onClick={onToggle}
          className={`mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded border transition ${
            checked
              ? "border-amber-600 bg-amber-600 text-zinc-950"
              : "border-zinc-600 hover:border-zinc-400"
          }`}
        >
          {checked && (
            <svg className="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={3} d="M5 13l4 4L19 7" />
            </svg>
          )}
        </button>

        <div className="flex-1">
          <div className="flex items-center gap-2">
            <span className={`text-sm ${checked ? "line-through text-zinc-500" : "text-zinc-200"}`}>
              {task.description}
            </span>
          </div>

          <div className="mt-1.5 flex items-center gap-2">
            <Badge variant={task.is_active ? "accent" : "outline"}>
              {task.is_active ? "Active" : "Passive"} - {task.duration_minutes}min
            </Badge>
            {task.technique && (
              <span className="text-xs text-zinc-500">{task.technique}</span>
            )}
          </div>

          {task.pro_tip && (
            <p className="mt-2 text-xs italic text-zinc-500">
              Tip: {task.pro_tip}
            </p>
          )}
        </div>
      </div>
    </div>
  );
}
