"""
Datos estructurados del Portfolio y CV de Diego J. Mora Benitez.
Podés editar o agregar ítems en las listas de abajo (EXPERIENCE, EDUCATION,
TRAINING, SKILLS, PUBLICATIONS) y se reflejarán automáticamente en la web.
"""

PROFILE = {
    "name": "Diego J. Mora Benitez",
    "handle": "@morabdiego",
    "role_es": "Economista · Analista de Datos y Política Fiscal",
    "role_en": "Economist · Data & Fiscal Policy Analyst",
    "tagline_es": "Econometría aplicada, analítica fiscal e investigación socioeconómica.",
    "tagline_en": "Applied econometrics, tax analytics, and socioeconomic research.",
    "bio_p1_es": (
        "Economista (UBA) especializado en econometría aplicada (SARIMAX, diferencias en diferencias, "
        "cointegración), analítica fiscal e investigación socioeconómica. Actualmente asesoro a la "
        "Dirección Ejecutiva de ARBA en estimación de recaudación subnacional y fiscalización basada en datos; "
        "previamente dirigí relevamientos federales a hogares de barrios populares."
    ),
    "bio_p1_en": (
        "Economist (University of Buenos Aires) specialized in applied econometrics (SARIMAX, "
        "difference-in-differences, cointegration), tax analytics, and socioeconomic research. I currently "
        "advise the Executive Directorate of ARBA, the Buenos Aires Province tax agency, on subnational "
        "revenue forecasting and data-driven tax enforcement; previously I led nationwide household surveys "
        "in low-income neighborhoods."
    ),
    "bio_p2_es": (
        "Trabajo el ciclo completo del dato —captura en campo, pipelines ETL reproducibles, modelado "
        "econométrico, ciencia abierta (Observadata) y tableros para la toma de decisiones— utilizando "
        "Python, Polars, R, SQL y Git."
    ),
    "bio_p2_en": (
        "I work across the full data cycle —field collection, reproducible ETL pipelines, econometric "
        "modeling, open science (Observadata), and decision-support dashboards— using Python, Polars, "
        "R, SQL, and Git."
    ),
}

HIGHLIGHTS = [
    {
        "metric": "< 5% MAPE",
        "label_es": "Estimación e Inteligencia Fiscal",
        "label_en": "Revenue Forecasting & Tax Analytics",
        "detail_es": "Modelos SARIMAX y cointegración en ARBA · $500M detectados en fiscalización",
        "detail_en": "SARIMAX & cointegration models at ARBA · ARS 500M identified in audits",
    },
    {
        "metric": "+6 Años",
        "metric_en": "6+ Years",
        "label_es": "Investigación Federal y Datos",
        "label_en": "Nationwide Research & Data",
        "detail_es": "Relevamientos en +20 provincias, pipelines ETL y ciencia abierta (Observadata)",
        "detail_en": "Surveys across 20+ provinces, ETL pipelines & open science (Observadata)",
    },
    {
        "metric": "Full-Cycle",
        "label_es": "Econometría e Ingeniería de Datos",
        "label_en": "Econometrics & Data Engineering",
        "detail_es": "Python · Polars · R · SQL · Series de tiempo · Diferencias en diferencias",
        "detail_en": "Python · Polars · R · SQL · Time series · Difference-in-differences",
    },
]

