import subprocess

# script_dir = Path(__file__).resolve().parent
# os.chdir(script_dir)

def GenerateTest(test):
    with open("src/data/solve.inp", "wb") as finp:
        subprocess.run(["src/generator/generator.exe", str(test)], stdout=finp, check=True)

def RunPython():
    with open("src/data/solve.out", "wb") as out, open("src/data/solve.ans", "wb") as ans:
        with open("src/data/solve.inp", "rb") as input:
            subprocess.run(["python", "src/bin/brute_force.py"], stdin=input, stdout=ans)
        with open("src/data/solve.inp", "rb") as input:
            subprocess.run(["python", "src/bin/solution.py"], stdin=input, stdout=out)

def RunExe():
    with open("src/data/solve.out", "wb") as out, open("src/data/solve.ans", "wb") as ans:
        with open("src/data/solve.inp", "rb") as input:
            subprocess.run(["src/bin/brute_force.exe"], stdin=input, stdout=ans)
        with open("src/data/solve.inp", "rb") as input:
            subprocess.run(["src/bin/solution.exe"], stdin=input, stdout=out)
    

def RunSolution(lang):
    if lang == "python":
        RunPython()
    else:
        RunExe()
        

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
    GenerateTest(36)
    
    RunSolution("c++")