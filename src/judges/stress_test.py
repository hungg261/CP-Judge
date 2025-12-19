import subprocess
import shutil

def CompileGenerator():
    subprocess.run(["g++", "src/generator/generator.cpp", "-o", "src/bin/generator.exe"])

def CompileSolution(conf, lang):
    if lang == "python":
        shutil.copyfile(f"{conf[lang][0]}/brute_force.py", f"src/bin/brute_force.py")
        shutil.copyfile(f"{conf[lang][0]}/solution.py", f"src/bin/solution.py")
        return
    
    subprocess.run(["g++", f"{conf[lang][0]}/brute_force{conf[lang][1]}",
                    "-o", f"src/bin/brute_force"],
                   check=True)
    
    subprocess.run(["g++", f"{conf[lang][0]}/solution{conf[lang][1]}",
                    "-o", f"src/bin/solution"],
                   check=True)

if __name__ == "__main__":
    import json

    def load_json(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"{path} not found")
        except json.JSONDecodeError:
            print(f"{path} is not valid JSON")
        return None
    config = load_json("src/config.json")
    
    print(config)
    CompileGenerator()
    CompileSolution(config["config"]["language"], "c++")