EXPERIENCE = [
    {
        "role_es": "Economista Asesor",
        "role_en": "Economist Advisor",
        "organization_es": "ARBA — Agencia de Recaudación de la Provincia de Buenos Aires",
        "organization_en": "ARBA — Buenos Aires Province Tax Agency",
        "location_es": "La Plata · Dirección Ejecutiva y Depto. de Análisis Fiscal Tributario (Gerencia de Inteligencia Fiscal)",
        "location_en": "La Plata · Executive Directorate and Tax Analysis Dept. (Fiscal Intelligence Division)",
        "period_es": "Oct. 2025 – Presente",
        "period_en": "Oct. 2025 – Present",
        "current": True,
        "icon": "landmark",
        "bullets_es": [
            "Diseñé e implementé en Python modelos econométricos y predictivos (SARIMAX y cointegración) para estimar la recaudación de Ingresos Brutos (IIBB) en todas las jurisdicciones, a partir de datos de COMARB, con MAPE inferior al 5% en todos los casos.",
            "Automaticé la definición del modelo: el sistema prueba especificaciones (log-log, ratios, variaciones interanuales, dummies transitorias y de nivel) y las refina en 24 iteraciones sucesivas hasta cumplir el criterio de MAPE.",
            "Desarrollé algoritmos de inteligencia fiscal y cruces masivos de bases sobre cientos de miles de contribuyentes para auditorías automatizadas y fiscalización individualizada de los sectores agropecuario e industrial, identificando $500 millones en impuesto omitido.",
            "Construí pipelines ETL estandarizados que mejoraron la velocidad de procesamiento y la reproducibilidad sobre millones de registros tributarios.",
            "Formulé el esquema cuantitativo y de incentivos del programa de cumplimiento fiscal ARBA-Puntos y evalué su impacto recaudatorio y sobre el comportamiento de los contribuyentes mediante diferencias en diferencias.",
        ],
        "bullets_en": [
            "Designed and implemented in Python econometric and predictive models (SARIMAX and cointegration) to forecast Gross Income Tax (IIBB) revenue across all jurisdictions using COMARB data, achieving MAPE below 5% in every case.",
            "Automated model specification: the system tests specifications (log-log, ratios, year-over-year changes, transitory and level dummies) and refines them over 24 successive iterations until the MAPE criterion is met.",
            "Developed fiscal intelligence algorithms and large-scale database cross-matching over hundreds of thousands of taxpayers for automated audits and targeted enforcement in the agricultural and industrial sectors, identifying ARS 500 million in unpaid tax.",
            "Built standardized ETL pipelines that improved processing speed and reproducibility across millions of tax records.",
            "Designed the quantitative and incentive framework of the ARBA-Puntos tax compliance program and assessed its revenue impact and effect on taxpayer behavior using difference-in-differences.",
        ],
        "tags_es": [
            "Python",
            "Polars",
            "SARIMAX",
            "Cointegración",
            "Diferencias en Diferencias",
            "Pipelines ETL",
            "Inteligencia Fiscal",
        ],
        "tags_en": [
            "Python",
            "Polars",
            "SARIMAX",
            "Cointegration",
            "Difference-in-Differences",
            "ETL Pipelines",
            "Fiscal Intelligence",
        ],
    },
    {
        "role_es": "Coordinador de Estudios Socioeconómicos y Data Lead",
        "role_en": "Socioeconomic Research Coordinator & Data Lead",
        "organization_es": "A.C. La Poderosa — Observatorio Villero",
        "organization_en": "A.C. La Poderosa — Socioeconomic Observatory",
        "location_es": "Ciudad de Buenos Aires, Argentina",
        "location_en": "Buenos Aires, Argentina",
        "period_es": "Ene. 2020 – Presente",
        "period_en": "Jan. 2020 – Present",
        "current": True,
        "icon": "bar-chart-3",
        "bullets_es": [
            "Dirección de investigaciones federales en convenio con UNICEF, ACIJ, IIGG-UBA, Fundación Rosa Luxemburgo, Friedrich Ebert y SAGE Foundation: diseño metodológico (muestreo, marcos conceptuales, instrumentos) y ejecución de relevamientos a escala nacional.",
            "Estudios principales: Endeudamiento en barrios populares (2026: muestreo por cuotas en 12 barrios de 7 provincias a 643 personas sobre circuitos financieros informales y costos no monetarios) y Uso del tiempo y trabajo comunitario (2025–2026: 1.096 hogares y 1.241 personas en 71 barrios de 14 provincias; adapté el clasificador de la ENUT-INDEC para medir la triple jornada, soporte empírico del proyecto de Ley de Salario para Cocineras Comunitarias presentado en el Congreso).",
            "Otros relevamientos federales: Condiciones de vida (2024–2025: 1.485 hogares y 5.024 personas en 9 barrios de 6 provincias junto a ACIJ e IIGG-UBA; y 2022: 1.222 viviendas en 23 barrios de 16 provincias junto a Fundación Rosa Luxemburgo y El Gato y La Caja); Gestión menstrual (2021: 2.478 hogares y 3.598 personas en 67 barrios de 22 provincias); Pobreza infantil y redes comunitarias (2022–2023: estudio cualitativo federal con UNICEF Argentina).",
            "Infraestructura de datos y automatización: diseñé la captura y el control con XLSForm/KoboToolbox y desarrollé librerías en Python sobre la API REST de Kobo para ingesta, validación de coherencia y limpieza (ETL). Programé bots de Telegram que auditan el avance territorial en tiempo real y aplican reglas de consistencia a las cargas.",
            "Ciencia abierta: creé y administro Observadata, repositorio de datos abiertos del Observatorio, con microdatos anonimizados, metadatos estructurados y publicación en GitHub/Zenodo con DOI y licencias abiertas.",
            "Divulgación: coordiné los contenidos y la arquitectura del sitio oficial del Observatorio (observatoriovillero.lapoderosa.org.ar), diseñé visualizaciones accesibles y lo represento técnicamente en medios, conferencias de prensa y ámbitos académicos.",
        ],
        "bullets_en": [
            "Led nationwide research projects in partnership with UNICEF, ACIJ, IIGG-UBA, Rosa Luxemburg Foundation, Friedrich Ebert Foundation, and SAGE Foundation: methodological design (sampling, conceptual frameworks, instruments) and fieldwork at national scale.",
            "Main studies: Household debt in low-income neighborhoods (2026: quota sampling across 12 neighborhoods in 7 provinces reaching 643 people on informal credit circuits and non-monetary costs) and Time use and community work (2025–2026: 1,096 households and 1,241 people in 71 neighborhoods across 14 provinces; adapted the INDEC ENUT classifier to measure the triple workday, providing the empirical basis for the Community Cooks' Wage Bill submitted to the Argentine Congress).",
            "Other nationwide studies: Living conditions (2024–2025: 1,485 households and 5,024 people in 9 neighborhoods across 6 provinces with ACIJ and IIGG-UBA; and 2022: 1,222 dwellings in 23 neighborhoods across 16 provinces with Rosa Luxemburg Foundation and El Gato y La Caja); Menstrual health management (2021: 2,478 households and 3,598 people in 67 neighborhoods across 22 provinces); Child poverty and community networks (2022–2023: nationwide qualitative study with UNICEF Argentina).",
            "Data infrastructure and automation: designed data capture and quality control with XLSForm/KoboToolbox and built Python libraries on the Kobo REST API for ingestion, consistency validation, and cleaning (ETL). Developed Telegram bots that monitor fieldwork progress in real time and apply consistency rules to submissions.",
            "Open science: created and maintain Observadata, the Observatory's open data repository, with anonymized microdata, structured metadata, and publication on GitHub/Zenodo with DOIs and open licenses.",
            "Outreach: coordinated the content and architecture of the Observatory's official website (observatoriovillero.lapoderosa.org.ar), designed accessible data visualizations, and serve as its technical spokesperson in media, press conferences, and academic forums.",
        ],
        "tags_es": [
            "Python",
            "KoboToolbox API",
            "Telegram Bots",
            "Muestreo",
            "Observadata (FAIR / DOI)",
            "Visualización",
        ],
        "tags_en": [
            "Python",
            "KoboToolbox API",
            "Telegram Bots",
            "Survey Sampling",
            "Observadata (FAIR / DOI)",
            "Visualization",
        ],
    },
    {
        "role_es": "Columnista Especialista en Economía y Datos",
        "role_en": "Economics and Data Columnist",
        "organization_es": "La Ley de la Selva — C5N",
        "organization_en": "La Ley de la Selva — C5N (TV)",
        "location_es": "Ciudad de Buenos Aires, Argentina",
        "location_en": "Buenos Aires, Argentina",
        "period_es": "May. – Sep. 2024",
        "period_en": "May – Sep. 2024",
        "current": False,
        "icon": "tv",
        "bullets_es": [
            "Convertí bases complejas (inflación, actividad, ingresos, mercado de trabajo) en segmentos informativos en vivo, con gráficos estáticos y dinámicos para televisión, sosteniendo el rigor estadístico junto al equipo de producción.",
        ],
        "bullets_en": [
            "Turned complex datasets (inflation, economic activity, income, labor market) into live TV segments with static and dynamic charts, maintaining statistical rigor in coordination with the production team.",
        ],
        "tags_es": ["Data Storytelling", "Visualización", "Divulgación", "Medios", "Economía"],
        "tags_en": ["Data Storytelling", "Visualization", "Outreach", "Broadcast Media", "Economics"],
    },
    {
        "role_es": "Coordinador Regional",
        "role_en": "Regional Coordinator",
        "organization_es": "RENABAP — Registro Nacional de Barrios Populares",
        "organization_en": "RENABAP — National Registry of Low-Income Neighborhoods",
        "location_es": "Ministerio de Desarrollo Social",
        "location_en": "Ministry of Social Development",
        "period_es": "May. – Dic. 2023",
        "period_en": "May – Dec. 2023",
        "current": False,
        "icon": "compass",
        "bullets_es": [
            "Coordiné la logística y ejecución del relevamiento en territorio: cronogramas, metas de cobertura y supervisión de cuadrillas, con rendición de avance a autoridades del Ministerio.",
            "Seleccioné, capacité y acompañé a más de 30 relevadores, manteniendo controles cruzados de consistencia de datos en campo.",
        ],
        "bullets_en": [
            "Coordinated fieldwork logistics and execution: schedules, coverage targets, and crew supervision, reporting progress to Ministry authorities.",
            "Recruited, trained, and supervised 30+ field surveyors, maintaining cross-checks of data consistency in the field.",
        ],
        "tags_es": ["Gestión Territorial", "RENABAP", "Auditoría de Campo", "Liderazgo"],
        "tags_en": ["Fieldwork Logistics", "RENABAP", "Field Data Auditing", "Leadership"],
    },
]

