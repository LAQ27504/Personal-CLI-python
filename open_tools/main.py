import typer
import subprocess
from PyInquirer import prompt, print_json, Separator
from rich import print as rprint
import rich.console
import yaml
import os

app = typer.Typer()

HOME_DIRECTORY = os.path.expanduser("~")
MAIN_DIRECTORY = HOME_DIRECTORY + "/.laq_data"
TOOL_DATA = MAIN_DIRECTORY + "/tool_data.yaml"

def add_tool(tool_name: str, link: str):
    with open(f"{TOOL_DATA}", 'r') as f:
        data = yaml.safe_load(f) or {}
    new_data = {tool_name : link}
    if data.get(tool_name):
        return "[red bold]This tool have been added[/red bold]"
    data.update(new_data)
    
    with open(TOOL_DATA, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)
    return "[green bold]Data added successfully[/green bold]"

def get_tool(tool_name : str):
    with open(TOOL_DATA, 'r') as f:
        data = yaml.safe_load(f) or {}
    if len(data) == 0:
        return None
    return data.get(tool_name)

def start_up():
    if not os.path.exists(MAIN_DIRECTORY):
        subprocess.run([f"mkdir {MAIN_DIRECTORY}"], shell= True)
    if not os.path.exists(TOOL_DATA):
        with open(TOOL_DATA, 'w') as f:
            yaml.dump({}, f, default_flow_style=False)


@app.command("open")
def open_tool(tool_name : str = typer.Argument(None, help="The tool name")):
    tool_name = tool_name.capitalize()
    if not tool_name:
        rprint("[red bold]Please insert the tool name!![/red bold]")
    response = get_tool(tool_name=tool_name)
    if not response:
        rprint("[red bold]There are no exist tool[/red bold]")
        return
    subprocess.run([f"xdg-open '{response}'"], shell=True)
    rprint(f"[green bold]Open {tool_name} ...[/green bold]")

@app.command("add")
def add(
    tool_name : str = typer.Argument(None, help="The tool name"),
    url_link : str = typer.Argument(None, help="The link of the tools")
    ):
    tool_name = tool_name.capitalize()
    if not tool_name or not url_link:
        rprint("[red bold]Please insert the tool name or the link!![/red bold]")
        return
    response = add_tool(tool_name=tool_name, link=url_link)
    rprint(response)

@app.command("list")
def list_tool(
    list_all : bool = typer.Option(False, "--list_all", "-la",help="Option to list all")
    ):
    with open(f"{TOOL_DATA}", 'r') as f:
        data = yaml.safe_load(f) or {}
    if len(data) == 0:
        rprint("[red bold]There are no tool added !![/red bold]")
        return 
    rprint('[yellow]Listing all the tools:[/yellow]')
    if list_all:
        for tool in data:
            rprint(f"[blue]{tool}: {data[tool]}[/blue]")
        return
    for tool in data:
        rprint(f"[blue]{tool}[/blue]")
    
    
    
if __name__ == "__main__":
    start_up()
    app()