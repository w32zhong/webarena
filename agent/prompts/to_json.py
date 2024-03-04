import glob
import importlib
import json
import os

# set the URLs of each website, we use the demo sites as an example
os.environ[
    "SHOPPING"
] = "http://ec2-3-131-244-37.us-east-2.compute.amazonaws.com:7770"
os.environ[
    "SHOPPING_ADMIN"
] = "http://ec2-3-131-244-37.us-east-2.compute.amazonaws.com:7780/admin"
os.environ[
    "REDDIT"
] = "http://ec2-3-131-244-37.us-east-2.compute.amazonaws.com:9999"
os.environ[
    "GITLAB"
] = "http://ec2-3-131-244-37.us-east-2.compute.amazonaws.com:8023"
os.environ[
    "MAP"
] = "http://ec2-3-131-244-37.us-east-2.compute.amazonaws.com:3000"
os.environ[
    "WIKIPEDIA"
] = "http://ec2-3-131-244-37.us-east-2.compute.amazonaws.com:8888/wikipedia_en_all_maxi_2022-05/A/User:The_other_Kiwix_guy/Landing"
os.environ[
    "HOMEPAGE"
] = "PASS"  # The home page is not currently hosted in the demo site
print("Done setting up URLs")
from browser_env.env_config import *


# use the current directory as the root
def run() -> None:
    """Convert all python files in agent/prompts to json files in agent/prompts/jsons

    Python files are easiser to edit
    """
    for p_file in glob.glob(f"agent/prompts/raw/*.py"):
        # import the file as a module
        base_name = os.path.basename(p_file).replace(".py", "")
        module = importlib.import_module(f"agent.prompts.raw.{base_name}")
        prompt = module.prompt
        # save the prompt as a json file
        os.makedirs("agent/prompts/jsons", exist_ok=True)
        with open(f"agent/prompts/jsons/{base_name}.json", "w+") as f:
            json.dump(prompt, f, indent=2)
    print(f"Done convert python files to json")


if __name__ == "__main__":
    run()
