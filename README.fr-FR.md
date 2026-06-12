# Skill de Synthèse Métaphysique

Un skill pour Codex et AI Agent consacré au BaZi, au Meihua Yishu, au Liuyao, au Feng Shui directionnel et au Tarot.

Ce dépôt n'est pas un simple prompt de divination. Il fournit une méthode réutilisable pour aider un assistant IA à choisir le bon système, formuler un verdict, présenter les preuves, estimer le timing, proposer une action et définir des signes de vérification.

> Usage culturel, réflexif et stratégique uniquement. Ce skill ne remplace pas un avis médical, juridique, financier, psychologique, d'urgence ou de sécurité.

## Requêtes de recherche visées

- skill IA de divination
- skill Codex pour BaZi
- assistant IA pour astrologie chinoise
- lecture BaZi quatre piliers
- calculateur Meihua Yishu
- Yi King présage Meihua
- méthode Liuyao pour IA
- six lignes Najia
- analyse Feng Shui des directions
- Feng Shui bureau poste de travail
- prompt Tarot IA
- tirage tarot carte inversée
- agent IA pour métaphysique chinoise

## Systèmes pris en charge

| Système | Questions adaptées | Fichier |
| --- | --- | --- |
| BaZi / Zi Ping | Structure de vie, cycles décennaux, carrière, richesse, mariage, santé | `references/bazi.md` |
| Meihua Yishu | Présages, horaires, événements soudains, mouvements à court terme | `references/meihua.md` |
| Liuyao / Najia | Contrats, poste, supérieur, salaire, traction produit, résultat concret | `references/liuyao.md` |
| Feng Shui / Direction | Poste de travail, orientation, portes, fenêtres, circulation, visibilité | `references/fengshui.md` |
| Tarot | Dynamique relationnelle, psychologie, choix, tournant symbolique | `references/tarot.md` |

## Fonctions principales

- Sépare le verdict, les preuves, le timing, l'action et les points de vérification.
- Distingue les conclusions fortes des hypothèses faibles.
- Analyse chaque système séparément avant toute synthèse.
- Marque chaque méthode comme `runnable`, `partial` ou `blocked`.
- Sépare les faits calculables du BaZi de leur interprétation.
- Fixe les entrées du Meihua Yishu: heure, nombres et présage externe.
- Impose l'ordre des six lignes Liuyao de bas en haut.
- Lit le Feng Shui par la forme et l'environnement avant les formules directionnelles.
- Fournit un tirage Tarot reproductible avec spread, seed et cartes droites/inversées.
- Inclut un script de calcul structurel pour le Meihua Yishu.
- Inclut un script de tirage Tarot et un contrôle de confidentialité avant publication.
- Définit des limites de sécurité pour les sujets sensibles.

## Installation

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill.git ~/.codex/skills/metaphysics-synthesis
```

Redémarrez Codex ou rechargez les skills si nécessaire.

## Exemples en français

### Exemple BaZi

```text
Analyse ce thème BaZi pour la carrière et la richesse de 2026 à 2036. Sépare la structure natale, la décennie de chance, les déclencheurs annuels, les conclusions fortes et les hypothèses faibles.
```

### Exemple Meihua Yishu

```text
Utilise le Meihua Yishu pour lire si ce lancement de produit peut créer une percée professionnelle visible. La question est apparue le 2026-06-12 à 10:36, avec comme signe externe un manager discutant du planning au nord-ouest.
```

### Exemple Liuyao

```text
Utilise le Liuyao pour juger si ce projet peut devenir la preuve principale d'une promotion. Les six lignes de bas en haut sont 5 / 4 / 25 / 12 / 22 / 17.
```

### Exemple Feng Shui

```text
Analyse mon poste de travail avec la logique des directions Feng Shui. Je fais face au sud-est, mon manager direct est au nord-ouest, le grand responsable est au sud, et un manager transversal est à l'est.
```

### Exemple Tarot

```text
Utilise un tirage de sept cartes de Tarot pour lire uniquement la dynamique relationnelle. Donne la carte centrale, l'obstacle, le tournant, l'action probable et les signes de vérification.
```
