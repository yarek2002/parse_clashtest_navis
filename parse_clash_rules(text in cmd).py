import xml.etree.ElementTree as ET
from pathlib import Path

def extract_clashtest_rules(xml_path: str):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    print("Найденные clash test'ы и их правила:\n" + "="*80)

    for clashtest in root.findall(".//clashtest"):
        clash_name = clashtest.get("name")
        if not clash_name:
            continue

        print(f"Clashtest: {clash_name}")

        rules_block = clashtest.find("rules")
        if rules_block is None or len(rules_block) == 0:
            print("  -> правил нет\n")
            continue  # <-- теперь правильно

        # цикл по правилам — теперь выполняется
        for rule in rules_block.findall("rule"):
            rule_name = rule.get("name")
            enabled = rule.get("enabled", "1")
            status = "включено" if enabled == "1" else "выключено"

            print(f"   * {rule_name} ({status})")

        print()


if __name__ == "__main__":
    xml_file = r"D:\загрузки\!К32_SM_Block_B_GF_увязка (ПЧ)_v3.xml"

    if not Path(xml_file).exists():
        print(f"Файл не найден: {xml_file}")
    else:
        extract_clashtest_rules(xml_file)
