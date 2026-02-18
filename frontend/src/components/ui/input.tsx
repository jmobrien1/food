import { forwardRef } from "react";

interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {}

export const Input = forwardRef<HTMLInputElement, InputProps>(
  ({ className = "", ...props }, ref) => {
    return (
      <input
        ref={ref}
        className={`flex h-10 w-full rounded-lg border border-zinc-700 bg-zinc-900 px-3 py-2 text-sm
          text-zinc-100 placeholder:text-zinc-500 focus:border-amber-600 focus:outline-none
          focus:ring-1 focus:ring-amber-600 disabled:cursor-not-allowed disabled:opacity-50
          ${className}`}
        {...props}
      />
    );
  }
);
Input.displayName = "Input";
