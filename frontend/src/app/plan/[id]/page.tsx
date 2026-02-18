"use client";

import { use } from "react";
import Link from "next/link";
import { Button } from "@/components/ui/button";
import { PlanHeader } from "@/components/plan/PlanHeader";
import { IngredientsList } from "@/components/plan/IngredientsList";
import { SubstitutionNotes } from "@/components/plan/SubstitutionNotes";
import { ChefSecrets } from "@/components/plan/ChefSecrets";
import { usePlan } from "@/hooks/usePlan";

export default function PlanPage({ params }: { params: Promise<{ id: string }> }) {
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
      <div className="mx-auto max-w-3xl px-4 py-12">
        <div className="rounded-lg border border-red-800 bg-red-950/50 p-6 text-center">
          <p className="text-red-300">{error || "Plan not found"}</p>
          <Link href="/audit" className="mt-4 inline-block text-sm text-amber-500 hover:underline">
            Start a new recipe
          </Link>
        </div>
      </div>
    );
  }

  const { plan } = data;

  return (
    <div className="mx-auto max-w-3xl px-4 py-12">
      <PlanHeader plan={plan} />

      <div className="space-y-6">
        <IngredientsList ingredients={plan.ingredients} />
        <SubstitutionNotes notes={plan.substitution_notes} />
        <ChefSecrets secrets={plan.chefs_secrets} />

        <div className="flex gap-4">
          <Link href={`/plan/${id}/timeline`}>
            <Button size="lg">View Timeline</Button>
          </Link>
          <Link href="/audit">
            <Button variant="outline" size="lg">
              New Recipe
            </Button>
          </Link>
        </div>
      </div>
    </div>
  );
}
