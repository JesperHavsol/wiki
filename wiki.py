import click
import wikipedia

@click.command()
@click.option('--topic',prompt="The wikipage we want to scrape",
            help="The page we want to scrape")
def scrape(topic="Linux", sentences=1):
    res = wikipedia.summary(topic, sentences)
    click.echo(res)

if __name__ == '__main__':
    scrape()