EDUCATION = [
    {
        "degree_es": "Licenciatura en Economía",
        "degree_en": "Bachelor’s Degree (Licenciatura) in Economics",
        "institution": "Universidad de Buenos Aires (UBA)",
        "faculty_es": "Facultad de Ciencias Económicas",
        "faculty_en": "School of Economics",
        "location_es": "Ciudad de Buenos Aires, Argentina",
        "location_en": "Buenos Aires, Argentina",
        "date_es": "Sept. 2023",
        "date_en": "Sept. 2023",
        "description_es": (
            "Formación integral en teoría económica, econometría aplicada, series de tiempo, "
            "estadística, desarrollo económico y evaluación de políticas públicas y fiscales."
        ),
        "description_en": (
            "Comprehensive training in economic theory, applied econometrics, time series, "
            "statistics, economic development, and public & fiscal policy evaluation."
        ),
        "badge_es": "Grado Universitario",
        "badge_en": "University Degree",
    },
    {
        "degree_es": "Diplomatura en Análisis de Datos para el Sector Público",
        "degree_en": "Diploma in Data Analysis for the Public Sector",
        "institution": "IPAP – UTN La Plata",
        "faculty_es": "Instituto Provincial de la Administración Pública · Universidad Tecnológica Nacional",
        "faculty_en": "Provincial Institute of Public Administration · National Technological University",
        "location_es": "La Plata, Provincia de Buenos Aires",
        "location_en": "La Plata, Buenos Aires Province",
        "date_es": "En curso · Dic. 2026",
        "date_en": "In progress · Dec. 2026",
        "description_es": (
            "Especialización aplicada al sector público en explotación de registros administrativos, "
            "producción estadística, sistemas de información geográfica (SIG), visualización con Tableau y programación en R."
        ),
        "description_en": (
            "Applied public-sector specialization in administrative records for statistical production, "
            "geographic information systems (GIS), Tableau visualization, and R programming."
        ),
        "badge_es": "Diplomatura · En Curso",
        "badge_en": "Diploma · In Progress",
    },
]

