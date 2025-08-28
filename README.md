📄 README.md für BTP_Publication_API
# BTP_Publication_API

Eine leichtgewichtige API zur Veröffentlichung und Verwaltung von Services
in der **SAP Business Technology Platform (BTP)**.  
Ziel ist es, den Publikationsprozess zu automatisieren und nahtlos in
CI/CD-Pipelines oder manuelle Deployments zu integrieren.

---

## 📦 Manifest

```yaml
name: BTP_Publication_API
description: API zum Publizieren von Services in SAP BTP
version: 0.1.0
author: Hannes Kröner (@haaansz)
license: MIT
repository: https://github.com/haaansz/BTP_Publication_API
status: alpha

⚙️ Requirements
runtime:
  node: ">=18.x"        # oder java >=17, je nach Implementierung
dependencies:
  - express / spring-boot
  - axios / http-client
  - dotenv
environment:
  - BTP_BASE_URL
  - BTP_API_TOKEN

🚀 Installation
# Repository klonen
git clone https://github.com/haaansz/BTP_Publication_API.git
cd BTP_Publication_API

# Abhängigkeiten installieren
npm install        # falls Node.js
# mvn install      # falls Java

🔧 Configuration
env:
  BTP_BASE_URL: "https://<your-btp-endpoint>"
  BTP_API_TOKEN: "<token>"

optional:
  LOG_LEVEL: "debug | info | warn | error"
  PORT: 8080

▶️ Usage

Server starten:

npm start
# oder bei Java:
mvn spring-boot:run

Beispiel-Request
curl -X POST \
  $BTP_BASE_URL/publications \
  -H "Authorization: Bearer $BTP_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "serviceName": "MyService",
    "version": "1.0.0",
    "environment": "prod",
    "description": "Publish Service v1.0.0"
  }'


Antwort:

{
  "status": "queued",
  "publicationId": "12345",
  "message": "Publishing started"
}

🤝 Contributing
workflow:
  - Fork erstellen
  - Feature-Branch anlegen
  - Code & Tests hinzufügen
  - Pull Request erstellen

guidelines:
  - Code-Style: eslint/prettier (Node) oder checkstyle (Java)
  - Tests: jest/mocha (Node) oder JUnit (Java)
  - Commits: Conventional Commits

📜 License
type: MIT
url: https://opensource.org/licenses/MIT


---

👉 Das Ganze ist im **Markdown mit Codeblöcken** formatiert und sollte beim Einfügen ins Repo sofort sauber gerendert werden.  

Möchtest du, dass ich zusätzlich noch ein **kleines Architekturdiagramm in ASCII** (z. B. `Client → BTP_Publication_API → SAP BTP`) in einen Block einfüge, damit die README visuell etwas „catchiger“ wirkt?
