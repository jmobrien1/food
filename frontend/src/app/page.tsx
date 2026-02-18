import Link from "next/link";

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center px-4 py-24">
      <div className="max-w-3xl text-center">
        <h1 className="font-serif text-6xl font-bold tracking-tight text-zinc-50 sm:text-7xl">
          Chef de <span className="text-amber-500">Cuisine</span>
        </h1>

        <p className="mt-6 text-xl leading-relaxed text-zinc-400">
          Michelin-level techniques, translated for your kitchen. Tell us what
          you have, and we&apos;ll create a precision execution plan worthy of a
          professional brigade.
        </p>

        <div className="mt-4 flex flex-wrap justify-center gap-3 text-sm text-zinc-500">
          <span className="rounded-full border border-zinc-800 px-3 py-1">
            Gram-Precise Scaling
          </span>
          <span className="rounded-full border border-zinc-800 px-3 py-1">
            Constraint-Aware Planning
          </span>
          <span className="rounded-full border border-zinc-800 px-3 py-1">
            Chef&apos;s Secrets
          </span>
          <span className="rounded-full border border-zinc-800 px-3 py-1">
            Flavor Affinity Engine
          </span>
        </div>

        <div className="mt-12 flex flex-col items-center gap-4 sm:flex-row sm:justify-center">
          <Link
            href="/audit"
            className="rounded-lg bg-amber-600 px-8 py-3 text-lg font-semibold text-zinc-950 transition hover:bg-amber-500"
          >
            Start a Recipe
          </Link>

          <a
            href="#how-it-works"
            className="rounded-lg border border-zinc-700 px-8 py-3 text-lg font-semibold text-zinc-300 transition hover:border-zinc-500 hover:text-zinc-100"
          >
            How It Works
          </a>
        </div>
      </div>

      <section id="how-it-works" className="mt-32 w-full max-w-5xl">
        <h2 className="mb-12 text-center font-serif text-3xl font-semibold text-zinc-200">
          The Pipeline
        </h2>

        <div className="grid gap-8 md:grid-cols-2 lg:grid-cols-4">
          {[
            {
              step: "01",
              title: "The Audit",
              desc: "Map your kitchen: ingredients, equipment, time, and skill level.",
            },
            {
              step: "02",
              title: "Translation",
              desc: "AI transforms constraints into a Michelin-inspired dish concept.",
            },
            {
              step: "03",
              title: "Mise en Temps",
              desc: "A phased timeline: day before, hour before, active cooking.",
            },
            {
              step: "04",
              title: "Chef's Secrets",
              desc: "Finishing touches, plating tips, and the science behind each step.",
            },
          ].map((item) => (
            <div
              key={item.step}
              className="rounded-xl border border-zinc-800 bg-zinc-900/50 p-6"
            >
              <div className="mb-3 text-sm font-bold text-amber-500">
                {item.step}
              </div>
              <h3 className="mb-2 font-serif text-xl font-semibold text-zinc-100">
                {item.title}
              </h3>
              <p className="text-sm leading-relaxed text-zinc-400">
                {item.desc}
              </p>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}