TRAINING = [
    {
        "title_es": "Tableau, Estadística, SIG, Registros Administrativos y Programación en R",
        "title_en": "Tableau, Statistics, GIS, Administrative Records, and R Programming",
        "institution": "IPAP",
        "date_es": "2026",
        "date_en": "2026",
        "location_es": "Provincia de Buenos Aires, Argentina",
        "location_en": "Buenos Aires Province, Argentina",
        "description_es": (
            "Cursos de especialización en registros administrativos para producción estadística, "
            "sistemas de información geográfica (SIG), análisis estadístico, Tableau y R."
        ),
        "description_en": (
            "Specialization courses in administrative records for statistical production, "
            "geographic information systems (GIS), statistical analysis, Tableau, and R."
        ),
        "tags_es": ["Tableau", "SIG / GIS", "Registros Administrativos", "R"],
        "tags_en": ["Tableau", "GIS", "Administrative Records", "R"],
    },
    {
        "title_es": "Datos para el relato: análisis, interpretación y visualización de datos",
        "title_en": "Data storytelling: analysis, interpretation and visualization of data",
        "institution": "Fundar",
        "date_es": "2025",
        "date_en": "2025",
        "location_es": "Ciudad de Buenos Aires, Argentina",
        "location_en": "Buenos Aires, Argentina",
        "description_es": (
            "Especialización intensiva en narrativa basada en evidencia, diseño de visualizaciones "
            "y comunicación pública de hallazgos cuantitativos."
        ),
        "description_en": (
            "Intensive specialization in evidence-based storytelling, visualization design, "
            "and public communication of quantitative findings."
        ),
        "tags_es": ["Data Storytelling", "Visualización", "Políticas Públicas"],
        "tags_en": ["Data Storytelling", "Visualization", "Public Policy"],
    },
    {
        "title_es": "Programación en Python orientado a Ciencia de Datos",
        "title_en": "Python Programming for Data Science",
        "institution": "Argentina Humana",
        "date_es": "2024",
        "date_en": "2024",
        "location_es": "Ciudad de Buenos Aires, Argentina",
        "location_en": "Buenos Aires, Argentina",
        "description_es": (
            "Desarrollo en Python orientado al procesamiento, limpieza, modelado y automatización "
            "de flujos de trabajo en ciencia de datos."
        ),
        "description_en": (
            "Python development focused on data processing, cleaning, modeling, and workflow "
            "automation in data science."
        ),
        "tags_es": ["Python", "Ciencia de Datos", "Automatización"],
        "tags_en": ["Python", "Data Science", "Automation"],
    },
    {
        "title_es": "Programación en R",
        "title_en": "R Programming",
        "institution": "Ecofeminita",
        "date_es": "2023",
        "date_en": "2023",
        "location_es": "Ciudad de Buenos Aires, Argentina",
        "location_en": "Buenos Aires, Argentina",
        "description_es": (
            "Procesamiento, limpieza y análisis estadístico de bases de datos socioeconómicas "
            "utilizando el ecosistema Tidyverse."
        ),
        "description_en": (
            "Processing, cleaning, and statistical analysis of socioeconomic datasets "
            "using the R Tidyverse ecosystem."
        ),
        "tags_es": ["R", "Tidyverse", "Estadística Socioeconómica"],
        "tags_en": ["R", "Tidyverse", "Socioeconomic Statistics"],
    },
]

