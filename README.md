# dlProject
Project for Deep Learning Course

## Schedule

Planned as of Proposal. 

```mermaid
gantt
    dateFormat  YYYY-MM-DD
    axisFormat  %m/%d
    title       Deep Learning Project - Proposed Project Timeline

    section Proposal
    Charter Team                     :done, p1, 2023-09-16, 2023-09-17
    Write Proposal                   :active, p2, after p1, 21d
    Research Topic and Tools         :active, p3, after p1, 21d
    Proposal DUE                     :crit, milestone, p4, 2023-10-08, 0d

    section Project Development
    Project Design                   :a1, after p4, 7d
    Build Data Pipeline              :a2, after p4, 14d
    Feature Engineering              :a3, 2023-10-15, 14d
    Design Neural Network            :a4, after a2, 21d
    Tune Hyperparameters             :a5, 2023-10-29, 21d
    Testing                          :a6, after a5, 7d
    Project Complete                 :crit, milestone, a7, after a6, 0d

    section Final Report
    Introduction                     :f1, 2023-10-29, 7d
    Methods                          :f2, after f1, 14d
    Results                          :f3, after a5, 14d
    Discussion                       :f4, after a5, 14d
    Review                           :f5, after f4, 8d
    Report DUE                       :crit, milestone, f6, 2023-12-11, 0d

    section Project Presentation
    Video Materials Prep             :v1, 2023-11-26, 7d
    Video Production                 :v2, after v1, 8d
    Presentation DUE                 :crit, milestone, v3, 2023-12-11, 0d
```

## Package Management

[Poetry](https://python-poetry.org/) is setup and optional to use, but nice if you choose to. 
