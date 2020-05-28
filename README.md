# Bigram-feature-vector-extraction-NPL-ML
Extracting Bigram dictionary from a natural language and then transforming it into a sparse feature vector.

## Example of transformation
### the following bigram dictionary:
{" s":3, "tr":2, "st":2, "s ":2, "ri":2, "ng":2, "is":2, "in":2, "th":1, "sa":1, "pl":1, "mp":1, "le":1, "hi":1, "g ":1, "e ":1, "am":1, "a ":1, " i":1, " a":1}

### Next, write a feature extractor that transforms the bigram frequency distribution into a sparse feature vector from the UTF-8 encoded bigrams. For example, if the bigram is “th”:

“t” -> UTF-8 hex value 74
“h” -> UTF-8 hex value 68
7468 (hex) -> 29800 (decimal)

## Test Cases

feature_vector("hahahaha") = "24936:3 26721:4"
feature_vector(“banana”) = "24942:2 25185:1 28257:2"
feature_vector(“do or do not”) = "8292:1 8302:1 8303:1 25711:2 28271:1 28448:2 28530:1 28532:1 29216:1"




