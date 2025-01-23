import typer

module1_commands = typer.Typer()
@module1_commands.command()
def xinchao():
    print("Xin chao the gioi")