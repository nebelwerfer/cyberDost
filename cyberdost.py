from rich import print
import yaml

def main():
    with open("config.yaml","r") as f:
        cfg=yaml.safe_load(f)
    print("[bold green]CyberDost X v0.1 Alpha[/bold green]")
    print(f"Backend: {cfg['backend']}")
    print(f"Workspace: {cfg['workspace']}")
    while True:
        try:
            cmd=input("Mission> ")
        except (EOFError, KeyboardInterrupt):
            break
        if cmd.lower() in ("exit","quit"):
            break
        print(f"Received mission: {cmd}")
        print("Planner and executor are not implemented yet.")

if __name__=="__main__":
    main()
