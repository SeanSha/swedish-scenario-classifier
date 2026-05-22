# Lecture Alignment

The dataset was updated to match the vocabulary and themes from the Swedish beginner lecture PDFs.

## Extracted Lecture Themes

| Lecture theme | Examples from lectures | Dataset label |
| --- | --- | --- |
| Introductions and social phrases | `Hej`, `Vad heter du?`, `Jag heter...`, `Var bor du?`, `Jag mår bra`, `Förlåt?`, `Jag förstår inte` | `social_intro` |
| Food, fika, and shops | `i affären`, `mat`, `kaffe`, `vatten`, `tomat`, `äpple`, `päron`, `kanelbulle`, `semla`, `kostar` | `food_shop` |
| Family and school | `barn`, `mamma`, `pappa`, `dotter`, `son`, `lärare`, `i skolan` | `family_school` |
| Health and care places | `apoteket`, `sjukhuset`, `sköterska`, `mår`, `sjuk`, `ont` | `health_places` |
| Transport and directions | `buss`, `tåg`, `tunnelbanan`, `bil`, `cykla`, `till höger`, `till vänster` | `transport` |
| Home and prepositions | `i rummet`, `i lägenheten`, `i sängen`, `på bordet`, `under stolen`, `bredvid`, `kök`, `vägg` | `home_places` |
| Introductions and clarification | `Hej`, `Vad heter du?`, `Jag heter...`, `Förlåt?`, `Jag förstår inte` | `social_intro` |

## Design Decision

The original daily-life idea was kept, but the labels were renamed to match the lecture themes more directly. Most examples are short pre-A1/A1-minus sentences using simple structures:

- `Jag är...`
- `Jag vill...`
- `Jag behöver...`
- `Var är...?`
- `När går...?`
- `Kan jag...?`

The model uses only the Swedish `text` column. English, Chinese, and `lecture_theme` are metadata for review and explanation.
