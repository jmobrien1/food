"use client";

import { useRouter } from "next/navigation";
import { AuditForm } from "@/components/audit/AuditForm";
import { LoadingOverlay } from "@/components/layout/LoadingOverlay";
import { useGeneratePlan } from "@/hooks/useGeneratePlan";
import type { PlanGenerateRequest } from "@/lib/types";

export default function AuditPage() {
  const router = useRouter();
  const { loading, error, generate } = useGeneratePlan();

  async function handleSubmit(request: PlanGenerateRequest) {
    const result = await generate(request);
    if (result) {
      router.push(`/plan/${result.id}`);
    }
  }

  return (
    <div className="mx-auto max-w-3xl px-4 py-12">
      {loading && <LoadingOverlay />}

      <div className="mb-8">
        <h1 className="font-serif text-4xl font-bold text-zinc-50">
          Start a <span className="text-amber-500">Recipe</span>
        </h1>
        <p className="mt-2 text-zinc-400">
          Tell us what you want to cook. We&apos;ll design a dish and give you
          a step-by-step execution plan.
        </p>
      </div>

      {error && (
        <div className="mb-6 rounded-lg border border-red-800 bg-red-950/50 p-4 text-sm text-red-300">
          {error}
        </div>
      )}

      <AuditForm onSubmit={handleSubmit} loading={loading} />
    </div>
  );
}
