"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

export function Header() {
  const pathname = usePathname();

  return (
    <header className="border-b border-zinc-800 bg-zinc-950/80 backdrop-blur-sm">
      <div className="mx-auto flex h-16 max-w-6xl items-center justify-between px-4">
        <Link href="/" className="font-serif text-xl font-bold text-zinc-100">
          Chef de <span className="text-amber-500">Cuisine</span>
        </Link>

        <nav className="flex items-center gap-6 text-sm">
          <Link
            href="/audit"
            className={`transition hover:text-zinc-100 ${
              pathname === "/audit" ? "text-amber-500" : "text-zinc-400"
            }`}
          >
            The Audit
          </Link>
        </nav>
      </div>
    </header>
  );
}