SKILLS = [
    {
        "category_es": "Lenguajes y Herramientas",
        "category_en": "Languages & Tools",
        "icon": "code-xml",
        "description_es": "Ecosistema de análisis de alto rendimiento, control de versiones y bases de datos.",
        "description_en": "High-performance analytics ecosystem, version control, and databases.",
        "items_es": [
            "Python (Polars, pandas, NumPy)",
            "SciPy · statsmodels · scikit-learn",
            "PyArrow",
            "R (Tidyverse)",
            "SQL",
            "Git / GitHub",
            "Linux / Bash",
        ],
        "items_en": [
            "Python (Polars, pandas, NumPy)",
            "SciPy · statsmodels · scikit-learn",
            "PyArrow",
            "R (Tidyverse)",
            "SQL",
            "Git / GitHub",
            "Linux / Bash",
        ],
    },
    {
        "category_es": "Econometría y Métodos",
        "category_en": "Econometrics & Methods",
        "icon": "trending-up",
        "description_es": "Modelado econométrico, evaluación de impacto e inteligencia fiscal a gran escala.",
        "description_en": "Econometric modeling, impact evaluation, and large-scale fiscal intelligence.",
        "items_es": [
            "SARIMAX y Series de Tiempo",
            "Diferencias en Diferencias (DiD)",
            "Cointegración",
            "Selección Automatizada de Modelos",
            "Estimación de Recaudación Subnacional",
            "Cruces Masivos e Inteligencia Fiscal",
            "Índices Multidimensionales y Métodos Mixtos",
        ],
        "items_en": [
            "SARIMAX & Time Series",
            "Difference-in-Differences (DiD)",
            "Cointegration",
            "Automated Model Selection",
            "Subnational Revenue Forecasting",
            "Large-Scale Cross-Matching & Tax Analytics",
            "Multidimensional Indices & Mixed Methods",
        ],
    },
    {
        "category_es": "Ingeniería de Datos",
        "category_en": "Data Engineering",
        "icon": "database",
        "description_es": "Ingesta automatizada, validación en tiempo real y pipelines reproducibles.",
        "description_en": "Automated ingestion, real-time validation, and reproducible pipelines.",
        "items_es": [
            "Pipelines ETL Reproducibles",
            "REST APIs (KoboToolbox)",
            "Bots con Telegram Bot API",
            "Validación y Monitoreo en Tiempo Real",
        ],
        "items_en": [
            "Reproducible ETL Pipelines",
            "REST APIs (KoboToolbox)",
            "Telegram Bot API Bots",
            "Real-Time Validation & Monitoring",
        ],
    },
    {
        "category_es": "Captura de Datos y Campo",
        "category_en": "Data Collection & Fieldwork",
        "icon": "clipboard-check",
        "description_es": "Diseño muestral e instrumentos digitales para operativos estadísticos federales.",
        "description_en": "Sampling design and digital instruments for nationwide survey operations.",
        "items_es": [
            "XLSForm (KoboToolbox, ODK, SurveyCTO)",
            "Muestreo Probabilístico y por Cuotas",
            "Encuestas de Uso del Tiempo (ENUT)",
            "Auditoría de Calidad de Datos",
        ],
        "items_en": [
            "XLSForm (KoboToolbox, ODK, SurveyCTO)",
            "Probability & Quota Sampling",
            "Time-Use Surveys (ENUT)",
            "Data Quality Auditing",
        ],
    },
    {
        "category_es": "Visualización",
        "category_en": "Visualization",
        "icon": "bar-chart-3",
        "description_es": "Tableros para la toma de decisiones y narrativas visuales para medios y políticas públicas.",
        "description_en": "Decision-support dashboards and visual storytelling for policy and broadcast media.",
        "items_es": [
            "Streamlit",
            "Tableau",
            "Flourish",
            "Matplotlib",
            "Seaborn",
        ],
        "items_en": [
            "Streamlit",
            "Tableau",
            "Flourish",
            "Matplotlib",
            "Seaborn",
        ],
    },
    {
        "category_es": "Ciencia Abierta e Idiomas",
        "category_en": "Open Science & Languages",
        "icon": "globe",
        "description_es": "Publicación de microdatos bajo estándares internacionales y comunicación técnica.",
        "description_en": "Microdata publication under international standards and technical communication.",
        "items_es": [
            "Anonimización de Microdatos",
            "Metadatos bajo Estándares FAIR",
            "Repositorios en GitHub y Zenodo (DOI)",
            "Español (Nativo)",
            "Inglés Técnico Profesional",
        ],
        "items_en": [
            "Microdata Anonymization",
            "FAIR-Standard Metadata",
            "GitHub & Zenodo Repositories (DOI)",
            "Spanish (Native)",
            "Professional Working English",
        ],
    },
]

