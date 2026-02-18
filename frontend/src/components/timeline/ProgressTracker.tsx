interface ProgressTrackerProps {
  total: number;
  completed: number;
}

export function ProgressTracker({ total, completed }: ProgressTrackerProps) {
  const percent = total > 0 ? Math.round((completed / total) * 100) : 0;

  return (
    <div className="rounded-xl border border-zinc-800 bg-zinc-900/50 p-4">
      <div className="flex items-center justify-between text-sm">
        <span className="text-zinc-400">Progress</span>
        <span className="font-mono font-semibold text-amber-400">
          {completed}/{total} tasks ({percent}%)
        </span>
      </div>
      <div className="mt-2 h-2 overflow-hidden rounded-full bg-zinc-800">
        <div
          className="h-full rounded-full bg-amber-500 transition-all duration-500"
          style={{ width: `${percent}%` }}
        />
      </div>
    </div>
  );
}
