import click
import requests

BASE_URL = 'https://api.publicapis.org'


@click.group()
def apis():
    """A CLI wrapper for the API of Public APIs."""


@click.option('-t', '--title', help='Name of API (matches via substring - i.e. "at" would return "cat" and "atlas".')
@click.option('-c', '--category', help='Return only APIs from this category')
@click.option('-a', '--no-auth', is_flag=True, help='Filter out APIs with required auth')
@apis.command()
def entries(title: str, category: str, no_auth: bool):
    """List all cataloged APIs."""


@click.option('-t', '--title', help='Name of API (matches via substring - i.e. "at" would return "cat" and "atlas".')
@click.option('-c', '--category', help='Return only APIs from this category')
@click.option('-a', '--no-auth', is_flag=True, help='Filter out APIs with required auth')
@apis.command()
def random(title: str, category: str, no_auth: bool):
    """Get a random API."""


@apis.command()
def categories():
    """List all categories."""
    response = requests.get(url=f'{BASE_URL}/categories')
    if response.status_code is 200:
        print('\n'.join(response.json()))
    else:
        print(f'Could not get the categories: {response.text}')


if __name__ == '__main__':
    apis(prog_name='apis')
