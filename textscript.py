import spacy


# Load the English language model.
nlp = spacy.load("en_core_web_sm")
ruler = nlp.add_pipe("entity_ruler", before="ner")


# EntityRuler patterns cover known entities and symptoms.
# Pain activities will be handled separately later, so they do not need
# individual patterns here.
patterns = [
    # Body parts
    {"label": "body_part", "pattern": [{"LOWER": "knee"}]},
    {"label": "body_part", "pattern": [{"LOWER": "ankle"}]},
    {"label": "body_part", "pattern": [{"LOWER": "shoulder"}]},
    {"label": "body_part", "pattern": [{"LOWER": "acl"}]},
    {"label": "body_part", "pattern": [{"LOWER": "lower"}, {"LOWER": "back"}]},
    {"label": "body_part", "pattern": [{"LOWER": "hip"}]},
    {"label": "body_part", "pattern": [{"LOWER": "hamstring"}]},
    {"label": "body_part", "pattern": [{"LOWER": "calf"}]},
    {"label": "body_part", "pattern": [{"LOWER": "quad"}], "id": "quadriceps"},
    {"label": "body_part", "pattern": [{"LOWER": "quadriceps"}], "id": "quadriceps"},

    # Side
    {"label": "side", "pattern": [{"LOWER": {"IN": ["left", "right"]}}]},

    # Duration
    {
        "label": "duration",
        "pattern": [
            {"IS_DIGIT": True},
            {"LOWER": {"IN": ["day", "days", "week", "weeks"]}},
        ],
    },

    # General pain term; activity is not hard-coded here.
    {"label": "symptom", "pattern": [{"LOWER": "pain"}], "id": "pain"},

    # Fixed physical/sensory symptoms
    {"label": "symptom", "pattern": [{"LOWER": "swelling"}], "id": "swelling"},
    {"label": "symptom", "pattern": [{"LOWER": "bruising"}], "id": "bruising"},
    {"label": "symptom", "pattern": [{"LOWER": "stiffness"}], "id": "stiffness"},
    {"label": "symptom", "pattern": [{"LOWER": "popping"}], "id": "popping"},
    {"label": "symptom", "pattern": [{"LOWER": "numbness"}], "id": "numbness"},
    {"label": "symptom", "pattern": [{"LOWER": "tingling"}], "id": "tingling"},
    {
        "label": "symptom",
        "pattern": [{"LOWER": "limited"}, {"LOWER": "mobility"}],
        "id": "limited_mobility",
    },
    {
        "label": "symptom",
        "pattern": [
            {"LOWER": "limited"},
            {"LOWER": "range"},
            {"LOWER": "of"},
            {"LOWER": "motion"},
        ],
        "id": "limited_mobility",
    },
    {
        "label": "symptom",
        "pattern": [{"LOWER": "reduced"}, {"LOWER": "mobility"}],
        "id": "limited_mobility",
    },
    {"label": "symptom", "pattern": [{"LOWER": "limited"}], "id": "limited_mobility"},

    # Movement terms
    {"label": "MOVEMENT", "pattern": [{"LOWER": "jump"}]},
    {"label": "MOVEMENT", "pattern": [{"LOWER": "lunge"}]},
    {"label": "MOVEMENT", "pattern": [{"LOWER": "squat"}]},
]

ruler.add_patterns(patterns)
