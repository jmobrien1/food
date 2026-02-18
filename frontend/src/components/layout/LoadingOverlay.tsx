"use client";

export function LoadingOverlay({ message = "Crafting your plan..." }: { message?: string }) {
  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-zinc-950/80 backdrop-blur-sm">
      <div className="text-center">
        <div className="mx-auto mb-4 h-12 w-12 animate-spin rounded-full border-4 border-zinc-700 border-t-amber-500" />
        <p className="font-serif text-xl text-zinc-200">{message}</p>
        <p className="mt-2 text-sm text-zinc-500">
          Our 4-agent pipeline is working: Audit, Translation, Scheduling, Chef Review
        </p>
      </div>
    </div>
  );
}
