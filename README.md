# scivolt


## Commands

- `<ctrl> + O`: Open or create a file
- `<ctrl> + N`: Create a file
- 

## Specifications

- fields common throughout all:
  - date (date str): date note was created
  - status (`backlog`, `todo`, `doing`, `done`, `cancel`) or (bool)
  - tags (str):
  - areas (links):

### 1_sources

- __description__: media from which knowledge/information was derived
- __each entry should be__:
- __extra fields__:
  - date-published (date str):

### 2_concepts

- __description__: distillation of knowledge from sources or personal thoughts
- __each entry should be__: a __unitary__ and __standalone__ concept
- __extra fields__:
  - 

### 3_areas

- __description__: general areas of a certain field
- __each entry should be__: a page that covers general themes in a field, sort of like a page-tag combination


### 4_endeavors

- __description__: containers for personal projects, research endeavors, business ideas
- __each entry should be__: a description of the endeavor, including motivation, background, acceptance criteria, goals
- __extra fields__:
  - pursuit (`learning`, `creative`, `research`, `engineering`, `personal`)
    - if it is a learning endeavor it is the same as an area, except with goal  s


### 5_products

- __description__: any work product in pursuit of an endeavor
- __extra fields__:
  - endeavor (link): link to endeavor involved with this.
