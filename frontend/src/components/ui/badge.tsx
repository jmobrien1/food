interface BadgeProps extends React.HTMLAttributes<HTMLSpanElement> {
  variant?: "default" | "accent" | "outline";
}

const variantStyles = {
  default: "bg-zinc-800 text-zinc-300",
  accent: "bg-amber-600/20 text-amber-400 border border-amber-600/30",
  outline: "border border-zinc-700 text-zinc-400",
};

export function Badge({ variant = "default", className = "", ...props }: BadgeProps) {
  return (
    <span
      className={`inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-medium
        ${variantStyles[variant]} ${className}`}
      {...props}
    />
  );
}
