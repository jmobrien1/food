"use client";

import { useCallback, useState } from "react";
import { searchIngredients } from "@/lib/api";
import type { IngredientSearchResult } from "@/lib/types";

export function useIngredientSearch() {
  const [results, setResults] = useState<IngredientSearchResult[]>([]);
  const [loading, setLoading] = useState(false);

  const search = useCallback(async (query: string) => {
    if (query.length < 2) {
      setResults([]);
      return;
    }
    setLoading(true);
    try {
      const data = await searchIngredients(query);
      setResults(data);
    } catch {
      setResults([]);
    } finally {
      setLoading(false);
    }
  }, []);

  return { results, loading, search };
}
