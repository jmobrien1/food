export interface PlanIngredient {
  name: string;
  amount_grams: number;
  original_amount: string;
  is_substitute: boolean;
  substitute_for: string | null;
  scaling_notes: string | null;
}

export interface TimelineTask {
  step: number;
  description: string;
  duration_minutes: number;
  is_active: boolean;
  technique: string | null;
  pro_tip: string | null;
}

export interface TimelinePhase {
  phase: string;
  tasks: TimelineTask[];
}

export interface ChefSecret {
  category: string;
  tip: string;
  why_it_works: string | null;
}

export interface ExecutionPlan {
  dish_name: string;
  dish_description: string;
  serves: number;
  total_time_minutes: number;
  active_time_minutes: number;
  difficulty: string;
  ingredients: PlanIngredient[];
  substitution_notes: string[];
  timeline: TimelinePhase[];
  chefs_secrets: ChefSecret[];
}

export interface PlanGenerateResponse {
  id: string;
  plan: ExecutionPlan;
}

export interface PlanGetResponse {
  id: string;
  plan: ExecutionPlan;
  model_used: string;
  latency_ms: number;
}

export interface PlanGenerateRequest {
  ingredients: string[];
  equipment: string[];
  time_limit_minutes: number;
  user_skill: string;
  guest_count: number;
  intent?: string;
}

export interface IngredientSearchResult {
  id: number;
  name: string;
  category: string;
}

export interface SubstitutionSuggestion {
  original: string;
  substitute: string;
  jaccard_score: number;
  rationale: string;
  adjustment_notes: string | null;
}
