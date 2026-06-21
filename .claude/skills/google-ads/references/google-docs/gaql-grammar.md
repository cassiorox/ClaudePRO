GAQL grammar
https://developers.google.com/google-ads/api/docs/query/grammar
Baixado para Google Ads API v23

# Google Ads Query Language Grammar

Grammar reference (in regular expression notation):

```
Query            -> SelectClause FromClause WhereClause? OrderByClause?
                    LimitClause? ParametersClause?
SelectClause     -> SELECT FieldName (, FieldName)*
FromClause       -> FROM ResourceName
WhereClause      -> WHERE Condition (AND Condition)*
OrderByClause    -> ORDER BY Ordering (, Ordering)*
LimitClause      -> LIMIT PositiveInteger
ParametersClause -> PARAMETERS Literal = Value (, Literal = Value)*

Condition        -> FieldName Operator Value
Operator         -> = | != | > | >= | < | <= | IN | NOT IN |
                    LIKE | NOT LIKE | CONTAINS ANY | CONTAINS ALL |
                    CONTAINS NONE | IS NULL | IS NOT NULL | DURING |
                    BETWEEN | REGEXP_MATCH | NOT REGEXP_MATCH
Value            -> Literal | LiteralList | Number | NumberList | String |
                    StringList | Function
Ordering         -> FieldName (ASC | DESC)?

FieldName        -> [a-z] ([a-zA-Z0-9._])*
ResourceName     -> [a-z] ([a-zA-Z_])*

StringList       -> ( String (, String)* )
LiteralList      -> ( Literal (, Literal)* )
NumberList       -> ( Number (, Number)* )

PositiveInteger  -> [1-9] ([0-9])*
Number           -> -? [0-9]+ (. [0-9] [0-9]*)?
String           -> (' Char* ') | (" Char* ")
Literal          -> [a-zA-Z0-9_]*

Function         -> LAST_14_DAYS | LAST_30_DAYS | LAST_7_DAYS |
                    LAST_BUSINESS_WEEK | LAST_MONTH | LAST_WEEK_MON_SUN |
                    LAST_WEEK_SUN_SAT | THIS_MONTH | THIS_WEEK_MON_TODAY |
                    THIS_WEEK_SUN_TODAY | TODAY | YESTERDAY
```

- `?` indicates an optional element
- `*` means zero or more; `+` means one or more
- `(xxxxxx)` indicates a grouping
- `[a-z0-9]` signifies character ranges
- `|` stands for "or"

## Rules and limitations
- The REGEXP_MATCH operator uses RE2 syntax.
- To match a literal `[`, `]`, `%`, or `_` using the LIKE operator, surround the character in square brackets. For example, the following condition matches all campaign.name values that start with `[Earth_to_Mars]`:
  ```
  campaign.name LIKE '[[]Earth[_]to[_]Mars[]]%'
  ```
- The LIKE operator can only be used on a string field, not an array.

Page last updated 2026-05-13 UTC. Content reflects Google Ads API v23 (latest serving).
