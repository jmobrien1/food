"use client";

import { useState } from "react";
import { TimelinePhase } from "./TimelinePhase";
import { ProgressTracker } from "./ProgressTracker";
import type { TimelinePhase as TimelinePhaseType } from "@/lib/types";

interface TimelineViewProps {
  timeline: TimelinePhaseType[];
}

export function TimelineView({ timeline }: TimelineViewProps) {
  const [checkedTasks, setCheckedTasks] = useState<Set<string>>(new Set());

  const totalTasks = timeline.reduce((sum, phase) => sum + phase.tasks.length, 0);
  const completedTasks = checkedTasks.size;

  function toggleTask(key: string) {
    setCheckedTasks((prev) => {
      const next = new Set(prev);
      if (next.has(key)) {
        next.delete(key);
      } else {
        next.add(key);
      }
      return next;
    });
  }

  return (
    <div>
      <ProgressTracker total={totalTasks} completed={completedTasks} />

      <div className="mt-8 space-y-10">
        {timeline.map((phase) => (
          <TimelinePhase
            key={phase.phase}
            phase={phase}
            checkedTasks={checkedTasks}
            onToggleTask={toggleTask}
          />
        ))}
      </div>
    </div>
  );
}
