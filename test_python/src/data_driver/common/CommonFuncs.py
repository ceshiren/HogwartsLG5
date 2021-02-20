import os

import yaml


class Common_Funcs:
    path = os.path.dirname(__file__).strip("common").__add__("datas/data.yaml")

    def get_data(self):
        print(self.path)
        with open(self.path, encoding="UTF-8") as f:
            data = yaml.safe_load(f)
            add_data = data['people']
            add_ids = data['myids']
            return [add_data, add_ids]


if __name__ == "__main__":
    cf = Common_Funcs()
    gt = cf.get_data()
    print(gt)