# Sport ESI 🏋️‍♂️

Un module Odoo pour la gestion des séances sportives à l'ESI (École Supérieure d'Informatique).

## Description 📝

**Sport ESI** est un module Odoo conçu pour simplifier la gestion des séances d'entraînement dans la salle de sport de l'école. Il permet d'organiser efficacement l'affectation des créneaux horaires aux sportifs.

## Fonctionnalités 🚀

- **Gestion des Sportifs**
  - Suivi des informations personnelles (Matricule, Nom)
  - Catégorisation des sportifs
  - Interface intuitive de gestion

- **Gestion des Séances**
  - Planification des séances d'entraînement
  - Attribution des créneaux horaires
  - Suivi des disponibilités

- **Intégration Calendrier**
  - Synchronisation avec Odoo Calendar
  - Vue calendrier interactive
  - Gestion visuelle des emplois du temps

## Prérequis 📋

- Odoo (version compatible)
- Modules requis :
  - Module Base Odoo
  - Module Calendar Odoo

## Installation 💻

1. **Copie des fichiers**
   ```bash
   # Copiez le dossier du module dans le répertoire addons d'Odoo
   cp -r sport_esi /chemin/vers/odoo/addons/
   ```

2. **Mise à jour de la base de données**
   ```bash
   # Redémarrez le serveur et mettez à jour le module
   odoo -u sport_esi --db votre_base_de_donnees
   ```

## Configuration ⚙️

1. Activez le module depuis l'interface Odoo
2. Configurez les paramètres initiaux dans le menu Settings
3. Commencez à créer vos premiers enregistrements

## Utilisation 📱

Le module offre plusieurs vues pour une gestion optimale :
- Vue Liste pour un aperçu global
- Vue Formulaire pour la gestion détaillée
- Vue Recherche pour retrouver rapidement les informations
- Vue Calendrier pour la planification

## Dépendances 🔗

- Module Base Odoo
- Module Calendar Odoo

## Auteur 👤

- **Achraf Abdelkebir** 

## Support 💬

Pour toute question ou problème :
- Créez une issue sur ce repository
