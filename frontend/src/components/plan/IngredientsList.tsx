import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import type { PlanIngredient } from "@/lib/types";

interface IngredientsListProps {
  ingredients: PlanIngredient[];
}

export function IngredientsList({ ingredients }: IngredientsListProps) {
  return (
    <Card>
      <CardHeader>
        <CardTitle>Ingredients</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="divide-y divide-zinc-800">
          {ingredients.map((ing, i) => (
            <div key={i} className="flex items-center justify-between py-3">
              <div className="flex items-center gap-3">
                <span className="text-zinc-200">{ing.name}</span>
                {ing.is_substitute && (
                  <Badge variant="accent">sub for {ing.substitute_for}</Badge>
                )}
              </div>
              <div className="text-right">
                <span className="font-mono text-sm font-semibold text-amber-400">
                  {ing.amount_grams}g
                </span>
                <span className="ml-2 text-sm text-zinc-500">
                  ({ing.original_amount})
                </span>
              </div>
            </div>
          ))}
        </div>
      </CardContent>
    </Card>
  );
}
