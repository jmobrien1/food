"use client";

import { useState } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import type { ChefSecret } from "@/lib/types";

interface ChefSecretsProps {
  secrets: ChefSecret[];
}

const categoryColors: Record<string, string> = {
  Finishing: "text-emerald-400 border-emerald-600/30",
  Plating: "text-violet-400 border-violet-600/30",
  "Flavor Boost": "text-amber-400 border-amber-600/30",
  Timing: "text-sky-400 border-sky-600/30",
};

export function ChefSecrets({ secrets }: ChefSecretsProps) {
  const [expandedIndex, setExpandedIndex] = useState<number | null>(null);

  if (secrets.length === 0) return null;

  return (
    <Card>
      <CardHeader>
        <CardTitle>Chef&apos;s Secrets</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="space-y-3">
          {secrets.map((secret, i) => {
            const colorClass = categoryColors[secret.category] || "text-zinc-400 border-zinc-600/30";
            const isExpanded = expandedIndex === i;

            return (
              <button
                key={i}
                onClick={() => setExpandedIndex(isExpanded ? null : i)}
                className="w-full rounded-lg border border-zinc-800 p-4 text-left transition hover:border-zinc-700"
              >
                <div className="flex items-start gap-3">
                  <span
                    className={`shrink-0 rounded-full border px-2 py-0.5 text-xs font-medium ${colorClass}`}
                  >
                    {secret.category}
                  </span>
                  <p className="text-sm text-zinc-200">{secret.tip}</p>
                </div>

                {isExpanded && secret.why_it_works && (
                  <p className="mt-3 pl-[4.5rem] text-xs leading-relaxed text-zinc-500">
                    {secret.why_it_works}
                  </p>
                )}
              </button>
            );
          })}
        </div>
      </CardContent>
    </Card>
  );
}
