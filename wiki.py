import click
from mylib.bot import scrape

@click.command()
@click.option('--topic',prompt="The wikipage we want to scrape",
            help="The page we want to scrape")
def scrape_cli(topic="Linux"):
    res = scrape(topic, sentences=1)
    click.echo(click.style(f"{res}",bg='blue',fg="red"))

if __name__ == '__main__':
    scrape_cli()
