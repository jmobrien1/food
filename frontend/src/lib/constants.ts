export const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8001";

export const SKILL_LEVELS = [
  { value: "Home Cook", label: "Home Cook", description: "Comfortable with basics, learning new skills" },
  { value: "Ambitious Amateur", label: "Ambitious Amateur", description: "Confident with most techniques, seeks challenges" },
  { value: "Serious Enthusiast", label: "Serious Enthusiast", description: "Advanced skills, professional-level ambition" },
] as const;

export const COMMON_EQUIPMENT = [
  { name: "Cast Iron Skillet", category: "Cookware" },
  { name: "Stainless Steel Pan", category: "Cookware" },
  { name: "Dutch Oven", category: "Cookware" },
  { name: "Sheet Pan", category: "Cookware" },
  { name: "Saucepan", category: "Cookware" },
  { name: "Stockpot", category: "Cookware" },
  { name: "Oven", category: "Appliance" },
  { name: "Stand Mixer", category: "Appliance" },
  { name: "Food Processor", category: "Appliance" },
  { name: "Blender", category: "Appliance" },
  { name: "Immersion Blender", category: "Appliance" },
  { name: "Immersion Circulator", category: "Specialty" },
  { name: "Kitchen Torch", category: "Specialty" },
  { name: "Grill", category: "Cookware" },
  { name: "Wok", category: "Cookware" },
  { name: "Mandoline", category: "Tool" },
  { name: "Microplane", category: "Tool" },
  { name: "Mortar and Pestle", category: "Tool" },
  { name: "Thermometer", category: "Tool" },
  { name: "Kitchen Scale", category: "Tool" },
] as const;
