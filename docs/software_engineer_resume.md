# David Isaac Belais

505 SE 35th Ave, Portland OR 97214  |  503-267-0942  |
[david@belais.me](mailto:david@belais.me) |
[david.belais.me](https://david.belais.me) |
[github.com/davebelais](https://github.com/davebelais)

## Summary

I am a highly productive software and data engineer with 18 years of
experience, including 15 years working in complex, matrixed, enterprise
organizations.

I pride myself in:

-   Creating resilient, maintainable, integrous data products
-   Authoring elegant, bulletproof, type-annotated, well-formed, thoroughly
    tested, distributable Python libraries, CLIs, asynchronous micro-services
    (web APIs), and SDKs
-   Designing efficient, maintainable, testable, continuously integrated
    and deployed, modern software systems
-   Planning development work with clarity, flexibility, parallel execution,
    and collaboration in mind

## My Tools

Python, SQL, Spark, Databricks Lakehouse, Snowflake, Airflow, AWS
(Amazon Web Services) EMR (Elastic Map Reduce), AWS Lambda, AWS Aurora,
AWS IAM, Okta + OAuth 2, Apache Kafka (Produce + Consumer), Pub-sub Github,
PostgreSQL, Open API (Swagger), Linux, SQL Server, Github Actions, Jenkins,
SQLAlchemy, XML, HTML, SOAP, WSDL, C++, Javascript (not exhaustive, and not
necessarily in this order)

## Experience

### Nike | Lead Data/Software Engineer - Sustainability Analytics | March 2021 - June 2025

-   I lead engineering of the Nike Product & Materials Sustainability Index
    with data products published in Databricks Lakehouse (Unity Catalog),
    Snowflake, and (prior to 2023) S3 + hive/presto + EMR. We utilized Spark,
    Python (applications and libraries, distributed through JFrog Artifactory),
    ASGI Microservices (Python + FastAPI + SQLAlchemy +
    Alembic), Apache Kafka (as a publisher), and AWS Aurora PostgreSQL.
    This entailed design and implementation of systems for distilling
    material manufacturing process lifecycle assessment data,
    the expertise of the material scientists and sustainability professionals
    with whom we collaborated, and materials data from our product creation
    systems into data products attributing environmental impact
    measures (greenhouse gas emissions and water quality
    degradation/depletion) to Nike materials. We subsequently parsed
    product bills of material line items in order to infer material gross usage
    (way more involved than it sounds) in kilograms. Applying these measures
    to purchase order and demand planning data we were able to measure and
    track aggregate impacts for the enterprise. More importantly, we provided
    tools for product developers to reduce environmental impacts through
    better materials selection during the design process. To this end, we
    stood up micro-services (Python + FastAPI on AWS lambda) for product and
    material footprint scenario modeling.

-   I lead development of foundational data products exposing
    Environmental Health & Safety data from our 3rd-party EHS reporting system,
    Enablon (via their "Blink" OData API), in Databricks Lakehouse (Unity
    Catalog), Snowflake, and (prior to 2023) S3 + hive/presto + EMR. I used
    Spark and Python.

-   I authored enterprise CLIs (command line interfaces) and frameworks (Python
    libraries) for use in CI/CD and locally, numerous SDKs (software
    development kits) for internal and third-party platforms, extended
    SQLAlchemy and Alembic to facilitate use of ORMs
    (object relational mappings) across multiple dialects simultaneously, and
    to facilitate common and complex data frame operations in Spark, validate
    data products based on ORM metadata, securely retrieve managed credentials,
    and many other common development tasks.

### BICP @ Nike | Lead Data/Software Engineer - Sustainability Analytics | March 2020 - March 2021

-   I developed a SQLAlchemy-ORM-based framework for automating deployment and
    versioning (schema migration) supporting all database dialects leveraged
    by the Nike Enterprise Data & Analytics organization: Databricks,
    Snowflake, Hive/Presto on S3, and PostgreSQL with full rollback
    and versioning support.
-   I authored a framework for Sustainability Analytics' ETL jobs incorporating
    end-to-end schema-based data validations, local testing, and environment
    + file system abstraction.

### BICP @ Nike | Senior Data/Software Engineer - Sustainability Analytics | January 2020 - March 2020

### The Kroger Co. | Lead Data/Software Engineer - Web & Digital Analytics | May 2018 - November 2019

-   I lead development of data products distilling and exposing analytics to
    buyers and planners correlating digital and store sales and EBITDA with
    inventory,sell-through, prices, and promotional events&#8212;contributing
    to decisions resulting in a 56% increase in e-commerce sales in 2018 vs
    2017, and a 67% increase in ecommerce sales in 2019 vs 2018.

<!--
Note: the header above conveys a genericized role name based on current
industry usage, for clarity. My official title was "Senior Manager, Web &
Digital Analytics".
-->

### The Kroger Co. | Lead Data/Software Engineer - Product Information Management | November 2013 - May 2018

-   I lead development of multi-platform (Spark/Hive/Presto, Netezza, DB2,
    Python, SQL Server, SQLAlchemy)
    OLAP and OLTP data products to ingest, consolidate and normalize sales,
    dimensional, and click-stream data from disparate subsidiary and partner
    systems' transactional databases, streaming platforms, APIs, and
    mainframes.
-   I engineered algorithms for scoring semi-structured data and performing
    human-in-the loop data validation and auditing for product descriptions,
    specifications and photography acquired through trading partners (Python).
-   I established source-management capabilities for inbound data to handle
    complex retailer/vendor/manufacturer relationships (Python).
-   Collaborated with emerging digital initiatives to ensure the capture of all
    metrics needed to facilitate accountability and continuous operational
    improvement.

<!--
Note: the header above conveys a genericized role name based on current
industry usage, for clarity. My official title was "Manager, Web & Digital
Content".
-->

### The Kroger Co. (Fred Meyer Stores Inc.) | Business Systems Analyst - Ecommerce | March 2011 - November 2013

-   I researched, designed, and prototyped Fred Meyer's (and later Kroger's)
    product information management system for [customer-facing digital
    initiatives](https://fredmeyer.com).
-   I collaborated with Fred Meyer's technology partner, 1WorldSync, to
    establish a roadmap, data model, and procedures for sourcing and validating
    product data from [GDSN](https://www.gs1.org/services/gdsn) data pools for
    use in digital sales channels.

### Dissent Graphics Inc. | Full-Stack Developer | January 2008 - March 2011

-   I designed and developed web applications for clients including:
    The Garrigan Lyman Group, Microsoft, Best Buy, Avenue A Razorfish,
    Nereus Communications, BlackEyedPeas.com, TeeFury.com, the Travel Channel’s
    Man v. Food, TheWho.com, Custom Rights, Hello Minor, ExoticTravelers.com,
    and the ACLU of Oregon.

## Education

- Portland State University | Computer Science (Postbaccalaureate) | 2018
- The Art Institute of Portland | Media Arts & Animation | Bachelor of
  Science | 2007
- Portland State University | Web Design | 2002 - 2004
- Loyola Marymount University | Fine Arts | 2000 - 2001

## Open Source Projects

...because code examples are worth a thousand interview questions!

-   [dependence](https://dependence.enorganic.org/):
    A CLI and library for aligning a python projects' declared dependencies with the package versions installed in the environment in which dependence is executed, and for "freezing" recursively resolved package dependencies (like pip freeze, but for a package, instead of the entire environment).
-   [maya-zen-tools](https://maya-zen-tools.enorganic.org/):
    An Autodesk Maya extension providing modeling tools for
    manipulating a polygon mesh using dynamically created NURBS curves and
    surfaces to distribute vertices and/or UVs
-   [oapi](https://oapi.enorganic.org/): A python library for generating client
    SDKs from Open API documents
-   [git-author-stats](https://github.com/enorganic/git-author-stats#git-author-stats):
    A CLI and library for extracting periodic author "stats" (insertions and
    deletions) for a Git repository or Github organization
-   [gittable](https://gittable.enorganic.org/): A CLI and library for
    performing common, but complex, development and CI/CD tasks for a Git
    repository, such as tagging a commit with your current project/package
    version and downloading or accessing specific file(s) from a remote
    repository (including non-public repos)

Please see Github ([github.com/davebelais](https://github.com/davebelais)) for
a full accounting of my activities :-)

## Certifications

- [JQL for Admins](https://university.atlassian.com/student/award/SbuF34YQEXwk3oDXv1coga2H)
- [Jira Automation for Admins](https://university.atlassian.com/student/award/KPXH8RPefKoMhjUno6PSfQkA)
- [AWS Certified Big Data - Specialty](https://www.youracclaim.com/badges/c9885f75-2b4e-42ea-b499-0f99eee3b7e9/public_url)
- [AWS Certified Cloud Practitioner](https://www.youracclaim.com/badges/68b84f25-96ee-4796-ac16-4c625ef4aadd/public_url)
