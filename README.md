Portfolio Data Platform

En cours de construction

Ce dépôt présente ma plateforme de Data Engineering personnelle, conçue pour collecter, transformer, stocker et visualiser des données issues de diverses API (Strava, etc.) jusqu’à un tableau de bord Streamlit.

Structure du projet

portfolio-data-platform/
├── infra/           # Configuration Docker Compose 
├── dags/            # Pipelines Airflow (ETL/ELT)
├── scripts/         # Jobs Python standalone (export, nettoyage...)
├── data/            # Data Lake (bronze, silver, gold)
├── app/             # Application Streamlit (portfolio & dashboards)
├── projects/        # Proof-of-concept isolés (ex: Strava)
├── docs/            # Documentation, diagrammes, captures d’écran
└── .github/         # CI/CD workflows (déploiement VPS)

Premiers pas
	1.	Copier le fichier d’environnement et renseigner les variables :

cp .env.example .env


	2.	Démarrer les services en local via Docker Compose :

docker-compose up -d


	3.	Accéder aux interfaces :
	•	Airflow UI : http://localhost:8080
	•	Streamlit : http://localhost:8501

Avenir
	•	Intégration complète de la collecte Strava et autres API
	•	Orchestration des pipelines ETL avec Airflow
	•	Stockage en bronze/silver/gold (Delta Lake / Parquet)
	•	Dashboard interactif Streamlit en production sur VPS

Merci de votre visite !