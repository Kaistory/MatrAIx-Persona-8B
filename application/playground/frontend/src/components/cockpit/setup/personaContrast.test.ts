import { describe, expect, it } from "vitest";

import type { OverlayDimension } from "@/lib/types";

import {
  contrastCombinations,
  contrastCopyCount,
  contrastDatasetCount,
  overlayContrastPlan,
} from "./personaContrast";

const device: OverlayDimension = {
  id: "device",
  label: "Device",
  values: ["Iphone", "Android", "Xiaomi"],
};

const membership: OverlayDimension = {
  id: "amazon_membership",
  label: "Amazon Membership",
  values: ["yes", "no"],
};

describe("overlayContrastPlan", () => {
  it("builds arms from selected contrast attributes", () => {
    expect(
      overlayContrastPlan(
        [device],
        { device: ["Iphone", "Android"] },
      ),
    ).toEqual([
      {
        overlayId: "device",
        baseValue: "Xiaomi",
        values: ["Iphone", "Android"],
      },
    ]);
  });

  it("allows every attribute on a dimension as contrast values", () => {
    expect(
      overlayContrastPlan(
        [membership],
        { amazon_membership: ["yes", "no"] },
      ),
    ).toEqual([
      {
        overlayId: "amazon_membership",
        baseValue: "yes",
        values: ["yes", "no"],
      },
    ]);
  });

  it("accepts several dimensions including profile-dimension ids", () => {
    const plan = overlayContrastPlan(
      [device, membership],
      {
        device: ["Xiaomi"],
        amazon_membership: ["yes"],
        gender: ["Female"],
      },
    );
    expect(plan.map((arm) => arm.overlayId)).toEqual([
      "device",
      "amazon_membership",
      "gender",
    ]);
    expect(contrastDatasetCount(plan)).toBe(2);
    expect(contrastCopyCount(plan)).toBe(1);
    expect(contrastCombinations(plan)).toEqual([
      { device: "Xiaomi", amazon_membership: "yes", gender: "Female" },
    ]);
  });

  it("expands several dimensions into one dataset per combination", () => {
    const plan = overlayContrastPlan(
      [device, membership],
      {
        device: ["Iphone", "Android"],
        amazon_membership: ["yes", "no"],
      },
    );
    expect(contrastCopyCount(plan)).toBe(4);
    expect(contrastDatasetCount(plan)).toBe(5);
    expect(contrastCombinations(plan)).toEqual([
      { device: "Iphone", amazon_membership: "yes" },
      { device: "Iphone", amazon_membership: "no" },
      { device: "Android", amazon_membership: "yes" },
      { device: "Android", amazon_membership: "no" },
    ]);
  });
});
