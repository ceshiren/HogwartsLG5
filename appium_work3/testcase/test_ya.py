import yaml

with open('main_page.yaml', encoding='utf-8') as f:
    step_yaml = yaml.safe_load(f)
    print(f'yaml数据：{step_yaml["goto_market"]}')