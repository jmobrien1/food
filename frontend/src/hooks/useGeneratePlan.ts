"use client";

import { useState } from "react";
import { generatePlan } from "@/lib/api";
import type { PlanGenerateRequest, PlanGenerateResponse } from "@/lib/types";

export function useGeneratePlan() {
  const [data, setData] = useState<PlanGenerateResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function generate(request: PlanGenerateRequest) {
    setLoading(true);
    setError(null);
    try {
      const result = await generatePlan(request);
      setData(result);
      return result;
    } catch (err) {
      const message = err instanceof Error ? err.message : "Unknown error";
      setError(message);
      return null;
    } finally {
      setLoading(false);
    }
  }

  return { data, loading, error, generate };
}
