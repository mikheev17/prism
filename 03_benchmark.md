# 3. Бенчмаркинг конкурентов — PRism

> **Цель:** определить стандарты для продукта PRism через анализ конкурентов, сформулировать минимальные требования к функциональности,
> ключевые конкурентные преимущества и ориентиры для метрик.

---

## 3.1 Выбор конкурентов

| # | Конкурент | Тип | Обоснование |
|---|-----------|-----|-------------|
| 1 | **CodeRabbit** | Прямой | AI-powered PR review с inline-комментариями на GitHub/GitLab; самый релевантный по UX-сценарию. 2 млн+ репозиториев, 13 млн+ разобранных PR. |
| 2 | **Codacy** | Прямой | Автоматизированный code review с AI Reviewer на PR, inline-комментарии, confidence score, 49 языков. DevSecOps-платформа с SAST + quality. |
| 3 | **Snyk Code** | Косвенный | Специализированный security SAST с AI-анализом и fix suggestions. Задаёт планку точности детектирования в классе `SECURITY_MISCONFIG`. |

Все три интегрированы через GitHub App/webhook — тот же технический путь, что у PRism. CodeRabbit и Codacy — ближайшие аналоги по продуктовому сценарию; Snyk Code — эталон по security-классу.

---

## 3.2 Профили конкурентов

### 3.2.1 CodeRabbit

