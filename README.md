<h1 align="center">
  <a href="https://github.com/morabdiego">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://readme-typing-svg.herokuapp.com?font=Montserrat&weight=700&size=50&pause=1000&color=FFFFFF&center=true&vCenter=true&random=false&width=600&lines=Diego+Mora">
      <source media="(prefers-color-scheme: light)" srcset="https://readme-typing-svg.herokuapp.com?font=Montserrat&weight=700&size=50&pause=1000&color=000000&center=true&vCenter=true&random=false&width=600&lines=Diego+Mora">
      <img src="https://readme-typing-svg.herokuapp.com?font=Montserrat&weight=700&size=50&pause=1000&color=000000&center=true&vCenter=true&random=false&width=600&lines=Diego+Mora" alt="Diego Mora" />
    </picture>
  </a>
</h1>

<p align="center">
  <b>Economist (UBA) · Fiscal Policy & Data Analyst · Socioeconomic Researcher</b>
</p>

<p align="center">
  <a href="https://morabdiego.github.io/morabdiego/" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Portfolio%20%26%20Interactive%20CV%20(ES%20/%20EN)&logo=githubpages&label=&color=1B4332&logoColor=white&style=for-the-badge" height="35" alt="Portfolio & CV" />
  </a>
</p>

<br />

- **Economist & Data Analyst** specialized in applied econometrics, tax analytics, and nationwide socioeconomic research (B.A. in Economics, **UBA** · Diploma in Public Sector Data Analysis, **IPAP–UTN**).
- **Economic Advisor at ARBA** *(Buenos Aires Province Tax Agency)*: subnational revenue forecasting (*SARIMAX*, cointegration), fiscal intelligence algorithms, large-scale ETL pipelines, and policy impact evaluation (*Difference-in-Differences*).
- **Socioeconomic Research Coordinator & Data Lead at [Observatorio Villero](https://observatoriovillero.lapoderosa.org.ar/)**: complex sampling design, nationwide household surveys, automated field data auditing (*KoboToolbox REST API & Telegram bots*), and data storytelling.

<br />

## Open-Source Packages & Datasets

| Project | Description | Package / Source |
| :--- | :--- | :--- |
| **[pyindec](https://github.com/morabdiego/pyindec)** | Python client for Argentina's National Statistics Institute (**INDEC**) PostgREST API with fluent `QueryBuilder`, column normalization, and automatic composite-key pagination across 19 official endpoints (*IPC, EMAE, EPH, Canastas, Comex, etc.*). | [![PyPI](https://img.shields.io/pypi/v/pyindec?color=1B4332&label=PyPI&logo=pypi&logoColor=white)](https://pypi.org/project/pyindec/) |
| **[pyBCRAdata](https://github.com/morabdiego/pybcradata)** | Python library for fetching monetary, exchange rate, and financial time series from the Central Bank of Argentina (**BCRA**) API. | [![PyPI](https://img.shields.io/pypi/v/pybcradata?color=1B4332&label=PyPI&logo=pypi&logoColor=white)](https://pypi.org/project/pybcradata/) |
| **[xlsform-to-registro](https://github.com/morabdiego/xlsform-to-registro)** | CLI & Python library that converts standard **XLSForm** surveys (*KoboToolbox, ODK, Enketo*) into publication-ready institutional Excel Data Dictionaries (*Diseños de Registro*), translating `relevant` skip logic into target universes and extracting large catalogues. | [![PyPI](https://img.shields.io/pypi/v/xlsform-to-registro?color=1B4332&label=PyPI&logo=pypi&logoColor=white)](https://pypi.org/project/xlsform-to-registro/) |
| **[kobo-api-v2](https://github.com/morabdiego/kobo-api-v2)** | Lightweight synchronous Python client for the **KoboToolbox API v2** featuring one-call Excel/CSV exports, reusable export settings, and automated polling. | [![PyPI](https://img.shields.io/pypi/v/kobo-api-v2?color=1B4332&label=PyPI&logo=pypi&logoColor=white)](https://pypi.org/project/kobo-api-v2/) |
| **[Observadata](https://github.com/ObservatorioVillero/observadata)** | Open-science repository of anonymized socioeconomic microdata and FAIR-standard metadata backed by Zenodo DOIs. | [![GitHub](https://img.shields.io/badge/GitHub-Repo-181717?logo=github&logoColor=white)](https://github.com/ObservatorioVillero/observadata) |

```bash
# Macroeconomic & Official Statistics APIs (Argentina)
pip install pyindec pybcradata

# Survey Engineering & KoboToolbox Workflows
pip install xlsform-to-registro kobo-api-v2
