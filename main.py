from bs4 import BeautifulSoup
import requests

# URL- ul paginii principale cu joburi
url = 'https://totalsoft.applytojob.com/apply/' 

# Face un request la pagina si returneaza o lista cu titlurile joburilor
def get_jobs(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() # Opreste daca serverul a dat o eroare
    except requests.RequestException as e:
        print(f'Eroare la accesarea {url}: {e}')
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all('h4', class_='list-group-item-heading')
    return [t.text.strip() for t in titles]

# Scrie o lista de joburi intr-un fisier text, fiecare pe un rand nou
def write_file(jobs, file_name='jobs.txt'):
    with open(file_name, 'w', encoding='utf-8') as file:
        for job in jobs:
            file.write(job + '\n')


jobs = get_jobs(url)

if jobs:
    write_file(jobs)
    print(f'S-au scris {len(jobs)} joburi in fisierul jobs.txt')
else:
    print('Nu s-au gasit joburi.')