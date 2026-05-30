# Decision Tables

## merge decision

| condition | decision |
|---|---|
| same label but different role | do not merge |
| same source and same meaning | merge candidate |
| source definitions conflict | record conflict |
| alias without proof | keep alias candidate |

## promotion decision

| condition | decision |
|---|---|
| source, evidence, and assertionBasis visible | may promote to asserted |
| search result only | keep candidate |
| unresolved conflict | do not promote |
| user confirmed but source absent | provisional only |

## connector decision

| consumer need | output |
|---|---|
| research | source, concept, relation, question packet |
| verification | rule, exception, evidence, conflict packet |
| coding | concept, attribute, enum, validation packet |
| domain work | domain concept/relation/rule packet |

## close decision

| condition | status |
|---|---|
| exports and connector packets updated | ready |
| conflicts unresolved | partial |
| source missing | blocked |
