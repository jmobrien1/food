"use client";

import { useState, useRef } from "react";
import { Input } from "@/components/ui/input";
import { Badge } from "@/components/ui/badge";
import { useIngredientSearch } from "@/hooks/useIngredientSearch";

interface IngredientInputProps {
  ingredients: string[];
  onChange: (ingredients: string[]) => void;
}

export function IngredientInput({ ingredients, onChange }: IngredientInputProps) {
  const [inputValue, setInputValue] = useState("");
  const [showSuggestions, setShowSuggestions] = useState(false);
  const { results, search } = useIngredientSearch();
  const inputRef = useRef<HTMLInputElement>(null);

  function addIngredient(name: string) {
    const trimmed = name.trim().toLowerCase();
    if (trimmed && !ingredients.includes(trimmed)) {
      onChange([...ingredients, trimmed]);
    }
    setInputValue("");
    setShowSuggestions(false);
    inputRef.current?.focus();
  }

  function removeIngredient(name: string) {
    onChange(ingredients.filter((i) => i !== name));
  }

  function handleKeyDown(e: React.KeyboardEvent) {
    if (e.key === "Enter" && inputValue.trim()) {
      e.preventDefault();
      addIngredient(inputValue);
    }
    if (e.key === "Backspace" && !inputValue && ingredients.length > 0) {
      removeIngredient(ingredients[ingredients.length - 1]);
    }
  }

  function handleChange(e: React.ChangeEvent<HTMLInputElement>) {
    const val = e.target.value;
    setInputValue(val);
    search(val);
    setShowSuggestions(val.length >= 2);
  }

  return (
    <div>
      <label className="mb-2 block text-sm font-medium text-zinc-300">
        Ingredients
      </label>

      <div className="mb-2 flex flex-wrap gap-2">
        {ingredients.map((ing) => (
          <Badge key={ing} variant="accent">
            {ing}
            <button
              onClick={() => removeIngredient(ing)}
              className="ml-1.5 text-amber-300 hover:text-amber-100"
            >
              x
            </button>
          </Badge>
        ))}
      </div>

      <div className="relative">
        <Input
          ref={inputRef}
          value={inputValue}
          onChange={handleChange}
          onKeyDown={handleKeyDown}
          onBlur={() => setTimeout(() => setShowSuggestions(false), 200)}
          placeholder="Type to search or press Enter to add..."
        />

        {showSuggestions && results.length > 0 && (
          <div className="absolute z-10 mt-1 w-full rounded-lg border border-zinc-700 bg-zinc-900 shadow-lg">
            {results.map((r) => (
              <button
                key={r.id}
                onMouseDown={() => addIngredient(r.name)}
                className="flex w-full items-center justify-between px-3 py-2 text-left text-sm text-zinc-300 hover:bg-zinc-800"
              >
                <span>{r.name}</span>
                <span className="text-xs text-zinc-500">{r.category}</span>
              </button>
            ))}
          </div>
        )}
      </div>

      <p className="mt-1 text-xs text-zinc-500">
        {ingredients.length} ingredient{ingredients.length !== 1 ? "s" : ""} added
      </p>
    </div>
  );
}