PUBLICATIONS = [
    {
        "type_es": "Ciencia Abierta · Datos Abiertos",
        "type_en": "Open Science · Open Data",
        "year": "2026 · Actualidad",
        "authors": "Mora Benitez, D. — Observatorio Villero (La Poderosa)",
        "title_es": "Observadata: Repositorio público de datos abiertos para transformar la realidad",
        "title_en": "Observadata: Open Data Repository to Transform Reality",
        "description_es": (
            "Repositorio oficial de datos abiertos del Observatorio Villero. Reúne relevamientos nacionales, "
            "microdatos anonimizados, diseños de registro, metadatos bajo estándares FAIR y tabulados "
            "alojados en GitHub y respaldados en Zenodo con identificador DOI permanente."
        ),
        "description_en": (
            "Official open data repository of the Socioeconomic Observatory. Hosts nationwide surveys, "
            "anonymized microdata, record layouts, FAIR-standard metadata, and tabulations on GitHub "
            "backed by Zenodo with permanent DOIs."
        ),
        "venue_es": "GitHub & Zenodo · Observatorio Villero de La Poderosa.",
        "venue_en": "GitHub & Zenodo · Socioeconomic Observatory of La Poderosa.",
        "links": [
            {
                "label_es": "Repositorio en GitHub",
                "label_en": "GitHub Repository",
                "url": "https://github.com/ObservatorioVillero/observadata",
            },
            {
                "label_es": "Ver en Observatorio Villero",
                "label_en": "View on Observatory Site",
                "url": "https://observatoriovillero.lapoderosa.org.ar/proyecto/10",
            },
        ],
        "icon": "database",
        "accent": "green",
    },
    {
        "type_es": "Relevamiento Federal · Endeudamiento",
        "type_en": "Nationwide Survey · Household Debt",
        "year": "Oct. 2026",
        "authors": "Observatorio Villero (La Poderosa) & Fundación Friedrich Ebert (FES)",
        "title_es": "Endeudamiento en barrios populares: circuitos informales y costos no monetarios",
        "title_en": "Household Debt in Low-Income Neighborhoods: Informal Credit Circuits & Non-Monetary Costs",
        "description_es": (
            "Muestreo por cuotas de género y edad a 643 personas endeudadas en 12 barrios populares "
            "de 7 provincias (Buenos Aires, Córdoba, Santa Fe, La Rioja, San Juan, Entre Ríos y Corrientes). "
            "Indaga circuitos financieros informales invisibles en el BCRA/Veraz, tasas, usos de la deuda "
            "y sus efectos sobre la salud mental y el bienestar."
        ),
        "description_en": (
            "Gender- and age-quota survey of 643 indebted residents across 12 low-income neighborhoods "
            "in 7 provinces. Captures informal credit circuits invisible to central bank registries, "
            "interest rates, debt uses, and non-monetary impacts on mental health and well-being."
        ),
        "venue_es": "Observatorio Villero de La Poderosa con apoyo de Fundación Friedrich Ebert (FES).",
        "venue_en": "Socioeconomic Observatory of La Poderosa supported by Friedrich Ebert Foundation (FES).",
        "links": [
            {
                "label_es": "Descargar informe (PDF)",
                "label_en": "Download report (PDF)",
                "url": "https://observatoriovillero.lapoderosa.org.ar/media/encuesta-endeudamiento-2026-v5.pdf",
            },
            {
                "label_es": "Ver proyecto",
                "label_en": "View project",
                "url": "https://observatoriovillero.lapoderosa.org.ar/proyecto/11",
            },
        ],
        "icon": "trending-up",
        "accent": "burgundy",
    },
    {
        "type_es": "Relevamiento Federal · Trabajo Comunitario",
        "type_en": "Nationwide Survey · Community Care Work",
        "year": "2025 – Mar. 2026",
        "authors": "Observatorio Villero (La Poderosa) & SAGE Foundation",
        "title_es": "Encuesta de Uso del Tiempo en Barrios Populares: medición del Trabajo Comunitario de Cuidados",
        "title_en": "Time-Use Survey in Low-Income Neighborhoods: Measuring Community Care Work",
        "description_es": (
            "Relevamiento a escala nacional en 71 barrios populares de 14 provincias (1.096 hogares y "
            "1.241 trabajadoras/es comunitarios). Adaptó el clasificador de la ENUT-INDEC con diario de "
            "actividades para cuantificar la triple jornada laboral y dar sustento empírico a la Ley de "
            "Salario para las Cocineras Comunitarias."
        ),
        "description_en": (
            "Nationwide survey across 71 neighborhoods in 14 provinces (1,096 households and 1,241 "
            "community care workers). Adapted the INDEC ENUT activity classifier with time-use diaries "
            "to measure the triple workday and support the Community Cooks' Wage Bill."
        ),
        "venue_es": "Observatorio Villero de La Poderosa con apoyo de SAGE Foundation.",
        "venue_en": "Socioeconomic Observatory of La Poderosa supported by SAGE Foundation.",
        "links": [
            {
                "label_es": "Informe definitivo (PDF)",
                "label_en": "Final report (PDF)",
                "url": "https://observatoriovillero.lapoderosa.org.ar/media/EUT-TCC._Resultados_finales_2026.pdf",
            },
            {
                "label_es": "Base de datos (Observadata)",
                "label_en": "Open dataset (Observadata)",
                "url": "https://github.com/ObservatorioVillero/observadata/tree/main/encuesta-uso-del-tiempo/2025",
            },
            {
                "label_es": "Ver proyecto",
                "label_en": "View project",
                "url": "https://observatoriovillero.lapoderosa.org.ar/proyecto/9",
            },
        ],
        "icon": "clock",
        "accent": "green",
    },
    {
        "type_es": "Relevamiento Federal · Hábitat y Servicios",
        "type_en": "Nationwide Survey · Housing & Services",
        "year": "2024 – Ago. 2025",
        "authors": "Observatorio Villero (La Poderosa), ACIJ, IIGG-UBA & Fundación TEMAS",
        "title_es": "Condiciones de vida en barrios populares (2024–2025)",
        "title_en": "Living Conditions in Low-Income Neighborhoods (2024–2025)",
        "description_es": (
            "Relevamiento de 1.485 hogares y 5.024 personas en 9 barrios populares de 6 provincias "
            "(CABA, Buenos Aires, Córdoba, La Rioja, Corrientes y Tierra del Fuego). Analiza hacinamiento, "
            "riesgo eléctrico, agua segura, saneamiento, movilidad, infraestructura barrial y demandas comunitarias."
        ),
        "description_en": (
            "Survey of 1,485 households and 5,024 residents across 9 neighborhoods in 6 provinces. "
            "Examines overcrowding, electrical hazards, safe water, sanitation, mobility, urban "
            "infrastructure, and community priorities."
        ),
        "venue_es": "Observatorio Villero, ACIJ, Instituto Gino Germani (UBA) & Fundación TEMAS.",
        "venue_en": "Observatorio Villero, ACIJ, Gino Germani Research Institute (UBA) & Fundación TEMAS.",
        "links": [
            {
                "label_es": "Descargar informe (PDF)",
                "label_en": "Download report (PDF)",
                "url": "https://observatoriovillero.lapoderosa.org.ar/media/observatorio-villero_condiciones_de_vida_2024.pdf",
            },
            {
                "label_es": "Web interactiva",
                "label_en": "Interactive web",
                "url": "https://lapoderosa.acij.org.ar/",
            },
            {
                "label_es": "Base de datos (Observadata)",
                "label_en": "Open dataset (Observadata)",
                "url": "https://github.com/ObservatorioVillero/observadata/tree/main/condiciones-de-vida/2024",
            },
        ],
        "icon": "home",
        "accent": "green",
    },
    {
        "type_es": "Publicación · Políticas de Urbanización",
        "type_en": "Publication · Urbanization Policy",
        "year": "Abr. 2025",
        "authors": "Cappa, A., Cejas Marcovecchio, M., Miño, L., & Mora Benitez, D.",
        "title_es": "Avances y desafíos en la urbanización de barrios populares: Políticas públicas para una transformación real (2021–2023)",
        "title_en": "Advances and Challenges in the Urbanization of Low-Income Neighborhoods: Public Policies for Real Transformation (2021–2023)",
        "description_es": (
            "Evaluación de la política de integración sociourbana (SISU) y la ejecución del Fondo de "
            "Integración Socio Urbana (FISU), su financiamiento progresivo (Aporte Solidario e impuesto PAIS), "
            "su impacto federal en infraestructura básica y el rol de las cooperativas comunitarias."
        ),
        "description_en": (
            "Assessment of Argentina's socio-urban integration policy (SISU) and the Socio-Urban "
            "Integration Fund (FISU), analyzing its progressive tax financing, nationwide basic "
            "infrastructure impact, and the role of community cooperatives."
        ),
        "venue_es": "Fundación Friedrich Ebert (FES), OCEPP & Observatorio Villero (La Poderosa).",
        "venue_en": "Friedrich Ebert Foundation (FES), OCEPP & Socioeconomic Observatory (La Poderosa).",
        "links": [
            {
                "label_es": "Publicación en FES",
                "label_en": "FES Publication",
                "url": "https://collections.fes.de/publikationen/ident/fes/21968",
            },
            {
                "label_es": "Nota en Observatorio",
                "label_en": "Observatory Article",
                "url": "https://observatoriovillero.lapoderosa.org.ar/informes/7",
            },
        ],
        "icon": "book-open",
        "accent": "burgundy",
    },
    {
        "type_es": "Investigación Cualitativa · UNICEF",
        "type_en": "Qualitative Study · UNICEF",
        "year": "Sep. 2023",
        "authors": "Dávolos, P. — UNICEF Argentina & Observatorio Villero (La Poderosa)",
        "title_es": "La situación de la pobreza en los barrios populares: Estudio cualitativo",
        "title_en": "The Poverty Situation in Low-Income Neighborhoods: A Qualitative Study",
        "description_es": (
            "Trabajo de campo en Santa Fe, Entre Ríos, Tucumán y CABA (22 entrevistas en profundidad, "
            "grupos focales y observación participante) sobre estrategias de organización comunitaria, "
            "redes de cuidado, precariedad habitacional y trayectorias educativas de niños, niñas y adolescentes."
        ),
        "description_en": (
            "Fieldwork in Santa Fe, Entre Ríos, Tucumán, and Buenos Aires City (22 in-depth interviews, "
            "focus groups, and participant observation) on community networks, care strategies, housing "
            "precarity, and children's educational trajectories."
        ),
        "venue_es": "UNICEF Argentina & Observatorio Villero de La Poderosa.",
        "venue_en": "UNICEF Argentina & Socioeconomic Observatory of La Poderosa.",
        "links": [
            {
                "label_es": "Ver estudio UNICEF (PDF)",
                "label_en": "View UNICEF study (PDF)",
                "url": "https://observatoriovillero.lapoderosa.org.ar/media/Estudio_cualitativo__la_situaci%C3%B3n_de_la_pobreza_en_barrios_populares.pdf",
            },
            {
                "label_es": "Ver proyecto",
                "label_en": "View project",
                "url": "https://observatoriovillero.lapoderosa.org.ar/proyecto/7",
            },
        ],
        "icon": "file-text",
        "accent": "green",
    },
    {
        "type_es": "Artículo Publicado",
        "type_en": "Published Article",
        "year": "Mar. 2023",
        "authors": "Mora Benitez, D.",
        "title_es": (
            "Relevamiento de condiciones habitacionales en barrios populares: "
            "El rol del Observatorio Villero de La Poderosa en la producción de estadísticas comunitarias"
        ),
        "title_en": (
            "Survey on Housing Conditions in Informal Settlements: "
            "The Role of the Villero Observatory of La Poderosa in the Production of Community Statistics"
        ),
        "description_es": (
            "Sistematización metodológica y analítica de la producción de estadísticas comunitarias sobre "
            "1.222 viviendas en 23 barrios populares de 16 provincias argentinas: hacinamiento, riesgo "
            "eléctrico, agua potable, saneamiento y exposición a riesgos ambientales."
        ),
        "description_en": (
            "Methodological and analytical account of community-led statistical production covering "
            "1,222 dwellings in 23 neighborhoods across 16 Argentine provinces: overcrowding, electrical "
            "hazards, water, sanitation, and environmental risks."
        ),
        "venue_es": "Revista Idelcoop, N° 239, pp. 128–140.",
        "venue_en": "Revista Idelcoop, Issue 239, pp. 128–140.",
        "links": [
            {
                "label_es": "Leer artículo (PDF)",
                "label_en": "Read article (PDF)",
                "url": "https://observatoriovillero.lapoderosa.org.ar/media/ObservatorioVillero-IDELCOOP.pdf",
            },
            {
                "label_es": "Nota en Observatorio",
                "label_en": "Observatory Article",
                "url": "https://observatoriovillero.lapoderosa.org.ar/informes/8",
            },
        ],
        "icon": "file-text",
        "accent": "green",
    },
    {
        "type_es": "Relevamiento Federal · Infraestructura",
        "type_en": "Nationwide Survey · Urban Infrastructure",
        "year": "Sep. 2022",
        "authors": "Observatorio Villero (La Poderosa), Fundación Rosa Luxemburgo & El Gato y La Caja",
        "title_es": "Condiciones habitacionales y servicios públicos en barrios populares (2022)",
        "title_en": "Housing Conditions and Public Services in Low-Income Neighborhoods (2022)",
        "description_es": (
            "Relevamiento en 1.222 viviendas de 23 barrios populares en 16 provincias sobre déficit de "
            "infraestructura de servicios públicos básicos, riesgo eléctrico, acceso al agua, recolección "
            "de residuos, inundaciones, conectividad y acceso a salud y transporte."
        ),
        "description_en": (
            "Survey across 1,222 dwellings in 23 neighborhoods and 16 provinces on basic public utility "
            "deficits, electrical hazards, water access, waste collection, flooding, internet connectivity, "
            "and access to healthcare and transit."
        ),
        "venue_es": "Observatorio Villero, Fundación Rosa Luxemburgo, Proyecto Habitar, Jóvenes por el Clima & El Gato y La Caja.",
        "venue_en": "Observatorio Villero, Rosa Luxemburg Foundation, Proyecto Habitar, Jóvenes por el Clima & El Gato y La Caja.",
        "links": [
            {
                "label_es": "Web interactiva (El Gato y La Caja)",
                "label_en": "Interactive web (El Gato y La Caja)",
                "url": "https://lapoderosa.elgatoylacaja.com/",
            },
            {
                "label_es": "Ver proyecto",
                "label_en": "View project",
                "url": "https://observatoriovillero.lapoderosa.org.ar/proyecto/6",
            },
        ],
        "icon": "compass",
        "accent": "burgundy",
    },
    {
        "type_es": "Relevamiento Federal · Salud y Género",
        "type_en": "Nationwide Survey · Health & Gender",
        "year": "2021",
        "authors": "Observatorio Villero (La Poderosa)",
        "title_es": "Relevamiento Nacional de Gestión Menstrual en Barrios Populares",
        "title_en": "National Survey on Menstrual Health Management in Low-Income Neighborhoods",
        "description_es": (
            "Encuesta a 2.478 hogares y 3.598 personas menstruantes en 67 barrios populares de 22 provincias. "
            "Relevó las barreras económicas de acceso (el 59% debió prescindir de comprar productos de gestión "
            "menstrual para priorizar alimentos u otros bienes esenciales y el 64% utilizó sustitutos) y el "
            "ausentismo escolar y laboral asociado."
        ),
        "description_en": (
            "Survey of 2,478 households and 3,598 menstruating people in 67 neighborhoods across 22 provinces. "
            "Documented economic barriers to menstrual products (59% had to forgo purchases to prioritize food "
            "or essentials; 64% used makeshift substitutes) and resulting school and work absenteeism."
        ),
        "venue_es": "Observatorio Villero de La Poderosa.",
        "venue_en": "Socioeconomic Observatory of La Poderosa.",
        "links": [
            {
                "label_es": "Ver relevamiento y resultados",
                "label_en": "View survey & findings",
                "url": "https://observatoriovillero.lapoderosa.org.ar/proyecto/1",
            },
        ],
        "icon": "heart-pulse",
        "accent": "burgundy",
    },
    {
        "type_es": "Expositor y Moderador en Congresos",
        "type_en": "Conference Speaker & Moderator",
        "year": "2023",
        "authors": "Mora Benitez, D.",
        "title_es": "Ponencias sobre medición de la pobreza (La Canasta Villera) y economía cooperativa",
        "title_en": "Presentations on Poverty Measurement (Informal Settlements Basket) & Cooperative Economy",
        "description_es": (
            "Expositor en la conferencia «Métodos de medición de la pobreza: La Canasta Villera» "
            "(Facultad de Trabajo Social, Universidad Nacional de Entre Ríos, oct. 2023) y moderador del "
            "«Conversatorio de Economía y Trabajo Cooperativo» (3er Encuentro Nacional de Cooperativas de "
            "La Poderosa, Cabildo de Córdoba, 2023)."
        ),
        "description_en": (
            "Speaker at 'Methods for Measuring Poverty: The Informal Settlements Basket' (Faculty of Social "
            "Work, National University of Entre Ríos, Oct. 2023) and moderator of the 'Panel on Economy and "
            "Cooperative Work' (3rd National Meeting of Cooperatives of La Poderosa, Cabildo of Córdoba, 2023)."
        ),
        "venue_es": "Universidad Nacional de Entre Ríos (UNER) & Cabildo de la Ciudad de Córdoba.",
        "venue_en": "National University of Entre Ríos (UNER) & Cabildo of the City of Córdoba.",
        "links": [],
        "icon": "mic",
        "accent": "green",
    },
]
