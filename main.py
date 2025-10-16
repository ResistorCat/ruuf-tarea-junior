from typing import List, Tuple, Dict
import json


class Panel:
    panel_idx = 1

    def __init__(self, width: int, height: int) -> None:
        self.idx = Panel.panel_idx
        Panel.panel_idx += 1
        self.width = width
        self.height = height

    def rotate(self) -> None:
        self.width, self.height = self.height, self.width
    
    def area(self) -> int:
        return self.width * self.height


class Roof:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.matrix = [[0] * width for _ in range(height)]
        self.remaining_area = width * height
        self.panels_count = 0
    
    def area(self) -> int:
        return self.width * self.height
    
    def can_place(self, panel: Panel, x: int, y: int) -> bool:
        for dy in range(panel.height):
            for dx in range(panel.width):
                if self.matrix[y + dy][x + dx] != 0:
                    return False
        return True
    
    def place(self, panel: Panel, x: int, y: int) -> None:
        for dy in range(panel.height):
            for dx in range(panel.width):
                self.matrix[y + dy][x + dx] = panel.idx
        self.remaining_area -= panel.area()
        self.panels_count += 1
    
    def try_place(self, panel: Panel) -> bool:
        if self.remaining_area >= panel.area():
            for y in range(self.height - panel.height + 1):
                for x in range(self.width - panel.width + 1):
                    if self.can_place(panel, x, y):
                        self.place(panel, x, y)
                        return True
        return False

    def __str__(self):
        return '\n'.join(' '.join(f"{cell:2}" for cell in row) for row in self.matrix)


def calculate_panels(panel_width: int, panel_height: int, 
                    roof_width: int, roof_height: int) -> int:
    
    # Implementa acá tu solución
    roof = Roof(roof_width, roof_height)
    while True:
        panel = Panel(panel_width, panel_height)
        if not roof.try_place(panel):
            panel.rotate()
            if not roof.try_place(panel):
                break
    
    print(roof)
    
    return roof.panels_count


def bonus() -> None:
    # Solución a bonus 2
    roof = Roof(9, 4)
    for i in range(4):
        roof.matrix[0][i] = -1
        roof.matrix[-1][-i-1] = -1
    print(f"Bonus 2: techo de {roof.width}x{roof.height} con esquinas de 1x4 ocupadas")
    print(roof)
    panel_width, panel_height = 1, 2
    print(f"Colocando paneles de {panel_width}x{panel_height}")
    while True:
        panel = Panel(panel_width, panel_height)
        if not roof.try_place(panel):
            panel.rotate()
            if not roof.try_place(panel):
                break
    print(roof)
    print(f"Se colocaron {roof.panels_count} paneles\n")


def run_tests() -> None:
    with open('test_cases.json', 'r') as f:
        data = json.load(f)
        test_cases: List[Dict[str, int]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "expected": test["expected"]
            }
            for test in data["testCases"]
        ]
    
    print("Corriendo tests:")
    print("-------------------")
    
    for i, test in enumerate(test_cases, 1):
        result = calculate_panels(
            test["panel_w"], test["panel_h"], 
            test["roof_w"], test["roof_h"]
        )
        passed = result == test["expected"]
        
        print(f"Test {i}:")
        print(f"  Panels: {test['panel_w']}x{test['panel_h']}, "
              f"Roof: {test['roof_w']}x{test['roof_h']}")
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")


def main() -> None:
    print("🐕 Wuuf wuuf wuuf 🐕")
    print("================================\n")
    
    run_tests()


if __name__ == "__main__":
    main()
    bonus()
