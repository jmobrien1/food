import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

interface SubstitutionNotesProps {
  notes: string[];
}

export function SubstitutionNotes({ notes }: SubstitutionNotesProps) {
  if (notes.length === 0) return null;

  return (
    <Card>
      <CardHeader>
        <CardTitle>Substitution Notes</CardTitle>
      </CardHeader>
      <CardContent>
        <ul className="space-y-2">
          {notes.map((note, i) => (
            <li key={i} className="flex gap-2 text-sm text-zinc-400">
              <span className="text-amber-500">*</span>
              {note}
            </li>
          ))}
        </ul>
      </CardContent>
    </Card>
  );
}
