"use client";

import { use } from "react";
import Link from "next/link";
import { Button } from "@/components/ui/button";
import { TimelineView } from "@/components/timeline/TimelineView";
import { usePlan } from "@/hooks/usePlan";

export default function TimelinePage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = use(params);
  const { data, loading, error } = usePlan(id);

  if (loading) {
    return (
      <div className="flex min-h-[50vh] items-center justify-center">
        <div className="h-12 w-12 animate-spin rounded-full border-4 border-zinc-700 border-t-amber-500" />
      </div>
    );
  }

  if (error || !data) {
    return (
      <div className="mx-auto max-w-3xl px-4 py-12 text-center">
        <p className="text-red-300">{error || "Plan not found"}</p>
      </div>
    );
  }

  const { plan } = data;

  return (
    <div className="mx-auto max-w-3xl px-4 py-12">
      <div className="mb-8">
        <Link
          href={`/plan/${id}`}
          className="text-sm text-zinc-500 hover:text-zinc-300"
        >
          &larr; Back to plan
        </Link>
        <h1 className="mt-2 font-serif text-3xl font-bold text-zinc-50">
          Mise en <span className="text-amber-500">Temps</span>
        </h1>
        <p className="mt-1 text-zinc-400">{plan.dish_name}</p>
      </div>

      <TimelineView timeline={plan.timeline} />

      <div className="mt-8">
        <Link href={`/plan/${id}`}>
          <Button variant="outline">Back to Plan Overview</Button>
        </Link>
      </div>
    </div>
  );
}
