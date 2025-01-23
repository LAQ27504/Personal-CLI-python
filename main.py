import typer
import subprocess
from PyInquirer import prompt, print_json, Separator
from rich import print as rprint

app = typer.Typer()

def get_delivery_options(answers):
    options = ['bike', 'car', 'truck']
    if answers['size'] == 'jumbo':
        options.append('helicopter')
    return options

@app.command("create-folder")
def sample_func():
    module_list_question = questions = [
    {
        'type': 'expand',
        'message': 'Conflict on `file.js`: ',
        'name': 'overwrite',
        'default': 'a',
        'choices': [
            {
                'key': 'y',
                'name': 'Overwrite',
                'value': 'overwrite'
            },
            {
                'key': 'a',
                'name': 'Overwrite this one and all next',
                'value': 'overwrite_all'
            },
            {
                'key': 'd',
                'name': 'Show diff',
                'value': 'diff'
            },
            Separator(),
            {
                'key': 'x',
                'name': 'Abort',
                'value': 'abort'
            }
        ]
    }
]

    username = prompt(module_list_question)
    print(username)
    # rprint("[yellow]=============================================[yello]")
    # rprint("[green bold]Enter folder name :[green bold]")
    # folder_name = input()


    # subprocess.run(f"mkdir {folder_name}_created_by_{username['username']}", shell=True)

@app.command("hello")
def sample_func():
    rprint("[red bold]Hello[/red bold] [yellow]World[yello]")



if __name__ == "__main__":
    app()    