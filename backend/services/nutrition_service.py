# Fake nutrition database
MOCK_DATA = {
    "pizza": {"calories": 300, "protein": 12},
    "burger": {"calories": 250, "protein": 10},
    "fries": {"calories": 200, "protein": 3},
    "coke": {"calories": 150, "protein": 0},
    "coffee": {"calories": 100, "protein": 2}
}

def get_nutrition(items):
    total_calories = 0
    total_protein = 0

    breakdown = []

    for item in items:
        if item in MOCK_DATA:
            data = MOCK_DATA[item]

            total_calories += data["calories"]
            total_protein += data["protein"]

            breakdown.append({
                "item": item,
                "calories": data["calories"],
                "protein": data["protein"]
            })

    return {
        "total_calories": total_calories,
        "total_protein": total_protein,
        "breakdown": breakdown
    }