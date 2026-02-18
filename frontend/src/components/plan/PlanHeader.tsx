import { Badge } from "@/components/ui/badge";
import type { ExecutionPlan } from "@/lib/types";

interface PlanHeaderProps {
  plan: ExecutionPlan;
}

export function PlanHeader({ plan }: PlanHeaderProps) {
  return (
    <div className="mb-8">
      <h1 className="font-serif text-4xl font-bold text-zinc-50">
        {plan.dish_name}
      </h1>
      <p className="mt-3 text-lg leading-relaxed text-zinc-400">
        {plan.dish_description}
      </p>

      <div className="mt-4 flex flex-wrap gap-3">
        <Badge variant="accent">{plan.difficulty}</Badge>
        <Badge variant="outline">Serves {plan.serves}</Badge>
        <Badge variant="outline">{plan.total_time_minutes} min total</Badge>
        <Badge variant="outline">{plan.active_time_minutes} min active</Badge>
      </div>
    </div>
  );
}
