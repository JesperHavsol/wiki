
from mylib.bot import scrape
from wiki import scrape_cli
from click.testing import CliRunner

def test_scrape():
    assert "Microsoft" in scrape("Microsoft")

def test_scrape_cli():
    runner = CliRunner()
    res = runner.invoke(scrape_cli, ['--topic', 'Microsoft'])
    assert res.exit_code == 0
    assert 'Microsoft' in res.output 
