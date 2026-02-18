"use client";

import { TaskCard } from "./TaskCard";
import type { TimelinePhase as TimelinePhaseType } from "@/lib/types";

interface TimelinePhaseProps {
  phase: TimelinePhaseType;
  checkedTasks: Set<string>;
  onToggleTask: (key: string) => void;
}

export function TimelinePhase({ phase, checkedTasks, onToggleTask }: TimelinePhaseProps) {
  const completedCount = phase.tasks.filter((t) =>
    checkedTasks.has(`${phase.phase}-${t.step}`)
  ).length;

  return (
    <div className="relative">
      <div className="mb-4 flex items-center gap-3">
        <div className="flex h-8 w-8 items-center justify-center rounded-full bg-amber-600/20">
          <div className="h-3 w-3 rounded-full bg-amber-500" />
        </div>
        <div>
          <h3 className="font-serif text-lg font-semibold text-zinc-100">
            {phase.phase}
          </h3>
          <p className="text-xs text-zinc-500">
            {completedCount}/{phase.tasks.length} tasks complete
          </p>
        </div>
      </div>

      <div className="ml-4 space-y-3 border-l border-zinc-800 pl-8">
        {phase.tasks.map((task) => {
          const key = `${phase.phase}-${task.step}`;
          return (
            <TaskCard
              key={key}
              task={task}
              checked={checkedTasks.has(key)}
              onToggle={() => onToggleTask(key)}
            />
          );
        })}
      </div>
    </div>
  );
}
