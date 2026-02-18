"use client";

import { useEffect, useState } from "react";
import { getPlan } from "@/lib/api";
import type { PlanGetResponse } from "@/lib/types";

export function usePlan(planId: string) {
  const [data, setData] = useState<PlanGetResponse | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function fetchPlan() {
      try {
        const result = await getPlan(planId);
        setData(result);
      } catch (err) {
        setError(err instanceof Error ? err.message : "Failed to load plan");
      } finally {
        setLoading(false);
      }
    }
    fetchPlan();
  }, [planId]);

  return { data, loading, error };
}
