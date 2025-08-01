# 🍽️ Scraping de Recettes - CuisineAZ avec Scrapy

Ce projet utilise **Scrapy**, un framework Python de scraping, pour extraire des informations structurées depuis des pages de recettes du site [cuisineaz.com](https://www.cuisineaz.com).

## 📁 Structure du projet

```
recettes_scrapy/
├── recettes_scrapy/
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders/
│       └── recettes_spider.py
├── recettes.json
├── scrapy.cfg
└── README.md
```

## 🧠 Fonctionnalités du spider

Le spider `recettes_spider.py` extrait pour chaque recette :
- `titre` : le titre de la recette
- `ingredients` : la liste des ingrédients
- `temps_preparation` : les temps associés à la recette (préparation, cuisson, etc.)
- `etapes` : les étapes de la recette

## ▶️ Lancement du spider

### 1. Installation de Scrapy (si ce n’est pas déjà fait) :
```bash
pip install scrapy
```

### 2. Lancer le spider :
Depuis la racine du projet, exécute :
```bash
scrapy crawl recettes_spider -o recettes.json
```

Cela va :
- Lancer le spider
- Parcourir les 4 URLs définies dans `start_urls`
- Enregistrer les données extraites dans le fichier `recettes.json`

## ⚙️ Fichier de configuration : `settings.py`

Le format de sortie a été défini pour générer du **JSON encodé en UTF-8**, via :

```python
FEEDS = {
    'recettes.json': {
        'format': 'json',
        'encoding': 'utf-8',
        'overwrite': True
    }
}
```

## 📌 Sélecteurs utilisés

Les sélecteurs CSS ont été choisis après inspection manuelle des pages HTML :
- Titre : `.recipe-title`
- Ingrédients : `.ingredient_label`
- Temps : `.recipe_time_information`
- Étapes : `.preparation_step_title_container > h3.recipe_section_h3`

## ❗ À savoir

- Le spider ne suit pas les liens : il scrape uniquement les pages listées dans `start_urls`.
- Le projet peut être facilement étendu pour inclure de la pagination ou du suivi de liens vers d'autres recettes.

## 📄 Auteurs

Projet réalisé par : [Ton nom ou pseudo]  
Date : Août 2025