**Ссылки:** [coderabbit.ai](https://www.coderabbit.ai) · [docs.coderabbit.ai](https://docs.coderabbit.ai/management/plans) · [G2 Reviews](https://www.g2.com/products/coderabbit/pricing)

**Позиционирование:** «AI-powered code review tool that automates the code review process, providing context-aware feedback on pull requests within minutes.» Ускоритель ревью, а не замена человека.

**Ключевые преимущества:**
- Автоматические inline PR-комментарии в течение минут после открытия PR.
- Walkthrough и architectural diagrams к каждому PR.
- One-click fix suggestions прямо в PR.
- Learning system: запоминает dismiss-ы и предпочтения команды.
- YAML-конфигурация: кастомные правила, path-specific rules, language filters.
- Агрегация 40+ линтеров и SAST-инструментов с LLM-фильтрацией шума.
- SOC 2 Type II, GDPR, zero training on customer code.
- GitHub, GitLab, Azure DevOps, Bitbucket + VS Code extension.

**Целевая аудитория:** команды 5–500+, особо релевантен для OSS (бесплатно) и продуктовых команд.

**Основные функции:**
- Автоматическое резюме PR + architectural walkthrough.
- Построчный AI review (баги, security, performance, style).
- Conversational chat внутри PR-комментария (explain / generate tests / docstrings).
- Аналитика по командам (review coverage, issue resolution rate).
- Multi-repo analysis, unit test generation, merge conflict resolution — Pro+.

**Цены:**

| План | Цена | Включено |
|------|------|----------|
| Free | $0 | Неограниченные репо; rate limits (4 reviews/h, 200 files/h); PR summary only |
| Pro | $24/dev/мес (annual) | Неограниченные reviews, 40+ integrations, analytics, autofix |
| Pro+ | $48/dev/мес (annual) | Всё из Pro + unit test gen, merge conflict resolution |
| Enterprise | от $15 000/мес | Self-hosting, SLA, RBAC, audit logging, CSM |

**Что хвалят:** скорость, автосаммари, one-click fixes, обучаемость, лёгкий онбординг.

**На что жалуются:** шум в первые недели, слабое понимание бизнес-логики и cross-module проблем, медленная поддержка.

---

### 3.2.2 Codacy

**Ссылки:** [codacy.com](https://www.codacy.com) · [codacy.com/pricing](https://www.codacy.com/pricing) · [G2 Reviews](https://www.g2.com/products/codacy/reviews)

**Позиционирование:** «The only DevSecOps platform that delivers plug-and-play code health and security scanning for AI and human generated code.» Акцент на compliance и enterprise SDLC.

**Ключевые преимущества:**
- AI Reviewer (Google Gemini, только GitHub; opt-in) — контекстуальные комментарии с учётом PR metadata, Jira-тикетов и Codacy data.
- False positive triage: confidence score на каждый issue.
- Кастомизация через `review.md` — инструкции AI Reviewer под стандарты команды.
- Самый широкий security-охват: SAST + SCA + DAST + secrets + SBOM + license scanning.
- SOC 2, GDPR; zero training on customer code; 49 языков.
- AI Guardrails для coding agents (Copilot, Cursor).

**Целевая аудитория:** enterprise и mid-market (50+ разработчиков), compliance-ориентированные команды.

**Основные функции:**
- Автоматический анализ code quality (complexity, duplication) на каждый PR.
- AI Reviewer с PR summary, inline fix suggestions, false positive detection.
- IDE plugin (VSCode, Cursor, Windsurf) с real-time SAST.
- Security dashboard: SAST, SCA, DAST, pentest findings в одном месте.
- SBOM reports, compliance reports (SOC2, ISO27001).
- MCP-интеграция для LLM-агентов.

**Цены:**

| План | Цена | Включено |
|------|------|----------|
| Open Source | $0 | Публичные репозитории, базовый анализ |
| Pro | $15/dev/мес (annual) | Автоматический code review, security, 49 языков, IDE plugin |
| Business | custom | AI Reviewer, AI Guardrails, enterprise compliance, DAST, SLA |

**Что хвалят:** широкое покрытие языков, security dashboard, быстрый онбординг.

**На что жалуются:** дорого для малых команд, AI Reviewer только на GitHub, FP требуют ручного review.

---

### 3.2.3 Snyk Code

**Ссылки:** [snyk.io](https://snyk.io) · [snyk.io/plans](https://snyk.io/plans/) · [Capterra Reviews](https://www.capterra.com/p/172252/Snyk/)

**Позиционирование:** «The AI Security Fabric. Secure at inception with continuous, autonomous defense for AI-generated code.» Developer-first SAST.

**Ключевые преимущества:**
- Специализированная AI-модель: обучена на верифицированных фиксах из OSS, понимает сложные паттерны уязвимостей.
- Data-flow анализ через несколько слоёв кода (SQL injection, XSS, insecure deserialization).
- PR blocking при High/Critical уязвимостях.
- Inline PR-комментарии с severity, data flow, fix suggestions.
- Автоматические dependency upgrade PR (Snyk Open Source).
- Accuracy: 85% при 8% FP rate (SAST Tool Evaluation Study 2024).

**Целевая аудитория:** банки, fintech, enterprise; DevSecOps teams; команды с compliance-требованиями.

**Основные функции:**
- Real-time SAST в IDE (JetBrains, VS Code).
- Автоматический PR scan; inline security comments.
- Snyk Open Source: SCA, dependency vulnerability, license compliance.
- Snyk Container: сканирование Docker images.
- Snyk IaC: анализ Terraform, Kubernetes, CloudFormation.
- Интеграция с GitHub, GitLab, Jira, Jenkins, Azure DevOps.

**Цены:**

| План | Цена | Включено |
|------|------|----------|
| Free | $0/dev | Базовый Snyk Code + Open Source, лимиты на тесты |
| Ignite (Team) | $105/dev/мес | Snyk Code + Open Source, расширенные лимиты, до 10 лицензий |
| Business / Enterprise | custom | Все продукты Snyk, AppRisk, неограниченные лицензии |

**Что хвалят:** точность security-детекции, data-flow анализ, fix suggestions, проактивная поддержка.

**На что жалуются:** высокий ценник, SAST слабее SCA, нет архитектурных паттернов, запутанный UI.

---

## 3.3 Сравнительная таблица

| Параметр | CodeRabbit | Codacy | Snyk Code | **PRism (цель)** |
|----------|-----------|--------|-----------|-----------------|
| **Фокус** | General AI PR review | DevSecOps quality + security | Security SAST | Архитектурные антипаттерны + SOLID + N+1 |
| **Интеграция** | GitHub, GitLab, Azure, Bitbucket | GitHub, GitLab, Bitbucket | GitHub, GitLab, Jira, CI/CD | GitHub App (MVP) |
| **Trigger** | Webhook на PR | Webhook + push | Webhook + IDE | Webhook на `pull_request` |
| **Тип анализа** | LLM generalist (GPT-4 / Claude) | Deterministic rules + AI (Gemini) | AI SAST + data flow | Специализированный CodeBERT + RAG + LLM |
| **Inline comments** | ✅ | ✅ | ✅ | ✅ |
| **Confidence / FP filtering** | ❌ | ✅ FP triage | Частично | ✅ per-class threshold |
| **Контекст кодовой базы** | Частично | ❌ | ❌ | ✅ RAG (пост-MVP) |
| **Архитектурные паттерны** | ❌ | ❌ | ❌ | ✅ SOLID, God Object, tight coupling |
| **N+1 / Race conditions** | ❌ | ❌ | ❌ | ✅ |
| **Security** | Базово | ✅ SAST, SCA, DAST, secrets | ✅✅ специализация | Частично (SECURITY_MISCONFIG) |
| **Языки (MVP)** | Все основные | 49 языков | Все основные | Python (MVP) |
| **Персонализация** | ✅ YAML + feedback | ✅ review.md | ❌ | ✅ `.prism.yml` + threshold per-class |
| **Dashboard** | ✅ | ✅ | ✅ | Пост-MVP |
| **IDE plugin** | ✅ VS Code | ✅ VSCode, Cursor, Windsurf | ✅ JetBrains, VS Code | ❌ MVP |
| **OSS / free tier** | ✅ неограниченно | ✅ публичные репо | ✅ с лимитами | TBD |
| **Цена (min paid)** | $24/dev/мес | $15/dev/мес | $105/dev/мес | $19/dev/мес (annual, гипотеза Team) |
| **Бизнес-модель** | Per seat | Per seat | Per seat/год | Per seat |
| **Целевой сегмент** | 5–500+ | 50+ (enterprise) | 10–10 000+ | 5–20 (стартапы, продуктовые команды) |
| **Compliance** | SOC 2 Type II, GDPR | SOC 2, GDPR | Корпоративные | TBD (пост-MVP) |
| **P95 latency** | ~2–3 мин | ~1–3 мин | ~2–5 мин | ≤ 10 с |
| **Accuracy** | ~85–90% (маркетинговое) | ~88% | 85% (8% FP) | F1 ≥ 0.72 (prod) |

---

## 3.4 Анализ

### Table stakes — обязательный минимум рынка

Без следующих функций продукт не воспринимается как серьёзный:

1. **Автоматический запуск** — trigger на webhook `pull_request`; ни один из конкурентов не требует ручного запуска.
2. **Inline-комментарии к конкретным строкам** — UX-стандарт; вывод в отдельный дашборд воспринимается как деградация.
3. **GitHub App с двухклик-установкой** — минимальный порог входа.
4. **Объяснение проблемы + совет по исправлению** — комментарий «здесь ошибка» без объяснения отклоняется.
5. **Защита от шума** — confidence threshold, FP triage или learning system; ни один конкурент не публикует всё подряд.
6. **Zero training on customer code** — privacy-требование; явно упоминается всеми тремя; отсутствие гарантии — блокер для enterprise.

### Дифференциаторы PRism

| Дифференциатор | Почему конкуренты его не дают |
|----------------|-------------------------------|
| **Специализированная классификация антипаттернов** (SOLID, N+1, Race Condition) | CodeRabbit и Codacy — generalist LLM; Snyk знает security, но не SOLID |
| **Confidence score в inline-комментарии** | Codacy использует его внутри для FP triage, но не показывает разработчику |
| **RAG-контекст из кодовой базы** (пост-MVP) | CodeRabbit частично использует file deps, но не строит полноценный векторный индекс |
| **Разделение ClassifierDecides / LLMFormulates** | Предотвращает галлюцинации LLM при вынесении вердикта |
| **Per-seat в полосе Codacy–CodeRabbit при узком scope** | Тот же биллинг-юнит, что у ближайших конкурентов, но без оплаты за generalist/DevSecOps full stack |

### Незакрытые боли конкурентов

| Боль | Решение PRism |
|------|---------------|
| **Шум в первые недели** (CodeRabbit) | Confidence threshold per-class с самого начала |
| **Нет архитектурного понимания** (все трое) | Специализированная модель + RAG (пост-MVP) |
| **Недоступный ценник** (Snyk) | ~$19/dev/мес (Team) vs $105+/dev/мес (Ignite) — для команды 5 чел. ~$95/мес vs $525+/мес |
| **Generalist feedback без специализации** (CodeRabbit, Codacy) | Классификатор различает `N_PLUS_ONE` и `EXCESSIVE_COMPLEXITY` |
| **FP triage непрозрачен** (Codacy) | Confidence score виден разработчику в inline-комментарии |

---

## 3.5 Стандарты для PRism

### MVP — минимальные требования к функциональности

| # | Требование | Обоснование |
|---|-----------|-------------|
| 1 | GitHub App с webhook на `pull_request` | Отсутствие автоматизации = нет продукта |
| 2 | Inline review-комментарии к конкретным строкам PR | UX-стандарт рынка |
| 3 | Объяснение проблемы + совет по исправлению в каждом комментарии | Generic «есть проблема» отклоняется пользователями |
| 4 | Confidence threshold — публикация только выше порога | Ключевой pain point всех конкурентов |
| 5 | Поддержка Python | Достаточно для первой когорты |
| 6 | Установка за 2 клика без обязательной настройки | Сложный онбординг = churn |
| 7 | Zero training on customer code (гарантия в документации) | Блокер для enterprise |
| 8 | P95 latency ≤ 10 с от webhook до публикации | Конкуренты считают «минуты»; 10 с — строже рынка |
| 9 | Error rate < 1% неуспешных генераций | Сбои в ревью = недоверие к инструменту |

### Ключевые конкурентные преимущества

| Преимущество | Проявление в продукте |
|-------------|----------------------|
| Специализированная классификация (CodeBERT fine-tuned) | Модель различает `SOLID_VIOLATION` и `N_PLUS_ONE`; конкуренты используют generalist LLM |
| Confidence score в inline-комментарии | Прозрачность: разработчик видит уверенность модели |
| RAG-контекст (пост-MVP) | Детектирование антипаттернов, невидимых в изолированном диффе (N+1 через модули) |
| ClassifierDecides / LLMFormulates | LLM не принимает решение о наличии проблемы — снижение галлюцинаций |
| Per-seat без «надбавки за всё» | Тот же формат, что у CodeRabbit/Codacy; Team ~$19/dev/мес (annual) — ниже CodeRabbit Pro ($24) при узком продуктовом scope |
| Фокус на архитектурных антипаттернах | Незакрытая ниша: ни один конкурент не специализируется на SOLID/N+1/Race Condition |

### Модель ценообразования

| Уровень | Цена | Описание |
|---------|------|----------|
| **Free / OSS** | $0 | Публичные репозитории — acquisition-канал (CodeRabbit набрал 2 млн репо через OSS) |
| **Team** | $19/dev/мес (annual) | MVP-гипотеза: активные контрибьюторы в периоде биллинга; ниже CodeRabbit Pro ($24) при том же per-seat |
| **Pro** | $39/dev/мес (annual) | Пост-MVP: RAG-контекст, dashboard, история PR, мультиязычность |
| **Enterprise** | custom | Self-hosting, SLA, SAML/SSO, audit logs |

**Billing unit:** **per seat** (активный разработчик в биллинг-периоде), как у CodeRabbit и Codacy — привычный формат закупки для mid-market и enterprise procurement.

**Trial:** 14 дней без кредитной карты — стандарт рынка (CodeRabbit, Codacy).

### Целевые метрики

| Метрика | Benchmark (рынок) | Цель PRism MVP | Источник |
|---------|--------------------|----------------|----------|
| **Helpful rate** | ~40–60% | ≥ 40% | 02_prototype.md |
| **False positive rate** | Snyk Code: 8% (SAST Eval 2024) | ≤ 20% | 02_prototype.md + Snyk benchmark |
| **P95 latency** (webhook → last comment) | «минуты» (CodeRabbit, Codacy) | ≤ 10 с | 02_prototype.md |
| **F1-macro классификатора** | Snyk: 85%; CodeRabbit: нет публ. метрик | ≥ 0.60 (MVP), ≥ 0.72 (prod) | 01_business_understanding.md |
| **Activation rate** (PR с ≥1 комментарием) | 50–80% (оценочно) | 60–80% | 02_prototype.md |
| **Error rate** | < 1% (SaaS-стандарт) | < 1% | 02_prototype.md |
| **Стоимость токенов на PR** | $0.01–0.05 (GPT-4o mini) | ≤ $0.05/PR | 02_prototype.md |
| **Время онбординга** | < 5 мин (CodeRabbit) | < 10 мин | CodeRabbit benchmark |
| **Cohen's kappa разметки** | ≥ 0.70 (NLP-стандарт) | ≥ 0.70 | 01_business_understanding.md |

---

## 3.6 Выводы

**PRism закрывает реальную нишу.** Ни один из конкурентов не специализируется на архитектурных антипаттернах (SOLID, N+1, Race Condition) с учётом контекста кодовой базы. CodeRabbit и Codacy используют generalist-LLM; Snyk Code знает только security.

**Главная угроза — шум.** Все три конкурента борются с нерелевантными комментариями. Confidence threshold per-class — правильная стратегия, требующая тщательной калибровки в первые недели реального трафика.

**Per-seat монетизация** — тот же тип, что у ближайших конкурентов (CodeRabbit, Codacy); гипотеза цены: **Team $19/dev/мес (annual)** — ниже полки CodeRabbit Pro ($24) за счёт узкого scope; **Pro $39/dev/мес** — проверка в trial-сценарии.

**OSS-free tier критически важен** для органического роста: viral loop через OSS-сообщество (один разработчик подключает — команда видит комментарии).

**Порог качества:** P95 ≤ 10 с, helpful rate ≥ 40%, FP rate ≤ 20%, F1-macro ≥ 0.60 — минимально приемлемые значения, ниже которых продукт не создаёт retention.