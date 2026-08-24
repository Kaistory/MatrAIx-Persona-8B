/** Contrast attribute combinations for Generation (extra stamped datasets). */

import type { OverlayContrastArm, OverlayDimension } from "@/lib/types";

export function overlayContrastPlan(
  overlay: OverlayDimension[],
  extrasById: Record<string, string[] | undefined>,
): OverlayContrastArm[] {
  const overlayById = new Map(overlay.map((dim) => [dim.id, dim]));
  const arms: OverlayContrastArm[] = [];
  for (const [id, raw] of Object.entries(extrasById)) {
    const picked = (raw ?? []).filter((value) => value.trim().length > 0);
    if (picked.length === 0) continue;
    const dim = overlayById.get(id);
    const values = dim
      ? picked.filter((value) => dim.values.includes(value))
      : [...new Set(picked)];
    if (values.length === 0) continue;
    const baseValue =
      dim?.values.find((value) => !values.includes(value)) ??
      dim?.values[0] ??
      values[0];
    if (!baseValue) continue;
    arms.push({ overlayId: id, baseValue, values });
  }
  return arms;
}

export function contrastSequenceLabel(arm: OverlayContrastArm): string {
  return arm.values.join(", ");
}

export function contrastDraftFromPlan(plan: OverlayContrastArm[] | undefined): {
  ids: string[];
  extras: Record<string, string[]>;
} {
  const extras: Record<string, string[]> = {};
  const ids: string[] = [];
  for (const arm of plan ?? []) {
    if (!arm.overlayId || arm.values.length === 0) continue;
    ids.push(arm.overlayId);
    extras[arm.overlayId] = [...arm.values];
  }
  return { ids, extras };
}

/** Number of stamped contrast datasets (one per attribute combination). */
export function contrastCopyCount(plan: OverlayContrastArm[]): number {
  if (plan.length === 0) return 0;
  return plan.reduce(
    (product, arm) => product * Math.max(arm.values.length, 1),
    1,
  );
}

/**
 * Contrast-family dataset count: base-value pool plus one stamped copy
 * per attribute combination.
 */
export function contrastDatasetCount(plan: OverlayContrastArm[]): number {
  if (plan.length === 0) return 0;
  return 1 + contrastCopyCount(plan);
}

export function contrastCombinations(
  plan: OverlayContrastArm[],
): Record<string, string>[] {
  if (plan.length === 0) return [];
  return plan.reduce<Record<string, string>[]>((rows, arm) => {
    if (rows.length === 0) {
      return arm.values.map((value) => ({ [arm.overlayId]: value }));
    }
    return rows.flatMap((row) =>
      arm.values.map((value) => ({ ...row, [arm.overlayId]: value })),
    );
  }, []);
}

export function contrastBaseStamps(
  plan: OverlayContrastArm[],
): Record<string, string> {
  const out: Record<string, string> = {};
  for (const arm of plan) {
    if (arm.overlayId && arm.baseValue) {
      out[arm.overlayId] = arm.baseValue;
    }
  }
  return out;
}

/** ``Contrast · Brand=Low`` for progress / dataset labels. */
export function contrastStampLabel(
  stamps: Record<string, string>,
  dimLabel: (id: string) => string,
): string {
  const bits = Object.entries(stamps).map(
    ([id, value]) => `${dimLabel(id)}=${value}`,
  );
  return bits.length > 0 ? `Contrast · ${bits.join(", ")}` : "Contrast";
}
