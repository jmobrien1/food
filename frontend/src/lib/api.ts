import { API_URL } from "./constants";
import type {
  IngredientSearchResult,
  PlanGenerateRequest,
  PlanGenerateResponse,
  PlanGetResponse,
  SubstitutionSuggestion,
} from "./types";

async function fetchApi<T>(path: string, options?: RequestInit): Promise<T> {
  const res = await fetch(`${API_URL}${path}`, {
    headers: { "Content-Type": "application/json" },
    ...options,
  });
  if (!res.ok) {
    const body = await res.text();
    throw new Error(`API error ${res.status}: ${body}`);
  }
  return res.json();
}

export async function generatePlan(
  request: PlanGenerateRequest
): Promise<PlanGenerateResponse> {
  return fetchApi("/api/v1/plans/generate", {
    method: "POST",
    body: JSON.stringify(request),
  });
}

export async function getPlan(planId: string): Promise<PlanGetResponse> {
  return fetchApi(`/api/v1/plans/${planId}`);
}

export async function searchIngredients(
  query: string,
  limit = 10
): Promise<IngredientSearchResult[]> {
  return fetchApi(
    `/api/v1/ingredients?q=${encodeURIComponent(query)}&limit=${limit}`
  );
}

export async function suggestSubstitutions(
  ingredientName: string,
  availableIngredients: string[] = []
): Promise<{ suggestions: SubstitutionSuggestion[] }> {
  return fetchApi("/api/v1/substitutions/suggest", {
    method: "POST",
    body: JSON.stringify({
      ingredient_name: ingredientName,
      available_ingredients: availableIngredients,
    }),
  });
}
